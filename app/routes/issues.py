from fastapi import APIRouter, HTTPException, status
import uuid
from app.schemas import IssueCreate, IssueOut, IssueUpdate, IssueStatus
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get(
    "/", response_model=list[IssueOut]
)  # treat response model as list of IssueOut schema
async def get_issues():
    """Retrieve all issues."""

    issues = load_data()

    return issues


@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create an issue."""

    issues = load_data()

    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": IssueStatus.OPEN,
    }

    issues.append(new_issue)

    save_data(issues)

    return new_issue


@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    """Retrieve specific issue by id"""
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:
            return issue

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
