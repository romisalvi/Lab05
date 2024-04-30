# Add whatever it is needed to interface with the DB Table corso
import mysql.connector

from database.DB_connect import get_connection
from model.corso import Corso

def get_corsi():
    result = []
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Oceane1+",
        database="iscritticorsi"
    )
    if cnx is None:
        print("Connessione non riuscita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.* 
                   FROM corso c"""
        cursor.execute(query)
        for row in cursor:
            result.append(Corso(row["codins"],
                                row["crediti"],
                                row["nome"],
                                row["pd"]))
        cursor.close()
        cnx.close()

    return result


