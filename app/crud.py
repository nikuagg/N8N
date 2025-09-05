from sqlalchemy.orm import Session
from . import models

def get_all_workflows(db: Session):
    return db.query(models.Workflow).all()

def get_workflows_by_platform(db: Session, platform: str):
    return db.query(models.Workflow).filter(models.Workflow.platform == platform).all()

def save_workflows(db: Session, workflows: list):
    for wf in workflows:
        # Check duplicate
        exists = db.query(models.Workflow).filter(
            models.Workflow.workflow == wf["workflow"],
            models.Workflow.platform == wf["platform"]
        ).first()
        if not exists:
            db.add(models.Workflow(**wf))
    db.commit()
