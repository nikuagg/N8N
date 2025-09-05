from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    workflow = Column(String, index=True)
    platform = Column(String, index=True)
    popularity_metrics = Column(JSON)
    country = Column(String, index=True)
