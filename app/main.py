from typing import Union
import uvicorn
from fastapi import FastAPI

from database import Database

db = Database()

app = FastAPI()

@app.get("/")
def read_root(): 
    try:
      conn = db.get_connection()

      cursor = conn.cursor()

      x1 = hasattr(cursor, "execute")
      print(x1)
      x2 = cursor.execute is not None
      print(x2)
      
      cursor.execute("select id from app where status = 1 and id = %s;", ("aee57b51-1a05-485c-9ae0-aac843e11325",))
      app = cursor.fetchone()
      print("app")
      print(app)
      return app
    except Exception as error:
      print('Something went wrong', error)
      db.rollback(conn)
      return "error"
    finally:
      print('The try except is finished')
      db.put_connection(conn)


if __name__=="__main__": 
  uvicorn.run(app, host="0.0.0.0", port=8000)