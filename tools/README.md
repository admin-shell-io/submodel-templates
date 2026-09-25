# Bug-fix automation

Maintainers edit only the template JSON of a bug-fix release. Everything else
(bug-fix folder, AASX packages, README, pull request, checks) is automatic.

## Fixing a reported bug

1. Check the issue against the specification PDF. If it is not a real bug,
   answer and close it.
2. Add three labels to the issue: `bugfix`, the SMT (e.g. `IDTA 02006`) and the
   version (e.g. `v3.0`).
3. A draft pull request appears, with the next bug-fix folder, for example
   `published/Digital nameplate/3/0/3/`. If a bug-fix PR for that SMT version is
   already open, the issue is added to it instead.
4. Correct the template JSON in that folder on the PR branch.
5. On every push the AASX packages are rebuilt from the JSON and the checks run.
6. Review and merge. The issues are closed and told which release fixed them.

One issue covers one SMT. For a bug in several SMTs, open one issue per SMT.

## What a bug-fix folder contains

- the template JSON (the only file edited by hand)
- one AASX per AAS metamodel version, generated from the JSON
- a README listing the fixed issues and linking the unchanged specification PDF

The PDF is linked, not copied. There is no `_forAASMetamodelV3.1.json` copy: AAS
JSON carries no metamodel version, so one JSON serves all of them.

## Checks on every pull request (`check_release.py`)

1. Released files are never changed. A correction goes into a new bug-fix
   folder. Allowed: editing a README, moving a file unchanged to `deprecated/`.
2. Every AASX matches its template JSON.
3. README links resolve.

## Settings (`smt-config.yml`)

- `aas_versions`: AAS metamodel versions new bug-fix releases are built for.
  For a new metamodel, add it here and its `aas-core` package to
  `requirements.txt`. Existing releases are not touched.
- `smts`: SMT label to folder. After adding an SMT, run
  `python tools/create_labels.py --apply`.

## Running the tools locally

```
pip install -r tools/requirements.txt
python tools/new_bugfix.py --labels "bugfix,IDTA 02002,v1.0" --issue 206
python tools/build_aasx.py "published/Contact Information/1/0/2"
python tools/build_aasx.py --check --changed-since origin/main
python tools/check_release.py --base origin/main
python tools/create_labels.py            # dry run
```

## One-time repository setup

- Run `python tools/create_labels.py --apply`.
- Settings > Actions > General: allow GitHub Actions to create pull requests.
- Optional: a `BOT_TOKEN` secret (GitHub App or fine-grained token, contents:
  write), so the commit with the rebuilt AASX starts the checks again. Needed
  only if branch protection requires status checks.
