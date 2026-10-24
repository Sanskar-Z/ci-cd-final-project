# CI/CD Final Project — Counter Service

Starter project for the IBM/Coursera CI/CD Tools and Practices final project.

> Important: this is a starter package, not proof of a completed deployment. You must run GitHub Actions and deploy the pipeline in your course-provided OpenShift cluster, then capture your own screenshots and logs.

## Project structure

- `.github/workflows/workflow.yml` — GitHub Actions lint and unit-test workflow
- `.tekton/tasks.yml` — Tekton cleanup and nose test tasks
- `service/` — small Python Flask counter API
- `tests/` — unit tests
- `Dockerfile` — container image definition
- `requirements.txt` — Python dependencies

## Run locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m pytest
python -m flake8 service tests
python -m service.app
```

Open http://127.0.0.1:8080

## GitHub setup

1. Create a repository named `ci-cd-final-project` in your own GitHub account.
2. Extract this ZIP and push the files to your repository.
3. Open the **Actions** tab and inspect the workflow run.
4. Submit the actual URLs of `README.md`, `.github/workflows/workflow.yml`, and `.tekton/tasks.yml`.

## OpenShift / Tekton

OpenShift access is provided by the course environment; this ZIP cannot create a cluster, PVC, pipeline run, or screenshots on your behalf. Follow the lab instructions for connecting to the cluster and creating the `oc-pipelines-oc-final` pipeline. Adapt task parameters and workspaces to the course's cluster and catalog versions.

Suggested evidence filenames:
- `oc-pipelines-console-pvc-details.png`
- `oc-pipelines-oc-green.png`

Do not submit fabricated screenshots or logs. Capture the real successful run from your own environment.
