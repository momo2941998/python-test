import asyncio
import time
import psycopg2
import psycopg2.pool
import logging
import sys


logger = logging.getLogger('sLogger')

class Database:
    
    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.init_connection())
    
    @asyncio.coroutine
    def init_connection(self):
        result = 1
        loop_end = time.time() + 10
        while time.time() < loop_end:
            try:
                self.pool = psycopg2.pool.SimpleConnectionPool(1, 200, user = "postgres", password = "123456", host = "10.1.10.192", port = 5432, database = "ott", options= "-c search_path=call_center")
                
                result = 0
                logger.info("Initializing a database connection success")
                break
            except:
                continue
        if result:
            logger.info("Initializing a database connection failed")
            sys.exit()

    def get_connection(self):
        conn = self.pool.getconn()
        print("dddd",conn.autocommit)
        return conn
    
    def put_connection(self, connection):
        if connection:
            self.pool.putconn(connection)
            logger.info("Put Connection")
            
    def commit(self, connection):
        try:
            logger.info("Commit Connection")
            connection.commit()
        except:
            connection.rollback()
    
    def rollback(self, connection):
        if connection:
            logger.info("Rollback Connection")
            connection.rollback()

    def __del__(self):
        if (self.pool):
            self.pool.closeall()
        logger.info("PostgreSQL connection pool is closed")
