from fastapi import APIRouter
import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("")
def create_mission():
    logger.info("POST /missions called")


@router.get("")
def get_all_missions():
    logger.info("GET /missions called")


@router.put("/{id}/assign/{agent_id}")
def assign_mission_to_agent(id: int, agent_id: int):
    logger.info("PUT /missions/{id}/assign/{agent_id} called")



@router.put("/{id}/star")
def mission_start(id: int):
    logger.info("PUT /missions/{id}/start called")



@router.put("/{id}/complete")
def mission_accomplished(id: int):
    logger.info("PUT /missions/{id}/complete called")



@router.put("/{id}/fail")
def mission_failed(id: int):
    logger.info("PUT /missions/{id}/fail called")



@router.put("/{id}/cancel")
def mission_cancelled(id: int):
    logger.info("PUT /missions/{id}/cancel called")
