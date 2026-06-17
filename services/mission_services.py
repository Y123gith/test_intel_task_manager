from database import db_connection


class AccessTables:
    def __init__(self):
        self.conn = db_connection.get_connect()
        self.cursor = self.conn.cursor()

    
    def rank_fits_mission(self, a_id: int, m_id: int):
        self.cursor.execute("SELECT agent_rank FROM agents WHERE id = %s", (a_id))
        rank = self.cursor.fetchone()
        self.cursor.execute("SELECT risk_level FROM missions WHERE id = %s", (m_id))
        level = self.cursor.fetchone()
        if level == "CRITICAL" and not rank == "Commander":
            raise ValueError("Only commanders can be assigned critical missions")


    def number_of_missions(self, id: int):
        self.cursor.execute("SELECT COUNT(*) FROM missions WHERE assigned_agent_id = %s AND (status = 'ASSIGNED' or status = 'IN_PROGRESS')", (id,))
        number_of_open_missions = self.cursor.fetchone()
        if self.number_of_missions > 2:
            raise ValueError("Agents can only have up to three open missions at once")
        

    def is_agent_active(self, id: int):
        self.cursor.execute("SELECT is_active FROM agents WHERE id = %s", (id,))
        active = self.cursor.fetchone()
        if not active:
            raise ValueError("Only active agents can be assigned missions")



def is_valid_status(status: str):
    user_valid_statuses = ["ASSIGNED", "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED"]
    if status not in user_valid_statuses:
        raise ValueError(f"{status} is not a valid status. It must be only one of the following: ASSIGNED IN_PROGRESS, COMPLETED, FAILED, CANCELLED")



def is_valid_importance_or_difficulty(value1: int, value2: int):
    if not 0 < value1 < 11 or not 0 < value2 < 11 :
        raise ValueError("the level must be between 1 to 10")
    


    