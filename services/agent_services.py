

def is_valid_rank(rank: str):
    valid_ranks = ["Junior", "Senior", "Commander"]
    if rank not in valid_ranks:
        raise ValueError("rank must be Junior/Senior/Commander")
    
def rank_in_update(data: dict):
    if 'rank' in data.keys():
        rank = data.get("rank")
        is_valid_rank(rank)
