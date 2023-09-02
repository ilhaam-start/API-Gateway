import json
import psycopg2
import json
import pandas as pd
import os
from datetime import datetime
# import requests

def get_connection(database_url, user, password):
    connection_url = f"postgresql+psycopg2://{user}:{password}@{database_url}"
    return connection_url

def lambda_handler(event, context):
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
    
    raw_countries = event['rawQueryString']
    countries = raw_countries[10:].split(',')
    
    all_countries_df = pd.DataFrame(columns=['cnt','avg_education', 'avg_belong','max_belonging', 'min_belonging', 'total_submissions'])
    for database_url in database_urls:
        
        user = os.environ['source_username']
        password = os.environ['source_password']
        connection_url = get_connection(database_url, user, password)
        query = """SELECT 
                        cnt, 
                        AVG(CASE WHEN durecec = 'NA' THEN NULL ELSE durecec::NUMERIC END) AS avg_education,
                        AVG(CASE WHEN belong IS NULL OR belong = 'NA' THEN 0 ELSE belong::numeric END) AS avg_belong,
                        MAX(CASE WHEN belong IS NULL OR belong = 'NA' THEN 0 ELSE belong::numeric END) AS max_belonging,
                        MIN(CASE WHEN belong IS NULL OR belong = 'NA' THEN 0 ELSE belong::numeric END) AS min_belonging,
                        COUNT(id) AS total_submissions
                    FROM responses 
                    GROUP BY cnt"""
        df = pd.read_sql(query, connection_url)
        all_countries_df = pd.concat([all_countries_df, df])
    all_countries_df = all_countries_df.sort_values(by=['total_submissions'], ascending=False)  
    data_list = []
    for row in all_countries_df.iterrows():
        if row[1][0] in countries:
            data_dict = {}
            data_dict['id'] = row[1][0]
            data_dict['data'] = [{
                "x": round(row[1][1],2),
                "y": round(row[1][2], 2),
                "submissions": str(row[1][5])
            }]
            data_list.append(data_dict)
    return {
          "datasets": data_list
        }
