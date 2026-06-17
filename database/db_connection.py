import mysql.connector

def get_connect():
        conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="Intelligence_db"
        )
        return conn

class DBConnection:

    def __init__(self):
        self.conn = get_connect()
        self.cursor = self.conn.cursor()
        
    def get_connection(self):
        return self.conn

    
    def create_database(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db")


    def create_tables(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS missions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100),
                description TEXT(5000),
                location VARCHAR(150),
                difficulty INT,
                importance INT,
                status VARCHAR(25) DEFAULT 'NEW',
                risk_level VARCHAR(10),
                assigned_agent_id INT DEFAULT NULL
                );
            """
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS agents (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                specialty VARCHAR(150),
                is_active BOOLEAN DEFAULT True,
                completed_missions INT DEFAULT 0,
                failed_missions INT DEFAULT 0,
                agent_rank ENUM('Junior', 'Senior', 'Commander')
                );
            """
        )