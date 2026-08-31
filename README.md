<div align="center">

<img src="https://raw.githubusercontent.com/muhammad-abdullah-nova-dev/muhammad-abdullah-nova-dev/main/assets/header-banner.svg" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=22&duration=3000&pause=1000&color=5EEAD4&center=true&vCenter=true&width=600&lines=Building+systems+from+the+kernel+up;C%2B%2B+%C2%B7+React+%C2%B7+FastAPI+%C2%B7+MySQL;Currently%3A+deep+in+CLRS+and+deadlock+graphs;Every+crash+log+is+just+a+puzzle+in+disguise" alt="Typing SVG" />
</a>

<br/>

<a href="https://www.linkedin.com/in/muhammad-abdullah-b422723a8/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="mailto:m.abdullah.nova7@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-F0B429?style=for-the-badge&logo=gmail&logoColor=0A0E14" />
</a>
<a href="https://leetcode.com/u/FZiFbWTBhC/" target="_blank">
  <img src="https://img.shields.io/badge/LeetCode-5EEAD4?style=for-the-badge&logo=leetcode&logoColor=0A0E14" />
</a>
<a href="https://github.com/muhammad-abdullah-nova-dev" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-1A2332?style=for-the-badge&logo=github&logoColor=F0B429" />
</a>

<img src="https://komarev.com/ghpvc/?username=muhammad-abdullah-nova-dev&style=for-the-badge&color=5eead4&labelColor=0a0e14" alt="profile views"/>

</div>

<br/>

<div align="center">
<img src="https://raw.githubusercontent.com/muhammad-abdullah-nova-dev/muhammad-abdullah-nova-dev/main/assets/terminal-intro.svg" width="100%" />
</div>

<br/>

## `01` About Me

Most of what I build starts with a question I can't let go of: *what is this actually doing underneath?* That's what pulled me into building MaqOS — an operating system simulation in C++ where I hand-rolled scheduling and process lifecycle myself instead of trusting a library — and it's the same instinct behind SkyNet ATC, where every core data structure (hash table, min-heap, AVL tree, graph routing) is written from scratch instead of pulled from `std::`. Lately that instinct has pointed at computer vision: real-time hand tracking, gesture recognition, and background segmentation running at 30+ FPS, with a properly tested pipeline behind it rather than a notebook demo.

I'm a Software Engineering undergraduate at **FAST-NUCES**, and most of my time splits across four layers most people are happy to leave to a framework: systems (schedulers, process lifecycles, precedence graphs), computer vision (temporal modeling, gesture pipelines, real-time compositing), full-stack product work (the kind where a Redis TTL bug at 2am teaches you more about concurrency than a lecture ever will), and applied ML/data (cleaning it, modeling it, being honest about what the R² actually means). AI is now a first-class part of that stack too — wiring Gemini into a real interview-feedback pipeline, or FLUX diffusion into a gesture-driven AR workspace, not just calling an API and calling it a day.

```txt
const abdullah = {
    role: "SE Undergraduate @ FAST-NUCES",
    focus: ["Computer Vision", "Systems Programming", "Full-Stack Dev", "AI-Integrated Apps", "Applied ML"],
    currentlyLearning: "Design & Analysis of Algorithms — CLRS, cover to cover",
    philosophy: "Understand the machine before you trust the framework"
};
```

<br/>

## `02` Featured Work

<table>
<tr>
<td width="50%" valign="top">

### 🖐️ HandFrame AI
Gesture-driven AR workspace — track hands with MediaPipe, frame a region of your webcam feed with a two-hand gesture, then restyle it instantly with OpenCV or a cloud diffusion model.

**Stack:** Python · OpenCV · MediaPipe · fal.ai (FLUX.2)

- 1-Euro filter smoothing on hand landmarks to kill high-frequency jitter
- Gesture engine resolves pinch lifecycles, swipes, and holds into discrete intents
- Async architecture keeps 30+ FPS camera throughput while diffusion calls run in the background
- 55 passing tests

</td>
<td width="50%" valign="top">

### ✈️ AeroNova Airlines
Full-stack airline management SaaS — booking, seat locking, payments, boarding passes, end to end.

**Stack:** React · TypeScript · Node.js · Express · Sequelize · MySQL · Redis · Stripe

- JWT auth held in memory with httpOnly refresh cookies
- Redis-backed seat locking with 15-minute TTL to prevent double-booking
- PDFKit-generated boarding passes on successful payment

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📚 Aurelis
Grading and performance-tracking platform for teaching assistants, with separate TA, student, and read-only teacher views.

**Stack:** HTML5 · CSS3 · Vanilla JS · Supabase (PostgreSQL)

- Class links for self-service student enrollment with a TA approval workflow
- Bulk quiz grading with automated email notifications when marks post
- No-login, token-based read access for teachers monitoring class analytics
- Deployed: [Vercel](https://aurelis-student-performance-platfor.vercel.app/) · [GitHub Pages](https://muhammad-abdullah-nova-dev.github.io/aurelis-student-performance-platform/)

</td>
<td width="50%" valign="top">

### 🛰️ SkyNet ATC
Real-time air traffic control simulator where every core data structure is hand-rolled — no `std::unordered_map`, no `std::priority_queue`.

**Stack:** C++ · Qt

- Hash table (aircraft registry), min-heap (landing priority), AVL tree (flight log), graph + Dijkstra (routing) — all built from scratch
- 25×25 radar grid rendered live in a custom Qt `QWidget`
- Mid-flight emergency declarations jump an aircraft to the front of the landing queue in real time

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧠 HireMind AI
AI-powered mock interview platform — role-specific question generation, real-time feedback, and interview analytics.

**Stack:** Next.js 14 · TypeScript · PostgreSQL · Drizzle ORM · Gemini Pro API · Clerk

- Generates interview questions dynamically from job role, description, and experience level
- Speech-to-text answer capture feeding a Gemini-driven feedback engine (score + improvements)
- Husky-enforced pre-commit checks (ESLint, Prettier, type-check) and a CI pipeline on every push

</td>
<td width="50%" valign="top">

### 🚗 Ford Used Car Price Prediction
Regression pipeline predicting UK resale prices for 17,966 Ford listings, shipped with a live prediction site.

**Stack:** Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn

- Linear Regression + One-Hot Encoding — R² 0.840, RMSE £1,900, 5-fold CV std < 0.01
- 22-visualization EDA pass with residual analysis and learning curves to rule out overfitting
- Auto-extracts the notebook into a 10-page live site with an interactive prediction form → [ford-car-price-prediction.vercel.app](https://ford-car-price-prediction.vercel.app)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ✍️ InkFlow
Real-time collaborative text editor with CRDT-based conflict-free sync, live cursors, and sub-50ms latency over WebSockets.

**Stack:** React · TypeScript · Yjs · Django Channels · Redis

- Yjs CRDT sync means concurrent edits merge without a central lock or "last write wins" data loss
- Live user-presence indicators and per-collaborator cursor tracking
- Django Channels + Daphne backend broadcasting over WebSockets
- Deployed: [inkflow-teal.vercel.app](https://inkflow-teal.vercel.app/)

</td>
<td width="50%" valign="top">

### 🔧 NexusFlow
A UI/UX and enterprise-feature layer built on top of Flowise's open-source AI-workflow engine.

**Stack:** React · TypeScript · Material-UI · React Flow · Node.js/Express · PostgreSQL · Redis

- Redesigned dashboard, navigation, and theme-customization system on top of Flowise's existing visual flow builder and multi-LLM node architecture
- Maintains full compatibility with upstream Flowise workflows while focused on UX polish and enterprise auth/RBAC groundwork
- Built as a PNPM/Turbo monorepo with its own Docker Compose setup and load-testing config (Artillery)

</td>
</tr>
</table>

<br/>

## `03` Tech Arsenal

<div align="center">

**Languages**

<img src="https://skillicons.dev/icons?i=cpp,c,python,js,ts,html,css,java&theme=dark" />

**Computer Vision & AI**

<img src="https://skillicons.dev/icons?i=opencv&theme=dark" />
<img src="https://img.shields.io/badge/MediaPipe-00897B?style=for-the-badge&logo=google&logoColor=white" height="48" />
<img src="https://img.shields.io/badge/Gemini_API-F0B429?style=for-the-badge&logo=googlegemini&logoColor=0A0E14" height="48" />
<img src="https://img.shields.io/badge/fal.ai_FLUX-FF3366?style=for-the-badge&logoColor=white" height="48" />
<img src="https://img.shields.io/badge/Scikit--learn-5EEAD4?style=for-the-badge&logoColor=0A0E14" height="48" />
<img src="https://img.shields.io/badge/Pandas-F0729E?style=for-the-badge&logoColor=0A0E14" height="48" />
<img src="https://img.shields.io/badge/NumPy-1A2332?style=for-the-badge&logoColor=5EEAD4" height="48" />

**Frontend**

<img src="https://skillicons.dev/icons?i=react,nextjs,vite,tailwind&theme=dark" />

**Backend & Data**

<img src="https://skillicons.dev/icons?i=nodejs,express,fastapi,django,sequelize,mysql,postgres,redis&theme=dark" />
<img src="https://img.shields.io/badge/Stripe-5851DD?style=for-the-badge&logo=stripe&logoColor=white" height="48" />
<img src="https://img.shields.io/badge/Drizzle_ORM-C5F74F?style=for-the-badge&logo=drizzle&logoColor=1A2332" height="48" />
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=0A0E14" height="48" />

**Tools & Platforms**

<img src="https://skillicons.dev/icons?i=git,github,vscode,linux,figma,jira,docker,qt&theme=dark" />
<img src="https://img.shields.io/badge/GitHub_Actions-1A2332?style=for-the-badge&logo=githubactions&logoColor=5EEAD4" height="48" />

</div>

<br/>

## `04` GitHub Activity

<div align="center">

<img src="https://raw.githubusercontent.com/muhammad-abdullah-nova-dev/muhammad-abdullah-nova-dev/main/profile-summary-card-output/github_dark/1-repos-per-language.svg" width="60%" />

</div>

<br/>

## `05` Contribution Graph

<div align="center">

<!--START_SECTION:snake-->
<img src="https://raw.githubusercontent.com/muhammad-abdullah-nova-dev/muhammad-abdullah-nova-dev/output/github-snake-dark.svg" alt="snake animation" />
<!--END_SECTION:snake-->

</div>

<br/>

## `06` LeetCode Stats

<div align="center">

<img src="https://raw.githubusercontent.com/muhammad-abdullah-nova-dev/muhammad-abdullah-nova-dev/main/leetcode-stats-output/card.svg" />

</div>

<br/>

## `07` Recent Solves

<!--START_SECTION:leetcode-->

| Problem | Difficulty |
|---|---|
| [Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) | 🟡 Medium |
| [Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) | 🟡 Medium |
| [Minimum Operations to Form Subset Sum I](https://leetcode.com/problems/minimum-operations-to-form-subset-sum-i/) | 🟡 Medium |
| [Sum of Decoded Numbers](https://leetcode.com/problems/sum-of-decoded-numbers/) | 🟡 Medium |
| [Count Integers Appearing in a Single Block](https://leetcode.com/problems/count-integers-appearing-in-a-single-block/) | 🟢 Easy |

<!--END_SECTION:leetcode-->

<br/>

<div align="center">

> *"Every system I build is an argument for how I think the world should work — clean, deliberate, and built to last."*

<br/>

<details>
<summary><b>⚙️ One-time setup: profile cards, snake animation & LeetCode auto-updates</b></summary>

<br/>

**GitHub Activity cards (`04` section)**

1. Create a **Personal access token** (classic) with `repo` scope: [github.com/settings/tokens](https://github.com/settings/tokens/new).
2. In this repo, go to **Settings → Secrets and variables → Actions**, add a new secret named `SUMMARY_GITHUB_TOKEN` with that token as the value.
3. Create `.github/workflows/summary-cards.yml`:

```yaml
name: GitHub-Profile-Summary-Cards
on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch: {}
  push:
    branches: [ main ]

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    name: generate-github-profile-summary-cards
    steps:
      - uses: actions/checkout@v4
      - uses: vn7n24fzkq/github-profile-summary-cards@release
        env:
          GITHUB_TOKEN: ${{ secrets.SUMMARY_GITHUB_TOKEN }}
        with:
          USERNAME: muhammad-abdullah-nova-dev
          BRANCH_NAME: "main"
          UTC_OFFSET: 5
          AUTO_PUSH: true
```

4. Commit, then run it once manually from the **Actions** tab (**GitHub-Profile-Summary-Cards → Run workflow**). It writes SVGs to a `profile-summary-card-output/` folder committed to `main`, which the `04` section reads directly — no more live third-party API calls that can go down or rate-limit.
5. Swap `github_dark` in the three image URLs for any other [theme name](https://github.com/vn7n24fzkq/github-profile-summary-cards#themes) if you want a different look.

**Snake animation (`05` section)**

1. In this repo, go to **Settings → Actions → General → Workflow permissions**, select **Read and write permissions**, save.
2. Create `.github/workflows/snake.yml`:

```yaml
name: Generate Snake
on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch: {}
  push:
    branches: [ main ]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        id: snake
        with:
          github_user_name: muhammad-abdullah-nova-dev
          outputs: dist/github-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

3. Commit, then run it once manually from the **Actions** tab (**Generate Snake → Run workflow**) so `output` branch exists immediately instead of waiting for the next scheduled run.

**LeetCode stats card (`06` section)**

Replaces the `leetcode-stats-six.vercel.app` live API (unreliable/frequently down) with a card generated by your own workflow — same pattern as the other two.

1. Add `generate_leetcode_card.py` to the repo root.
2. Create `.github/workflows/leetcode-card.yml`:

```yaml
name: LeetCode Stats Card
on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch: {}
  push:
    branches: [ main ]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install requests
      - run: python generate_leetcode_card.py
        env:
          LEETCODE_USERNAME: FZiFbWTBhC
      - name: Commit if changed
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add leetcode-stats-output/card.svg
          git diff --staged --quiet || git commit -m "chore: update leetcode stats card"
          git push
```

3. Commit, then run it once manually from **Actions → LeetCode Stats Card → Run workflow**. It hits LeetCode's public GraphQL endpoint directly and writes `leetcode-stats-output/card.svg`, which the `06` section reads.
4. No secret needed — this one only reads public profile data, `GITHUB_TOKEN` (already provided by Actions) is enough to push the commit.

**LeetCode auto-updates (`07` section)**

Already set up — `.github/workflows/leetcode.yml` runs a custom `update_leetcode.py` script and has been committing updates on schedule. No action needed here.

The snake badge will look broken until its first successful run — that's expected on a new repo, not a sign anything is misconfigured.

</details>

<img src="https://raw.githubusercontent.com/muhammad-abdullah-nova-dev/muhammad-abdullah-nova-dev/main/assets/footer-banner.svg" width="100%"/>

</div>
