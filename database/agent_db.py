from pydantic import BaseModel
import db_connection
from services import agent_services


class AgentInfo(BaseModel):
    name : str | None
    specialty : str | None
    completed_missions : int | None
    failed_missions : int | None
    agent_rank : str

class AgentDB(AgentInfo):
    def __init__(self):
        self.conn = db_connection.get_connect()
        self.cursor = self.conn.cursor()

    
    def create_agent(self, data: AgentInfo):
        agent_services.is_valid_rank(data.agent_rank)
        query = """INSERT INTO agents (name, specialty, completed_missions, failed_missions, agent_rank)
                   VALUES (%s, %s, %s, %s, %s)
                """
        values = []
        values.append(data.name)
        values.append(data.specialty)
        values.append(data.completed_missions)
        values.append(data.failed_missions)
        values.append(data.agent_rank)
        self.cursor.execute(query, values)
        self.conn.commit()
        succesful = self.cursor.rowcount > 0
        return succesful
    

    def get_all_agents(self):
        self.cursor.execute("SELECT * FROM agents")
        succesful = self.cursor.fetchall()
        if not succesful:
            return None
        return succesful
    

    def get_agent_by_id(self, id: int):
        self.cursor.execute("SELECT * From agents WHERE id %s", (id,))
        succesful = self.cursor.fetchone()
        if not succesful:
            return None
        return succesful
    

    def update_agent(self, id: int, data: AgentInfo):
        query = "UPDATE agents SET %s WHERE id = %s"
        dict_data = AgentInfo.model_dump(data)
        agent_services.rank_in_update(dict_data)
        keys = [f"{key} = {value}" for key, value in dict_data.items()]
        formated_data = ", ".join(keys)
        self.cursor.execute(query,(formated_data, id))
        self.conn.commit()
        succesful = self.cursor.rowcount > 0
        if not succesful:
            return None
        return succesful
    

    def deactivate_agent(self, id: int):
        self.cursor.execute("UPDATE agents SET is_active = False WHERE id = %s", (id,))
        self.conn.commit()
        succesful = self.cursor.rowcount > 0 
        if not succesful:
            return None
        return succesful
    

    def increment_completed(self, id: int):
        self.cursor.execute("UPDATE agents SET completed_missions = completed_missions + 1  WHERE id = %s", (id,))
        self.conn.commit()
        succesful = self.cursor.rowcount > 0
        if not succesful:
            return None
        return succesful
    

    def increment_failed(self, id: int):
        self.cursor.execute("UPDATE agents SET failed_missions = failed_missions + 1  WHERE id = %s", (id,))
        self.conn.commit()
        succesful = self.cursor.rowcount > 0
        if not succesful:
            return None
        return succesful
    

    def get_agent_performance(self, id: int):
        succeses = self.count_succeses_by_id(id)
        failures = self.count_failures_by_id(id)
        result_dict = {"completed": succeses, "failed": failures, "total": failures + succeses, "succes_rate":(succeses//failures)//100}
        return result_dict


    def count_active_agents(self):
        self.cursor.execute("SELECT COUNT(*) FROM agents WHERE is_active = True")
        result = self.cursor.fetchone()
        return result

    # helper method 
    def count_succeses_by_id(self, id: int):
        self.cursor.execute("SELECT completed_missions FROM agents WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result
        
    # helper method 
    def count_failures_by_id(self, id: int):
        self.cursor.execute("SELECT failed_missions FROM agents WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result
        

    # helper method
    def get_all_agent_ids(self):
        self.cursor.execute("SELECT id FROM agents")
        succesful = self.cursor.fetchall()
        if not succesful:
            return None
        return succesful

ar = AgentDB()
print(ar.get_all_agents())