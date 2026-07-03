"""
Generates a self-hosted LeetCode stats SVG card, committed to the repo by a
GitHub Actions workflow instead of depending on a live third-party API.

Uses LeetCode's public GraphQL endpoint directly (no auth needed for public
profile data) with the standard matchedUser/submitStatsGlobal query used by
most community LeetCode-stats tools.
"""

import json
import os

import requests

USERNAME = os.environ.get("LEETCODE_USERNAME", "FZiFbWTBhC")
OUTPUT_DIR = "leetcode-stats-output"
OUTPUT_PATH = f"{OUTPUT_DIR}/card.svg"

QUERY = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile { ranking }
    submitStats: submitStatsGlobal {
      acSubmissionNum { difficulty count }
    }
  }
}
"""

# Palette matches the rest of the profile README (capsule-render header,
# summary cards) so this card doesn't look bolted-on.
BG_PANEL = "#1A2332"
BORDER = "#2A3441"
AMBER = "#F0B429"
TEAL = "#5EEAD4"
CORAL = "#F0729E"
TEXT = "#E5E9F0"
MUTED = "#8B95A5"

FONT = "JetBrains Mono, Consolas, monospace"


def fetch_stats(username: str) -> dict:
    resp = requests.post(
        "https://leetcode.com/graphql",
        json={"query": QUERY, "variables": {"username": username}},
        headers={
            "Content-Type": "application/json",
            # LeetCode's endpoint 403s requests without a Referer/UA that
            # look like a browser — this is the #1 cause of these tools
            # silently failing.
            "Referer": f"https://leetcode.com/u/{username}/",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
        },
        timeout=15,
    )
    resp.raise_for_status()
    payload = resp.json()

    user = payload.get("data", {}).get("matchedUser")
    if not user:
        raise RuntimeError(
            f"No LeetCode user found for '{username}'. "
            f"Response: {json.dumps(payload)[:500]}"
        )

    counts = {
        row["difficulty"]: row["count"]
        for row in user["submitStats"]["acSubmissionNum"]
    }
    ranking = (user.get("profile") or {}).get("ranking")

    return {
        "total": counts.get("All", 0),
        "easy": counts.get("Easy", 0),
        "medium": counts.get("Medium", 0),
        "hard": counts.get("Hard", 0),
        "ranking": ranking,
    }


def render_svg(stats: dict) -> str:
    width = 420
    bar_x = 96
    bar_max_w = 264
    rows = [
        ("Easy", stats["easy"], TEAL),
        ("Medium", stats["medium"], AMBER),
        ("Hard", stats["hard"], CORAL),
    ]
    scale_max = max(stats["easy"], stats["medium"], stats["hard"], 1)

    row_blocks = []
    y = 78
    row_h = 34
    for label, count, color in rows:
        bar_w = round((count / scale_max) * bar_max_w, 1)
        row_blocks.append(f"""
  <text x="24" y="{y + 14}" font-family="{FONT}" font-size="13" fill="{MUTED}">{label}</text>
  <rect x="{bar_x}" y="{y}" width="{bar_max_w}" height="14" rx="7" fill="{BORDER}"/>
  <rect x="{bar_x}" y="{y}" width="{bar_w}" height="14" rx="7" fill="{color}"/>
  <text x="{width - 24}" y="{y + 13}" font-family="{FONT}" font-size="13" fill="{TEXT}" text-anchor="end">{count}</text>""")
        y += row_h

    footer = ""
    if stats["ranking"]:
        footer = (
            f'<text x="24" y="{y + 16}" font-family="{FONT}" '
            f'font-size="12" fill="{MUTED}">Global rank #{stats["ranking"]:,}</text>'
        )
        y += 26
    else:
        y += 10

    height = y + 18

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" fill="{BG_PANEL}" stroke="{BORDER}" stroke-width="1"/>
  <text x="24" y="38" font-family="{FONT}" font-size="17" font-weight="700" fill="{AMBER}">LeetCode Stats</text>
  <text x="{width - 24}" y="38" font-family="{FONT}" font-size="17" font-weight="700" fill="{TEXT}" text-anchor="end">{stats["total"]} solved</text>
  <line x1="24" y1="52" x2="{width - 24}" y2="52" stroke="{BORDER}" stroke-width="1"/>
  {''.join(row_blocks)}
  {footer}
</svg>"""


def main():
    stats = fetch_stats(USERNAME)
    svg = render_svg(stats)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUTPUT_PATH} for '{USERNAME}':")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
