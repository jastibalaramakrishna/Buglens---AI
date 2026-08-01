# BugLens AI - AI-Powered Bug Predictor Web Application

**Find the code most likely to break before it becomes a bug.**

BugLens AI is a modern, production-quality developer SaaS web application that analyzes GitHub repositories, AST code complexity, Git history, author churn, and defect commit patterns to predict which files are most likely to contain bugs.

---

## Architecture Overview

```
                      +-----------------------------------+
                      |   BugLens AI Next.js 14 Frontend  |
                      |   Dark Slate Developer SaaS UI    |
                      +-----------------+-----------------+
                                        |
                                        v
                      +-----------------+-----------------+
                      |    FastAPI Python REST Service    |
                      |   Orchestrator & REST Routers     |
                      +--------+----------------+---------+
                               |                |
            +------------------+                +------------------+
            |                                                      |
            v                                                      v
+-----------+-------------+                          +-------------+-----------+
| Git & AST Code Analyzer |                          | scikit-learn ML Engine  |
| - AST Complexity Parser |                          | - RandomForest Classifier|
| - Heuristic Bug Filter  |                          | - Feature Scaling & SHAP|
| - Author & Code Churn   |                          | - Explainable Risk Score|
+-------------------------+                          +-------------------------+
```

---

## Features

- **AST Code Complexity Parsing**: Computes Cyclomatic Complexity, Cognitive Complexity, Lines of Code (LOC), function counts, and nesting depth across Python, JavaScript, TypeScript, Go, Java, C++.
- **Git Commit Mining & Churn**: Parses Git logs, classifies bug-fix commits via heuristic keyword analysis (`fix`, `bug`, `issue`, `hotfix`, `defect`), measures author churn and code modification velocity.
- **Explainable Machine Learning Model**: Uses scikit-learn (`RandomForestClassifier` + `StandardScaler`) to calculate `bug_probability`, normalize 0–100 `risk_score`, and assign risk levels (`Critical`, `High`, `Medium`, `Low`, `Safe`).
- **Explainability Guarantee**: Breakdowns risk scores into explicit factor percentages (Complexity, Change Frequency, Bug-Fix History, Contributor Churn, Code Churn).
- **Interactive Code Viewer**: Syntax-highlighted editor with line numbers, flagged risk zones, and hover tooltips.
- **Actionable AI Recommendations**: Formulates refactoring strategies, guard clause previews, and unit test suggestions tailored to code smells.
- **Complexity Hotspots & Git Timeline Charts**: Visualizes risk distribution, complexity scatter charts, and commit timelines using Recharts.
- **Instant Demo Mode**: Pre-populated with real open-source repositories (`facebook/react`, `expressjs/express`, `fastapi/fastapi`).

---

## Directory Structure

```
buglens-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py          # REST API endpoints
│   │   ├── analyzers/
│   │   │   ├── code_analyzer.py   # AST & complexity metrics
│   │   │   └── git_analyzer.py    # Git commit log parser & bug fix filter
│   │   ├── ml/
│   │   │   └── risk_model.py      # scikit-learn ML model & factor scoring
│   │   ├── services/
│   │   │   └── ai_recommender.py  # AI refactoring recommendation generator
│   │   ├── database.py            # SQLAlchemy SQLite schema & models
│   │   ├── main.py                # FastAPI entry point
│   │   └── seed_demo.py           # Demo repository seeder
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── app/                   # Next.js App Router pages
    │   ├── components/            # UI components (MetricCard, RiskBadge, CodeViewer, etc.)
    │   ├── lib/                   # API client & demo data
    │   └── types/                 # TypeScript interfaces
    ├── package.json
    ├── tailwind.config.js
    └── tsconfig.json
```

---

## Quick Setup Instructions

### 1. Backend Setup (FastAPI + Python ML)

```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
# source venv/bin/activate

pip install -r requirements.txt
python -m app.main
```
Backend API will start at: `http://localhost:8000` (API Docs: `http://localhost:8000/docs`).

### 2. Frontend Setup (Next.js 14)

```bash
cd frontend
npm install
npm run dev
```
Frontend Web App will run at: `http://localhost:3000`.

---

## Environment Variables

### Backend (`backend/.env`)
```env
DATABASE_URL=sqlite:///./buglens.db
GITHUB_TOKEN=your_optional_github_pat_here
```

### Frontend (`frontend/.env.local`)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

---

## Machine Learning Methodology

1. **Feature Extraction**:
   - `loc`: Lines of code
   - `cyclomatic_complexity`: AST decision branch nodes
   - `cognitive_complexity`: Nesting depth weighted complexity
   - `commit_count`: Historical change count
   - `bug_fix_commits_count`: Commit messages containing defect keywords
   - `contributors_count`: Unique author count
   - `code_churn`: Sum of added and deleted lines

2. **Model Training**:
   - Standardized using `StandardScaler`
   - Trained via `RandomForestClassifier(n_estimators=100)`
   - Computes probability output `bug_probability` mapped to 0-100 `risk_score`.

---

## Verification & User Flow Test

1. Launch Landing Page (`/`): Inspect hero section and miniature dashboard preview.
2. Click **Demo Mode** or **Analyze a Repository**: Loads instant pre-computed open-source repositories (`facebook/react`).
3. View **Dashboard**: Check Overall Risk, High-Risk Files, Complexity Hotspots, and Risk Distribution.
4. Navigate to **File Risk Explorer** (`/files`): Filter and sort files by risk score or cyclomatic complexity.
5. Open **File Detail Page** (`/files/1`): Inspect explainable risk factors, line-annotated Code Viewer, and AI Recommendations.
6. Explore **Complexity Hotspots** (`/hotspots`) and **Git History** (`/history`).
