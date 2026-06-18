from fastapi import APIRouter
import logging
from pydantic import BaseModel


class MissionInfo(BaseModel):
    title : str 
    description : str 
    location : str 
    difficulty : int
    importance : int
    status : str | str="NEW"
    risk_level : str
    assigned_agent_id : int | None

logger = logging.getLogger(__name__)

router = APIRouter()


# @router.post("")
# def create_mission(body: MissionInfo):
#     logger.info("POST /missions called")
#     from database import mission_db
#     ar = mission_db.MissionDB()
#     ar.create_mission(body)
    


@router.get("")
def get_all_missions():
    logger.info("GET /missions called")
    from database import mission_db
    ar = mission_db.MissionDB()
    result = ar.get_all_missions()
    return result

@router.put("/{id}/assign/{agent_id}")
def assign_mission_to_agent(id: int, agent_id: int):
    logger.info("PUT /missions/{id}/assign/{agent_id} called")
    from database import mission_db
    ar = mission_db.MissionDB()
    succesful = ar.assign_mission(id, agent_id)
    if not succesful:
        return "Failed to assign mission"
    return "Assigned mission"


@router.put("/{id}/start")
def mission_start(id: int, status: dict):
    logger.info("PUT /missions/{id}/start called")
    from database import mission_db
    ar = mission_db.MissionDB()
    succesful = ar.update_mission_status(id, status)
    if not succesful:
        return "Failed to update status"
    return "updated status successfully"

@router.put("/{id}/complete")
def mission_accomplished(id: int, status: dict):
    logger.info("PUT /missions/{id}/complete called")
    from database import mission_db
    ar = mission_db.MissionDB()
    succesful = ar.update_mission_status(id, status)
    if not succesful:
        return "Failed to update status"
    return "updated status successfully"


@router.put("/{id}/fail")
def mission_failed(id: int, status:dict):
    logger.info("PUT /missions/{id}/fail called")
    from database import mission_db
    ar = mission_db.MissionDB()
    succesful = ar.update_mission_status(id, status)
    if not succesful:
        return "Failed to update status"
    return "updated status successfully"


@router.put("/{id}/cancel")
def mission_cancelled(id: int, status:dict):
    logger.info("PUT /missions/{id}/cancel called")
    from database import mission_db
    ar = mission_db.MissionDB()
    succesful = ar.update_mission_status(id, status)
    if not succesful:
        return "Failed to update status"
    return "updated status successfully"