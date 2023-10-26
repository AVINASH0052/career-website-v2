import pymysql.cursors
import pymysql
import os

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db=os.environ['DB_NAME'],
  host=os.environ['DB_HOST'],
  password=os.environ['DB_PASSWORD'],
  read_timeout=timeout,
  port=int(os.environ['DB_PORT']),
  user=os.environ['DB_USER'],
  write_timeout=timeout,
)

def load_jobs_from_db():
  jobs=[]
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    for row in cursor.fetchall():
      jobs.append(row)
  except Exception as e:
        print("An error occurred while loading jobs from the database:", e)
    
  return jobs

def load_job_from_db(id):
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs WHERE id= %s", id)

    rows=cursor.fetchall()
    if len(rows) > 0:
      return rows[0]
    else:
      return None
  
  except Exception as e:
        print("An error occurred while loading jobs from the database:", e)

