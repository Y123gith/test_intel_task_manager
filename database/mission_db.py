import database.db_connection as db_conn
from services import mission_services





class MissionDB:
    def __init__(self):
        self.conn = db_conn.get_connect()
        self.cursor = self.conn.cursor()


    # def create_mission(self, data):
    #     mission_services.is_valid_importance_or_difficulty(data.difficulty, data.importance)
    #     query = """"
    #             INSERT INTO missions (title, description, location, difficulty, importance, status, assigned_agent_id)
    #             VALUES (%s, %s, %s, %s ,%s, %s, %s)
    #             """
    #     values = []
    #     if not 0 < data.difficulty < 11 or not 0 < data.importance < 11:
    #         raise ValueError("the diffculty and importance are numbers between 1-10 only")
    #     values.append(data.title)
    #     values.append(data.description)
    #     values.append(data.location)
    #     values.append(data.difficulty)
    #     values.append(data.importance)
    #     values.append(data.status)
    #     values.append(data.assigned_agent_id)
    #     self.cursor.execute(query, values)
    #     self.conn.commit()
    #     succesful = self.cursor.rowcount > 0
    #     if not succesful:
    #         return None
    #     return succesful
    

    def get_all_missions(self):
        self.cursor.execute("SELECT * FROM missions")
        succesful = self.cursor.fetchall()
        if not succesful:
            return []
        return succesful


    def get_mission_by_id(self, id: int):
        self.cursor.execute("SELECT * From missions WHERE id %s", (id,))
        succesful = self.cursor.fetchone()
        if not succesful:
            return None
        return succesful


    def assign_mission(self, m_id: int, a_id: int):
        mission_services.AccessTables.rank_fits_mission(a_id, m_id)
        mission_services.AccessTables.number_of_missions(a_id)
        mission_services.AccessTables.is_agent_active(a_id)
        self.cursor.execute("UPDATE missions SET assigned_agent_id = %s  WHERE id = %s", (a_id, m_id))
        self.conn.commit()
        succesful = self.cursor.rowcount > 0 
        if not succesful:
            return None
        return succesful
    

    def update_mission_status(self, id: int, status: dict):
        mission_services.is_valid_status(status.values())
        # need a method (since i need to read from the table) to make sure the update procces is in the correct order. for example: after NEW it can only be updated to ASSIGNED
        self.cursor.execute("UPDATE missions SET status = %s  WHERE id = %s", (status.values(), id))
        self.conn.commit()
        succesful = self.cursor.rowcount > 0 
        if not succesful:
            return None
        return succesful


    def get_open_missions_by_agent(self, id: int):
        self.cursor.execute("SELECT * FROM missions WHERE (status = 'ASSIGNED' OR status = 'IN_PROGRESS') AND id = %s ",(id,))
        result = self.cursor.fetchall()
        return result
    
    def count_all_missions(self):
        self.cursor.execute("SELECT COUNT(*) FROM missions")
        succesful = self.cursor.fetchone()
        if not succesful:
            return None
        return succesful
    

    def count_by_status(self, status: str):
        self.cursor.execute("SELECT COUNT(*) FROM missions WHERE status = %s", (status,))
        result = self.cursor.fetchall()
        return result
    

    def count_open_missions(self):
        self.cursor.execute("SELECT * FROM missions WHERE (status = 'ASSIGNED' OR status = 'IN_PROGRESS')")
        result = self.cursor.fetchall()
        return result
    

    def count_critical_missions(self):
        self.cursor.execute("SELECT * FROM missions WHERE status = 'CRITICAL'")
        result = self.cursor.fetchall()
        return result


    def get_top_agent(self):
        self.cursor.execute("SELECT MAX(completed_missions) FROM agents")
        succesful = self.cursor.fetchone()
        if not succesful:
            return None
        return succesful

    # helper method
    def get_all_mission_ids(self):
        self.cursor.execute("SELECT id FROM missions")
        succesful = self.cursor.fetchall()
        if not succesful:
            return None
        return succesful


    # helper method
    def calc_risk_level(diff: int, impor: int):
        return (diff * 2) + impor