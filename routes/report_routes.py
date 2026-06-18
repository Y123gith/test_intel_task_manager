from fastapi import APIRouter
import logging


logger = logging.getLogger(__name__)

router = APIRouter()


# @router.get("/summary")
# def general_summary():
#     logger.info("GET /reports/summary called")
#     from database import mission_db
#     ar = mission_db.MissionDB()


@router.get("/missions-by-status")
def get_missions_by_status():
    logger.info("GET /reports/missions-by-status called")
    from database import mission_db
    ar = mission_db.MissionDB()
    open = ar.count_open_missions()
    in_progress = ar.count_by_status("IN_PROGRESS")
    completed = ar.count_by_status("COMPLETED")
    failed = ar.count_by_status("FAILED")
    cancelled = ar.count_by_status("CANCELLED")
    mission = {"open": open, "in_progress": in_progress, "completed": completed, "failed": failed, "cancelled": cancelled}
    return mission

# @router.get("/top-agent")
# def get_top_agent():
#     logger.info("GET /reports/top-agent called")
