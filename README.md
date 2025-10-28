Simple Flask App with DevOps (GitHub Actions)
This project is a minimal Flask application set up to demonstrate a full DevOps CI/CD pipeline using GitHub Actions.
Project Structure
app.py: The main Flask application.
test_app.py: Pytest unit tests for the application.
requirements.txt: Python dependencies.
Dockerfile: Used to build a container image for the application.
.github/workflows/: Contains the GitHub Actions.
ci.yml: Continuous Integration
build-push.yml: Continuous Delivery (Build Artifact)
deploy.yml: Continuous Deployment (Simulated)
DevOps Concepts Implemented
1. Continuous Integration (CI)
File: .github/workflows/ci.yml
This workflow runs automatically on every push or pull_request to the main branch. It ensures that new code meets quality standards before it can be merged.
Linting: Uses flake8 to check for Python code style errors and syntax issues.
Testing: Uses pytest to run all the unit tests in test_app.py.
Dependency: The test job only runs if the lint job succeeds, creating a chain of checks.
2. Continuous Delivery (CD) - Build
File: .github/workflows/build-push.yml
This workflow runs automatically after a push to the main branch (typically after the CI workflow has passed). Its job is to create the deployable artifact.
Containerization: Uses the Dockerfile to build a Docker image of the application.
Artifact Registry: It logs into GitHub Container Registry (GHCR) and pushes the newly built image, tagging it with the unique commit SHA. This image is now versioned and ready to be deployed.
3. Continuous Deployment (CD) - Deploy
File: .github/workflows/deploy.yml
This workflow is set to workflow_dispatch, meaning it must be triggered manually from the GitHub Actions tab. This is a common setup for production deployments, allowing a final human "go" signal.
Environments: It uses a GitHub Environment named production. You can configure this in your repository's settings to add required reviewers or environment-specific secrets.
Deployment (Simulated): The deploy job contains echo commands that simulate the steps of a real deployment (e.g., logging into a server, pulling the new Docker image from GHCR, and restarting the service).
