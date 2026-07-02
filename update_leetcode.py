"""
Fetches recently-solved LeetCode problems for a given public profile and
writes them into the README between the leetcode markers.

Uses LeetCode's public GraphQL endpoint (no login/API key required) to pull
recent accepted submissions, then rewrites the section of README.md between
<!--START_SECTION:leetcode--> and <!--END_SECTION:leetcode-->.
"""

import json
import re
import sys
import urllib.request

LEETCODE_USERNAME = "FZiFbWTBhC"
README_PATH = "README.md"
MAX_PROBLEMS = 5

GRAPHQL_URL = "https://leetcode.com/graphql"
QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    title
    titleSlug
    timestamp
  }
}
"""

DIFFICULTY_EMOJI = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴",
}


def fetch_recent_submissions(username, limit):
    payload = json.dumps({
        "query": QUERY,
        "variables": {"username": username, "limit": limit},
    }).encode("utf-8")

    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/u/{username}/",
            "Origin": "https://leetcode.com",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )

    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    submissions = data.get("data", {}).get("recentAcSubmissionList", [])
    if not submissions:
        raise RuntimeError(
            "No submissions returned — profile may be private, "
            "username may be wrong, or LeetCode may be rate-limiting."
        )
    return submissions


def fetch_difficulty(title_slug):
    """Best-effort difficulty lookup; falls back to no emoji if it fails."""
    query = """
    query questionDifficulty($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
      }
    }
    """
    payload = json.dumps({
        "query": query,
        "variables": {"titleSlug": title_slug},
    }).encode("utf-8")

    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Origin": "https://leetcode.com",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["data"]["question"]["difficulty"]
    except Exception:
        return None


def build_table(submissions):
    rows = [
        "| Problem | Difficulty |",
        "|---|---|",
    ]
    for sub in submissions[:MAX_PROBLEMS]:
        title = sub["title"]
        slug = sub["titleSlug"]
        url = f"https://leetcode.com/problems/{slug}/"
        difficulty = fetch_difficulty(slug)
        emoji = DIFFICULTY_EMOJI.get(difficulty, "")
        label = f"{emoji} {difficulty}".strip() if difficulty else "—"
        rows.append(f"| [{title}]({url}) | {label} |")
    return "\n".join(rows)


def update_readme(table_markdown):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"(<!--START_SECTION:leetcode-->)(.*?)(<!--END_SECTION:leetcode-->)",
        re.DOTALL,
    )

    if not pattern.search(content):
        raise RuntimeError(
            "Could not find leetcode markers in README.md — "
            "make sure <!--START_SECTION:leetcode--> and "
            "<!--END_SECTION:leetcode--> are both present."
        )

    new_content = pattern.sub(
        rf"\1\n\n{table_markdown}\n\n\3", content
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    try:
        submissions = fetch_recent_submissions(LEETCODE_USERNAME, MAX_PROBLEMS)
    except Exception as e:
        print(f"Failed to fetch submissions: {e}", file=sys.stderr)
        sys.exit(1)

    table = build_table(submissions)
    update_readme(table)
    print("README updated with recent LeetCode submissions.")


if __name__ == "__main__":
    main()
