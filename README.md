
# Docker-Based DevOps CI/CD Project

A beginner-friendly DevOps project demonstrating a Python Flask web application, automated testing, Docker containerization, and continuous integration using GitHub Actions.

## 🚀 Project Overview

This project demonstrates how a web application can be tested automatically and packaged into a Docker image whenever code is pushed to GitHub.

The goal is to understand the basic DevOps workflow and reduce manual testing and build steps.

## 🛠️ Technologies Used

- **Python** — application development
- **Flask** — web framework
- **Pytest** — automated testing
- **Docker** — application containerization
- **Git & GitHub** — version control and source code hosting
- **GitHub Actions** — CI/CD workflow automation
- **HTML & CSS** — website interface

## ⚙️ Project Workflow

1. Write or update the application code.
2. Push the changes to the GitHub repository.
3. GitHub Actions automatically starts the workflow.
4. Python dependencies are installed.
5. Automated tests run using Pytest.
6. Docker builds an image if the previous steps succeed.
7. The application can be run locally inside a Docker container.

## 📁 Project Structure

```text
docker-cicd-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── tests/
│   └── test_app.py
├── app.py
├── dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## ▶️ Run the Project Locally

### Prerequisites

Install Python, Git, and Docker Desktop.

### 1. Clone the repository

```bash
git clone https://github.com/kotwalurja-03/docker-cicd-project.git
cd docker-cicd-project
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run automated tests

```bash
python -m pytest
```

### 4. Build the Docker image

```bash
docker build -t docker-cicd-project .
```

### 5. Run the container

```bash
docker run -d --name devops-web -p 5000:5000 docker-cicd-project
```

Open the application in your browser:

http://localhost:5000

Health-check endpoint:

http://localhost:5000/health

If a container named `devops-web` already exists, remove or rename that specific container before running the command again.

## 🔄 CI/CD Automation

The GitHub Actions workflow is stored in `.github/workflows/ci-cd.yml`.

It is configured to run on pushes and pull requests targeting the `main` branch, and can also be started manually if the workflow includes `workflow_dispatch`.

The workflow checks the application by running automated tests and building a Docker image. This project builds the image locally in the GitHub Actions runner; publishing the image to a container registry or deploying it to a cloud server is not included unless configured separately.

To view the workflow results, open the repository on GitHub and select the **Actions** tab.

## 🩺 Health Check

The `/health` endpoint returns a JSON response indicating whether the Flask application is responding.

Expected response:

```json
{
  "status": "healthy"
}
```

## 🎯 Learning Outcomes

- Understanding the DevOps lifecycle
- Using Git and GitHub for version control
- Writing automated tests with Pytest
- Creating and building Docker images
- Running applications in containers
- Automating test and build steps with GitHub Actions
- Understanding the difference between CI, containerization, and deployment

## 🔮 Future Improvements

- Publish Docker images to Docker Hub
- Add application deployment to a hosting platform
- Add code-quality and security checks
- Improve monitoring and logging
- Add deployment status badges to the README

## 👩‍💻 Author

**Urja Kotwal**

GitHub: https://github.com/kotwalurja-03

---

*This project was created for hands-on learning of fundamental DevOps concepts.*
