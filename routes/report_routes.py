from fastapi import APIRouter
import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/summary")
def general_summary():
    logger.info("GET /reports/summary called")
    


@router.get("/missions-by-status")
def get_missions_by_status():
    logger.info("GET /reports/missions-by-status called")



@router.get("/top-agent")
def get_top_agent():
    logger.info("GET /reports/top-agent called")
