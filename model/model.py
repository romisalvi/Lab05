from database.corso_DAO import get_corsi
from database.studente_DAO import cerca_studente, corsi_studente,cerca_iscritti_corso
class Model:

    def cerca_studentee(self,matricola):
        return cerca_studente(matricola)
    def corsi_studentee(self,matricola):
        return corsi_studente(matricola)
    def get_corsii(self):
        return get_corsi()
    def cerca_iscritti_corsoo(self,codice):
        return cerca_iscritti_corso(codice)