"""
Verification test script for BugLens AI backend
"""
import sys
import os

# Ensure backend path is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def test_backend_integrity():
    print("[Verification] Testing Database initialization...")
    from app.database import init_db, SessionLocal, Repository, FileMetric
    init_db()
    print("[OK] Database initialized.")

    print("[Verification] Testing Seed script...")
    from app.seed_demo import seed_demo_data
    seed_demo_data()
    db = SessionLocal()
    repos = db.query(Repository).all()
    assert len(repos) > 0, "No repositories seeded"
    print(f"[OK] Seeded {len(repos)} repositories successfully.")

    print("[Verification] Testing AST Code Analyzer...")
    from app.analyzers.code_analyzer import CodeAnalyzer
    sample_code = """
def test_func(x):
    if x > 10:
        if x < 20:
            return x * 2
    return 0
"""
    res = CodeAnalyzer.analyze_source_code(sample_code, "test.py")
    assert res["cyclomatic_complexity"] >= 2
    print(f"[OK] AST Code Analyzer passed (Cyclomatic: {res['cyclomatic_complexity']}, Cognitive: {res['cognitive_complexity']}).")

    print("[Verification] Testing ML Risk Model...")
    from app.ml.risk_model import MLRiskModel
    model = MLRiskModel()
    risk = model.predict_file_risk({
        "loc": 500,
        "cyclomatic_complexity": 25,
        "cognitive_complexity": 30,
        "nesting_depth": 5,
        "commit_count": 50,
        "bug_fix_commits_count": 12,
        "contributors_count": 8,
        "code_churn": 2000
    })
    print(f"[OK] ML Risk Model predicted risk score: {risk['risk_score']} ({risk['risk_level']}).")

    print("[Verification] ALL BACKEND VERIFICATIONS PASSED CLEANLY!")

if __name__ == "__main__":
    test_backend_integrity()
