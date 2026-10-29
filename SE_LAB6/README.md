# LAB6 — Marathon Registration (Code and Branch Coverage)

This folder contains the Lab 6 application, separate pytest test files, and terminal screenshots for coverage analysis.

## Files
- `marathon_registration.py` — application under test
- `CodeCoverageTest_marathon_registration.py` — test suite for the code coverage run
- `BranchCoverageTest_marathon_registration.py` — test suite for the branch coverage run
- `screenshots/code_coverage_terminal.png` — code coverage terminal report
- `screenshots/branch_coverage_terminal.png` — branch coverage terminal report

## Install
Run from the LAB6 directory:
```powershell
python -m pip install pytest coverage
```

## Code coverage
```powershell
python -m coverage erase
python -m coverage run --source=marathon_registration -m pytest -q CodeCoverageTest_marathon_registration.py
python -m coverage report -m
```

## Branch coverage
```powershell
python -m coverage erase
python -m coverage run --branch --source=marathon_registration -m pytest -q BranchCoverageTest_marathon_registration.py
python -m coverage report -m
```

The included screenshots show the successful terminal runs captured during local testing. Re-run the commands locally if you need to reproduce them.
