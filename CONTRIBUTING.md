# Contributing

## Branches
- `main`: released, production-ready code. Tagged releases only.
- `staging`: release candidate, verified before going to main.
- `dev`: integration branch. All work starts here.

Branch off `dev` using these prefixes:
- `feat/<topic>`: new features
- `fix/<topic>`: bug fixes
- `docs/<topic>`: documentation
- `data/<change>`: dataset changes
- `exp/<name>-<idea>`: experiments (may never merge)

Before starting any branch: `git switch dev && git pull`.

## Commits
We use [Conventional Commits](https://www.conventionalcommits.org/):
`<type>: <short description>`, e.g. `feat: add dvc pipeline`.
Types: `feat`, `fix`, `docs`, `chore`, `test`, `refactor`, `ci`, `data`.

## Pull requests
- Never push directly to `dev`, `staging` or `main`.
- Every PR needs 1 approval. Never approve your own PR.
- Never commit for another person.
- We use **squash merge** to keep history linear.
- Fill in the PR template.

## Data and secrets
- Data and models are tracked by DVC, never by Git.
- Run `dvc push` before `git push` whenever data or models change.
- DVC tokens live in `.dvc/config.local` and are **never** committed.
