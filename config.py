from configparser import ConfigParser
import psycopg2

import os
def get_connection():
    db_config = get_config()
    # conectarse a la base de datos
    db = psycopg2.connect(**db_config) # db connection
    db.autocommit = True
    # crear un cursor object para la ejecucion
    cur = db.cursor()
    return db, cur

def get_config(filename="properties.ini", section="postgresql"):
    """Parses and gets database config from file"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser = ConfigParser()
    parser.read(filename)
    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found".format(section))

    return db_config