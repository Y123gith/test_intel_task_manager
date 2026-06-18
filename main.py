import uvicorn
import logging
from database import db_connection

ar = db_connection.DBConnection()
ar.create_tables()

from routes import agent_routes, mission_routes, report_routes
from fastapi import FastAPI


LOG_FILE = 'logs/app.log'
logging.basicConfig(level=logging.INFO, filename=LOG_FILE, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()


app.include_router(agent_routes.router, prefix="/agents", tags=["agents"])
app.include_router(mission_routes.router, prefix="/missions", tags=["missions"])
app.include_router(report_routes.router, prefix="/reports", tags=["reports"])


if __name__ == "__main__":
    uvicorn.run("main:app",host='localhost', port=8000, reload=True)