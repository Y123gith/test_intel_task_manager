# ITELLIGENCE-TASK_MANAGER:
 

## Project Use:
the project is bult to allow the user to handle agents and their missions. 
They will be able to store and view the info about the availabilty of agents, rank and succes rate.
They will also be able to store and view important info about the missions such as the status of the mission, it's assigned agent and risk level.


## Folder and File Structure: 
```
intelligence-task-manager/
|
|--- database/
|    |
|    |--- db_connection.py
|    |--- agent_db.py
|    |--- mission_db.py
|
|--- services/
|    |
|    |--- agent_services.py
|    |--- mission_services.py
|
|--- main.py
|--- README.md
|--- requirements.txt
|--- .gitignore
```

## Table Structure:
### agents:
```
id                 | INT PRIMARY KEY AUTO_INCREMENT        | 
name               | VARCHAR(50)                           |
specialty          | VARCHAR(150)                          |
is_active          | BOOLEAN DEFAULT True                  |
completed_missions | INT DEFAULT 0                         |
failed_missions    | INT DEFAULT 0                         |
agent_rank         | ENUM('Junior', 'Senior', 'Commander') |
```
### missions:
```
id                | INT PRIMARY KEY AUTO_INCREMENT |
title             | VARCHAR(100)                   |
description       | TEXT(5000)                     |
location          | VARCHAR(150)                   |
difficulty        | INT                            | *between 1-10 only
importance        | INT                            | *between 1-10 only
status            | VARCHAR(25) DEAFULT 'NEW'      |
risk_level        | VARCHAR(10)                    | *input automatic only
assigned_agent_id | INT DEFAULT NULL               |
```

## Explaination on the different 'classes':
### DBConnection:
The class is responsable for:
1) getting the connection between the mysql container using the 'get_connection()' method
2) creating the database using the 'create_database()' method
3) creating the tables (agents and soldiers) using the 'create_tables()' method

### AgentDB:
The class is responsable for:
1) creating (and returning) a new agent using the 'create_agent(data)' method
2) returning a list of all the agents using the 'get_all_agents()' method
3) returning an agent by id (or None if nonexistant) using the 'get_agent_by_id(id)' method
4) updating the agents data (except the id) using the 'update_agent(id, data)' method
5) sets an agent by is as 'not active' using the 'deactivate_agent(id)' method
6) adds the number of missions that were succesfully completed by the agent using the 'increment_completed(id)' method
7) adds the number of missions that failed by the agent using the 'increment_completed(id)' method
8) returning a dictioanry with the following info A. number of completed missions, B. number of failed missions, C. total number of missions, D. succes rate
9) returning the number of active agents

### MissionDB:
The class is responsable for:
1) creating (and returning) a new mission using the 'create_mission(data)' method
2) returning all the missions using the 'get_all_missions()' method
3) returning the mission (or None if nonexistsant) by the mission's id using the 'get_mission_by_id(id)' method
4) assigning a mission to an agent using the 'assign_mission(m_id, a_id)' method
5) updating a mission's status using the 'update_mission_status(id, status)' method
6) returning the mission's that were assinged but not yet completed by an agent using the 'get_open_missions_by_agent(id)' method
7) countins the total number of mission
8) counts the total number of incomplete missions
9) counts the total number of "CRITICAL" level missions
10) returning the agent with highest number of completed (successfully) missions


## System Rules:
1) an agent's 'rank' must be either 'Junior', 'Senior' or 'Commander' any other rank will get an error
2) the difficulty and importance level must be between 1 to 10 otherwise there an error will be raised
3) the user does not sent the 'risk level'. Instead it is calculated by the program
4) an agent who 'is_active=False' cannot be assigned any missions
5) an agent cannot have more then three missions which are either 'ASSIGNED' or 'IN_PROGRESS' simeltanously
6) only agent of the 'rank' 'commander' can get 'critical' missions
7) a mission can be assinged only when in the status 'NEW'. After being assigned it will be updated to 'ASSIGNED' status
8) a mission may be started when in stage 'ASSIGNED' after the mission starts it will be updated to 'IN_PROGRESS'
9) a mission can be completed only from the 'IN_PROGRESS' status the it will updated to either 'failed' or 'completed' 
10) a mission can be cancelled only when in status of 'NEW' or 'ASSIGNED' otherwise it will raise an error


## Getting the system started:
1) docker run --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 -d mysql:8.
2) python -m venv venv
3) source venv/Scripts/activate
4) pip install -r requirements.txt
5) python main.py