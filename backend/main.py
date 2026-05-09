from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import DashboardResponse
from mock_data import mock_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/performance", response_model=DashboardResponse)
def get_performance():
    return {"data": mock_data}