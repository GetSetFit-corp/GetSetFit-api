from fastapi import APIRouter
from typing import Dict

router  =APIRouter()

@router.get("", summary="HealthCheck", description="To check whether system is up or not", response_model=Dict)
async def health_check():
    return {"status": "ok"}