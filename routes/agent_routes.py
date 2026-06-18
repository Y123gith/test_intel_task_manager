from fastapi import APIRouter
import logging


logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("")
def create_agent():
    logger.info("POST /agents called")
    


@router.get("")
def get_all_agents():
    logger.info("GET /agents called")


@router.get("/{id}")
def get_agent_by_id(id: int):
    logger.info("GET /agents/{id} called")


@router.put("/{id}")
def update_agent(id: int):
    logger.info("PUT /agents/{id} called")


@router.put("/{id}/deactivate")
def deactivate_agent(id: int):
    logger.info("PUT /agents/{id}/deactivate called")


@router.get("/{id}/performance")
def get_agent_performance(id: int):
    logger.info("GET /agents/{id}/performance called")