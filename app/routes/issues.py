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
        # store enum values so JSON serialization works; Pydantic will coerce back
        "priority": payload.priority.value,
        "status": IssueStatus.OPEN.value,
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


@router.put("/update/{issue_id}", response_model=IssueOut)
def update_issue(payload: IssueUpdate, issue_id: str):
    """update issue by id"""

    issues = load_data()

    # You need both the element and its position.
    # enumerate gives you the current index (idx) and the issue dict in one loop, so you can update the list item in place with issues[idx] = issue #

    for idx, issue in enumerate(issues):
        if issue["id"] == issue_id:
            if payload.title is not None:
                issue["title"] = payload.title
            if payload.description is not None:
                issue["description"] = payload.description
            if payload.priority is not None:
                issue["priority"] = payload.priority.value
            if payload.status is not None:
                issue["status"] = payload.status.value
            issues[idx] = issue
            save_data(issues)
            return issue

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """delete issue by id"""

    issues = load_data()

    for idx, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(idx)
            save_data(issues)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
