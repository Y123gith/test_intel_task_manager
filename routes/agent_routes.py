from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import agent_services
import logging


logger = logging.getLogger(__name__)

router = APIRouter()

class AgentInfo(BaseModel):
    name : str | None=None
    specialty : str | None=None
    completed_missions : None | int=0
    failed_missions : None | int=0 
    agent_rank : str



@router.post("")
def create_agent(body: AgentInfo):
    from database import agent_db
    ar = agent_db.AgentDB()
    logger.info("POST /agents called")
    logger.info("POST /accessing the db")
    succesful = ar.create_agent(body)
    if succesful:
        logger.info("POST /agents succeded")
        return "Succes!"
    logger.error("POST /agents failed")
    return "Failed!"
    

@router.get("")
def get_all_agents():
    logger.info("GET /agents called")
    from database import agent_db
    ar = agent_db.AgentDB()
    logger.info("GET /agents calling db")
    result = ar.get_all_agents()
    if not result:
        logger.error("GET /agents call failed")
        return "None"
    logger.info("GET /agents call succeded")
    return result



@router.get("/{id}")
def get_agent_by_id(id: int):
    logger.info("GET /agents/{id} called")
    from database import agent_db
    ar = agent_db.AgentDB()
    logger.info("GET /agents/{id} calling db")
    result = ar.get_agent_by_id(id)
    if not result:
        logger.error("GET /agents/{id} call failed")
        return "None"
    logger.info("GET /agents/{id} call succeded")
    return result


@router.put("/{id}")
def update_agent(id: int, data: dict):
    #### not working sql syntax problem #####
    logger.info("PUT /agents/{id} called")
    from database import agent_db
    ar = agent_db.AgentDB()
    logger.info("PUT /agents/{id} contacting database")
    succesful = ar.update_agent(id, data)
    if not succesful:
        return "Failed to update"
    logger.info("PUT /agents/{id} call succeded")
    return "Successfully Updated Agent"


@router.put("/{id}/deactivate")
def deactivate_agent(id: int):
    logger.info("PUT /agents/{id}/deactivate called")
    from database import agent_db
    ar = agent_db.AgentDB()
    logger.info("PUT /agents/{id}/deactivate contacting database")
    succesful = ar.deactivate_agent(id)
    if not succesful:
        logger.error("PUT /agents/{id}/deactivate call failed")
        return "Failed to deactivate"
    logger.info("PUT /agents/{id}/deactivate call succeded")
    return "Successfully deactivtaed Agent"


@router.get("/{id}/performance")
def get_agent_performance(id: int):
    logger.info("GET /agents/{id}/performance called")
    from database import agent_db
    ar = agent_db.AgentDB()
    logger.info("PUT /agents/{id}/performance contacting database")
    result = ar.get_agent_performance(id)
    if not result:
        logger.error("PUT /agents/{id}/prformance call failed")
        return "Failed to get performance"
    logger.info("PUT /agents/{id}/prformance call succeded")
    return result


