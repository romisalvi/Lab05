import mysql.connector
import database
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

#1 da qua cerco gli studenti con tale matricola
def cerca_studente(matricola):
    cnx=mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="Oceane1+",
                                database="iscritticorsi"
                                )
    result=[]
    if cnx is None:
        print("Errore connessione")
    else:
        cursor=cnx.cursor(dictionary=True)
        query="""select s.*
                from studente s 
                where S.MATRICOLA=%s"""
        cursor.execute(query,(matricola,))
        for row in cursor:
            result.append(Studente(row["matricola"],
                                                  row["cognome"],
                                                  row["nome"],
                                                  row["CDS"]))
        cursor.close()
        cnx.close()
        return result
def corsi_studente(matricola):
    result=[]
    cnx=mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="Oceane1+",
                                database="iscritticorsi"
                                )
    if cnx is None:
        print("Connessione non riuscita")
    else:
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT c.* 
                FROM iscrizione i 
                JOIN corso c ON c.codins = i.codins
                WHERE i.matricola = %s"""
        cursor.execute(query,(matricola,))
        for row in cursor:
            result.append(Corso(row["codins"],
                                row["crediti"],
                                row["nome"],
                                row["pd"]))
        cursor.close()
        cnx.close()
        return result

def cerca_iscritti_corso(codice):
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
        query = """SELECT s.* 
                        FROM iscrizione i 
                        JOIN studente s ON i.matricola = s.matricola
                        WHERE i.codins = %s"""
        cursor.execute(query, (codice,))
        for row in cursor:
            result.append(Studente(row["matricola"],
                                row["cognome"],
                                row["nome"],
                                row["CDS"]))
        cursor.close()
        cnx.close()
        return result
