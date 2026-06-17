from pydantic import BaseModel
import db_connection


class AgentInfo:
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
        query = """INSERT INTO agents (name, specialty, completed_missions, failed_missions, agent_rank)
                   VALUES (%s, %s, %s, %s, %s)
                """
        values = []
        values.append(data.name)
        values.append(data.specialty)
        values.append(data.completed_missions)
        values.append(data.failed_missions)
        values.append(data.agent_rank)
        val
        self.cursor.execute(query, )
        

    
