from fastapi import APIRouter

issues = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@issues.get("/")
async def get_issues():
    return []
