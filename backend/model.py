from pydantic import BaseModel
from typing import List

class CoursePerformance(BaseModel):
    course_name: str
    average_score: float

class DashboardResponse(BaseModel):
    data: List[CoursePerformance]