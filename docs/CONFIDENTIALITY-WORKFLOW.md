# Confidentiality and Contribution Workflow

This procedure records the agreed boundary between SQA work in the official project repository
and public evidence in the portfolio repository. The repositories have different purposes and
must remain separate: the portfolio is not a mirror of the official project.

## 1. Repository roles

| Repository | Purpose | Content |
|---|---|---|
| Official project repository | Current team work and authorized SQA contribution | Project source and internal evidence; for SQA work, use only branch `sqa` and only the authorized SQA scope |
| Portfolio repository | Demonstrate SQA and DApp skills publicly | Sanitized descriptions, generic examples, local mocks, and evidence explicitly approved for publication |

Keep the repositories in separate working directories. Never clone the official repository inside
the portfolio folder, copy its full source tree into the portfolio, or configure one repository as
a mirror of the other.

The official project uses these branch roles for this workflow:

| Branch | Use | Rule |
|---|---|---|
| `sqa` | SQA working branch | Make and push authorized SQA changes here only. The official SQA boundary currently limits changes to `.docs/SQA/`. |
| `dev` | Current team work reference | Read it to understand the latest team baseline. Do not commit or push SQA work to it. |
| Other branches, including `main` | Outside this SQA workflow | Do not modify them as part of this procedure. |

When checking current team work, record the exact `dev` commit SHA used as the SQA baseline.
Do not merge, rebase, cherry-pick, or push between `dev` and `sqa` unless the project owner
explicitly approves that integration step. If test-code changes outside `.docs/SQA/` are needed,
stop and obtain an updated scope approval before editing those files.

## 2. Information handling

| Information | Portfolio handling |
|---|---|
| Proprietary source code, business logic, internal architecture | Do not publish or copy |
| Internal URLs, endpoints, infrastructure, dashboards, or environment names | Do not publish |
| Credentials, tokens, private keys, seed phrases, customer or employee data | Never publish; use synthetic data in examples |
| Screenshots, recordings, logs, API payloads, and bug details from the official project | Keep in approved project storage; publish only with written project-owner approval and after sanitization |
| Project or client name, logo, PR link, contract address, or deployment details | Publish only when explicitly approved |
| Generic testing methods and newly written mock examples | May be published if they do not reveal project-specific information |
| Public test results and metrics | Publish only when reproducible, accurate, and approved for the audience |

If permission or classification is unclear, keep the material private and ask the project owner.
Removing a name alone does not make confidential source, architecture, or evidence safe to publish.

## 3. Work procedure

### Step 1 — Confirm access and scope

Before opening or changing the official project:

1. Confirm you have authorization to access the repository and the target environment.
2. Confirm which QA or DApp tasks are in scope and which test data/environment may be used.
3. Confirm whether the project name, screenshots, PR links, test results, and contribution summary
   may be mentioned publicly.
4. Record publication restrictions in private project notes, not in this public portfolio.

Do not run tests against production or third-party services unless the project owner explicitly
authorizes that exact target and activity.

### Step 2 — Keep local checkouts separate

The local official checkout and portfolio checkout must be separate directories. Set these example
variables to the actual local paths for your machine; do not publish personal filesystem paths:

```powershell
$ProjectRepo = 'D:\work\official-project'
$PortfolioRepo = 'D:\work\portfolio_nilo_web3_sqa'
```

- `$ProjectRepo` is a placeholder path for the separately cloned official repository.
- `$PortfolioRepo` is a placeholder path for the local portfolio directory.
- These assignments only define paths in the current PowerShell session; they do not clone,
  modify, or publish either repository.

Before work, verify the official project checkout and portfolio checkout independently:

```powershell
git -C $ProjectRepo rev-parse --show-toplevel
git -C $ProjectRepo remote -v
git -C $ProjectRepo status --short --branch
git -C $ProjectRepo branch --show-current

git -C $PortfolioRepo rev-parse --show-toplevel
git -C $PortfolioRepo remote -v
git -C $PortfolioRepo status --short --branch
git -C $PortfolioRepo branch --show-current
```

- `git -C <directory>` runs that Git command against the specified directory, reducing the risk
  of working in the wrong repository.
- `rev-parse --show-toplevel` prints the repository root. Stop if it fails or shows an unexpected
  directory.
- `remote -v` shows the configured fetch and push URLs. Confirm they point to the intended repo;
  never assume the local portfolio folder is connected to the public GitHub repo.
- `status --short --branch` shows the current branch and uncommitted changes. Review it before
  editing, committing, or switching branches.
- `branch --show-current` prints the active branch. For official SQA edits it must print `sqa`;
  stop if it prints another branch.

If Git is unavailable, the directory is not a Git checkout, or a remote is unexpected, stop before
committing or pushing. Resolve repository setup separately and verify it again.

### Step 3 — Read the latest team baseline and work only on SQA

Read `dev` as the latest team-work reference, then keep the SQA work on branch `sqa`. Fetching
updates remote-tracking information locally; it does not push changes:

```powershell
git -C $ProjectRepo fetch origin dev
git -C $ProjectRepo log -1 --format="%H %s" origin/dev
git -C $ProjectRepo switch sqa
git -C $ProjectRepo status --short --branch
```

- `fetch origin dev` retrieves the current `dev` reference without changing the checked-out files.
- `log ... origin/dev` displays the exact `dev` SHA and commit subject to record as the baseline.
- `switch sqa` selects the existing SQA branch; it does not create a new branch.
- If the local `sqa` branch does not exist, stop and ask the project owner before creating it.
- The final status command confirms the branch and checks for pre-existing changes. Do not overwrite
  or discard unreviewed work.

If Git reports uncommitted changes, stop and inspect them before switching branches. Do not use
force, reset, or cleanup commands to make the working tree appear clean. Do not merge `dev` into
`sqa` as an automatic way to update the baseline; get the owner's approval for any branch
integration.

Only make changes inside `.docs/SQA/` under the currently approved SQA scope. Keep source code,
application configuration, workflows, and other documentation unchanged unless the project owner
formally expands the scope.

After implementation:

1. Run only checks authorized for the approved environment and scope.
2. Record the branch, `dev` baseline SHA, SQA commit SHA, environment, commands, actual results,
   limitations, and private evidence location in the SQA run record.
3. Review the diff and output for secrets, real personal data, and unrelated changes.
4. Commit and open a PR from `sqa` according to the official project's contribution process.
5. Keep internal issue details, review discussion, and restricted artifacts in approved private
   project systems.

### Step 4 — Create portfolio evidence separately

The portfolio repository is not a second working copy of the official project. Do not copy official
source files, tests, reports, screenshots, or logs into it. Instead:

1. Write a short role and contribution summary using only facts that are approved for disclosure.
2. Recreate a generic example in the portfolio or its local mock, using synthetic data and
   independently written code.
3. Link a PR, screenshot, demo, or test report only when the owner has approved that exact item
   for public access.
4. Keep claims measurable and reproducible. Label drafts `TODO` or `EXAMPLE` until verified.
5. If the project name is restricted, use a generic label such as “Confidential company-profile
   project” and remove identifying details.

The public portfolio should show the skill and process, not expose the product's implementation.

### Step 5 — Review before publishing

Before committing portfolio content:

1. Confirm written approval for every project-specific name, artifact, result, and link. If approval
   is absent or unclear, anonymize the project and omit project-specific artifacts and links.
2. Search the proposed change for domains, endpoints, account names, tokens, private keys, real
   personal data, internal issue IDs, and copied proprietary text/code.
3. Inspect screenshots and logs visually; redact or replace them rather than relying on filenames
   or metadata.
4. Review the exact portfolio diff and verify the current directory, branch, and remote.
5. Run the repository's appropriate local checks. Do not describe a check as passed unless it was
   actually run, and state whether it used a local mock or the real authorized target.
6. Publish only after all approvals and checks are complete.

### Commit author and Copilot attribution

The portfolio owner does not want Copilot recorded as a contributor or co-author on commits. For
both repositories:

1. Do not add a `Co-authored-by: Copilot ...` trailer or any Copilot identity to a commit message.
2. Do not set Git's commit author or committer identity to Copilot.
3. Before committing, inspect the configured identity and the final commit message. Use only the
   user's authorized Git identity and the repository's contribution rules.
4. If a tool or integration would create a commit attributed to Copilot, stop before committing
   and use an approved user-authored workflow instead.

This controls commit author/co-author metadata. It cannot remove Copilot attribution from commits
that already exist, change repository collaborator permissions, or guarantee how GitHub displays
contributors for unrelated existing commits.

For this portfolio, `SECURITY.md`, `AGENTS.md`, and `PUBLISH-CHECKLIST.md` remain the controlling
repository guidance. This procedure does not override an NDA, client agreement, employer policy, or
the official project's rules.

## 4. Separate-repository command reference

These are examples, not commands to run blindly. Replace paths and names with verified values.

```powershell
git -C $ProjectRepo status --short --branch
git -C $ProjectRepo diff -- .docs/SQA
git -C $ProjectRepo diff --check
```

- `status --short --branch` confirms the checkout is on `sqa` and lists working-tree changes.
- `diff -- .docs/SQA` shows tracked changes in the permitted SQA directory. Review untracked files
  separately; do not stage unrelated work.
- `diff --check` checks the current tracked diff for whitespace errors; it does not test the
  application or detect confidential information.

After an approved contribution, a team-approved commit may look like:

```powershell
git -C $ProjectRepo add .docs\SQA\path\to\approved\document.md
git -C $ProjectRepo diff --cached --check
git -C $ProjectRepo diff --cached
git -C $ProjectRepo commit -m "docs(sqa): update approved SQA evidence"
```

- `add` stages only the named file under `.docs/SQA/`. Review the staged diff and make sure no
  paths outside the authorized SQA folder are staged.
- `diff --cached --check` and `diff --cached` review the staged content before committing.
- `commit` records staged changes in the current repository and branch. It does not publish them.
  Follow the official project's message conventions and do not add a Copilot co-author trailer.

Before pushing an official SQA contribution, verify the remote, branch, author, staged content,
and commit attribution:

```powershell
git -C $ProjectRepo remote -v
git -C $ProjectRepo branch --show-current
git -C $ProjectRepo log -1 --format="%an <%ae>%n%cn <%ce>%n%B"
git -C $ProjectRepo push origin sqa
```

- Confirm the remote is the official project repository, the current branch is `sqa`, and the
  author and committer are the user's authorized identity.
- The log command displays the latest commit's author, committer, and full message so any
  co-author trailer can be reviewed before publishing.
- `push origin sqa` pushes only the `sqa` branch to the `origin` remote. Never replace `sqa` with
  `dev` or another branch for SQA work.
- If any check is unexpected, stop; do not push.

For the portfolio repository, use the portfolio path explicitly and stage only approved,
sanitized portfolio files. The GitHub remote must be the user's portfolio repository, never the
official project repository:

```powershell
git -C $PortfolioRepo status --short --branch
git -C $PortfolioRepo diff --check
git -C $PortfolioRepo add docs\CONFIDENTIALITY-WORKFLOW.md
git -C $PortfolioRepo diff --cached --check
git -C $PortfolioRepo diff --cached
```

- The first command confirms the portfolio checkout and branch.
- The second checks formatting in the tracked diff; it is not a confidentiality scan.
- `add` stages this procedure only. The final commands review exactly what is staged before a
  commit or push.

For the first publication to an empty portfolio repository, review every file that will be included
before the initial push. After committing approved portfolio content, a normal first push may be:

```powershell
git -C $PortfolioRepo remote -v
git -C $PortfolioRepo branch --show-current
git -C $PortfolioRepo log -1 --format="%an <%ae>%n%cn <%ce>%n%B"
git -C $PortfolioRepo push -u origin main
```

- Confirm `origin` is `https://github.com/prstiio/portfolio_nilo_web3_sqa`, the branch is the
  intended portfolio branch (`main` in this example), and the commit attribution contains no
  Copilot author or co-author.
- `push -u origin main` publishes local `main` and sets its upstream. If GitHub already has
  commits, or Git rejects the push, stop and reconcile safely; never force-push.
- A push publishes content publicly. It does not replace reviewing every file and confirming
  publication permission.

Do not use `git add -f` to bypass ignore rules for environment files or generated secrets. Never
push the official project's code, branch, or SQA evidence to the portfolio remote. Before pushing
portfolio documentation, confirm the remote URL points to `prstiio/portfolio_nilo_web3_sqa`,
review the staged diff, and obtain publication approval for any project-specific information.
Push only the portfolio branch intended for publication; do not push to the official project.

## 5. Simple decision rule

Official project workspace: branch `sqa` only for authorized SQA work; branch `dev` is a
read-only reference for the latest team baseline. Portfolio workspace: publish only separately
written, sanitized, approved material to the portfolio repository. Never mirror the official repo.
If permission or attribution is uncertain, stop and ask before proceeding.
