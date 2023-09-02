import psycopg2
import json
import pandas as pd
import os


def get_connection(database_url):
    user = os.environ['username']
    password = os.environ['password']
    connection_url = f"postgresql+psycopg2://{user}:{password}@{database_url}"
    return connection_url

def lambda_handler(event, context):
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
    raw_countries = event['rawQueryString']
    countries = raw_countries[10:].split(',')
    data_list = []
    
    for database_url in database_urls:
        connection_url = get_connection(database_url)
        df = pd.read_sql("SELECT cnt, AVG(CAST(tmins AS int)) FROM responses WHERE tmins != 'NA' GROUP BY cnt", connection_url)
        country = df["cnt"].iloc[0]
        hours = int(df["avg"].iloc[0]/60)
        if country in countries:
            data_list.append({"country":country,  "hours":hours})
    return {
  "datasets": data_list
}
