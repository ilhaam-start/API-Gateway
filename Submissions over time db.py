import psycopg2
import json
import pandas as pd
import os
from datetime import datetime

def get_connection(database_url, user, password):
    connection_url = f"postgresql+psycopg2://{user}:{password}@{database_url}"
    return connection_url

def get_data():
    # List of database connection URLs
    database_urls = [
        "seta-alb.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/alb",
        "seta-arg.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/arg",
        "seta-aus.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/aus",
        "seta-aut.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/aut",
        "seta-bel.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/bel",
        "seta-bgr.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/bgr",
        "seta-bih.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/bih",
        "seta-blr.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/blr",
        "seta-bra.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/bra",
        "seta-brn.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/brn",
        "seta-can.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/can",
        "seta-che.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/che",
        "seta-chl.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/chl",
        "seta-col.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/col",
        "seta-cri.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/cri",
        "seta-cze.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/cze",
        "seta-deu.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/deu",
        "seta-dnk.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/dnk",
        "seta-dom.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/dom",
        "seta-esp.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com:5432/esp"
    ]
    total_count = 0
    for database_url in database_urls:
        user = os.environ['source_username']
        password = os.environ['source_password']
        connection_url = get_connection(database_url, user, password)
        df = pd.DataFrame()
        df["count"] = (pd.read_sql("SELECT count(id) FROM responses", connection_url))
        # Fetch the count and add it to the total count
        count = df["count"].iloc[0]
        total_count += count
    total_count = total_count
    return total_count

def lambda_handler(event, context):
    total_count = int(get_data())
    time = str(datetime.now())
    user = os.environ['dest_username']
    password = os.environ['dest_password']
    with psycopg2.connect( \
            host = 'analyticaldb-3.cfmnnswnfhpn.eu-west-2.rds.amazonaws.com', \
            user = user, \
            password = password, \
            dbname = 'analyticaldb') \
            as conn:
                with conn.cursor() as cur:
                    get_query = 'SELECT "Total_count" FROM submissions ORDER BY "Time_submitted" DESC LIMIT 1;'
                    cur.execute(get_query)
                    try: 
                        prev_count = cur.fetchall()[0][0]
                        hourly_submissions = total_count - int(prev_count)
                    except:
                        hourly_submissions = None
                    insert_query = 'INSERT INTO submissions ("Time_submitted", "Total_count", "Submissions_per_hour") VALUES (%s,%s,%s);'
                    cur.execute(insert_query, [time, total_count, hourly_submissions])
                    conn.commit()
