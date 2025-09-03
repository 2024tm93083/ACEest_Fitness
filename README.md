# ACEest Fitness and Gym – DevOps Assignment

Flask-based fitness and gym management application demonstrating DevOps practices: version control with Git/GitHub, automated testing with Pytest, containerization with Docker, and CI/CD using GitHub Actions.

---

## 🚀 Project Overview

A minimal web API for a fitness/gym context:

- `POST /add_workout` — add a workout with duration (minutes)
- `GET  /workouts` — list logged workouts
- `GET  /` — health/status endpoint

Focus is on the DevOps pipeline (tests, Docker, CI) rather than full product features.

---

## 📁 Repository Structure

├── app.py  
├── requirements.txt    
├── tests/  
│ └── test_app.py   
├── Dockerfile  
├── .dockerignore   
├── .github/    
│ └── workflows/    
│ └── ci.yml    
└── README.md   


---

## 🧰 Prerequisites

- Python 3.11+
- (Optional to test locally) Docker Desktop / Docker Engine
- Git

---

## 🧑‍💻 Run Locally

### 1) Create and activate a virtualenv
**Windows (PowerShell):**
python -m venv venv
venv\Scripts\activate

**Linux/Mac**
python3 -m venv venv
source venv/bin/activate

### 2) Install dependencies
pip install -r requirements.txt

### 3) Start the app
python app.py


The app runs at:

http://127.0.0.1:5000

http://localhost:5000

🔌 Endpoints

Add a workout

PowerShell (Windows):

Invoke-WebRequest -Method POST `
  -Uri http://127.0.0.1:5000/add_workout `
  -ContentType "application/json" `
  -Body (@{ workout="Running"; duration=30 } | ConvertTo-Json)


curl (Linux/Mac/WSL):

curl -X POST http://127.0.0.1:5000/add_workout \
  -H "Content-Type: application/json" \
  -d '{"workout":"Running","duration":30}'


List workouts

curl http://127.0.0.1:5000/workouts

### ✅ Run Tests Locally

From the repo root (with venv active):

python -m pytest -q

### 🐳 Run with Docker (optional)

Build:

docker build -t aceest-fitness:dev .


Run:

docker run --rm -p 5000:5000 aceest-fitness:dev


Open http://localhost:5000

### ⚙️ GitHub Actions CI/CD Overview

The workflow file is at .github/workflows/ci.yml. It runs on every push and pull request.

Jobs:

test

Checks out the repository

Sets up Python 3.11

Installs dependencies (pip install -r requirements.txt)

Runs unit tests (python -m pytest -q)

Ensures Python can import the app by setting PYTHONPATH to the repo root

docker-build (runs only if tests pass)

Builds the Docker image using Buildx

Does not push to a registry (kept simple for coursework requirements)

Why this setup?

Guarantees tests run on clean runners for every change

Validates the Docker image builds successfully

Keeps the pipeline minimal, fast, and reproducible

### 🧩 Troubleshooting

ModuleNotFoundError: No module named 'app' in CI
The workflow sets PYTHONPATH to the workspace and invokes python -m pytest; if you modify paths, ensure tests import correctly.

Port already in use
Run with another port:

docker run -p 5001:5000 aceest-fitness:dev


Windows: python opens Microsoft Store
Disable the Python app alias (Settings → Apps → Advanced app settings → App execution aliases), or use py -3.