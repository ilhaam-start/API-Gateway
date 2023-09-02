import psycopg2
import json
import pandas as pd
import os

def lambda_handler(event, context):
    user = os.environ['username']
    password = os.environ['password']
    host = 'analyticaldb-3.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com'
    dbname = 'analyticaldb'
    with psycopg2.connect(
        host=host,
        database=dbname,
        user=user,
        password=password
    ) as conn:
            with conn.cursor() as cur:
                get_query = 'SELECT "Time_submitted", "Submissions_per_hour" FROM submissions ORDER BY "Time_submitted" DESC LIMIT 12;'
                cur.execute(get_query)
                data = cur.fetchall()
                submission_data = []
                for line in reversed(data):
                    x = line[0][11:16]
                    y = line[1]
                    submission_data.append({"x": x, "y": y})

    return{
  "datasets": [
    {
      "id": "Submissions",
      "data": submission_data
    }
  ]
}
