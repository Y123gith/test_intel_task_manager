from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


def is_valid_rank(rank: str):
    valid_ranks = ["Junior", "Senior", "Commander"]
    if rank not in valid_ranks:
        raise HTTPException(status_code=400, detail="rank must be Junior/Senior/Commander")
    return True
    

def rank_in_update(data: dict):
    if 'rank' in data.keys():
        rank = data.get("rank")
        is_valid_rank(rank)


def get_agent_name() -> str:
    name = input("Please enter the agents speciality if there is. It must not exceed 50 charachters ")
    if len(name) > 50:
        raise HTTPException(status_code=400, detail="the name exceeded 50 charachters")
    return name


def get_agent_speciality() -> str:
    speciality = input("Please enter the agents speciality if there is. It must not exceed 150 charachters ")
    if len(speciality) > 150:
        raise HTTPException(status_code=400, detail="the speciality exceeded 150 charachters")
    return speciality


def get_agent_rank() -> str:
    rank = input("Please type one of the following ranks: Junior, Senior, Commander: ")
    if is_valid_rank(rank):
        return rank