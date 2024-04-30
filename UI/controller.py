import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def get_corsii(self):
        results=self._model.get_corsii()
        return results


    def handle_iscritti_corso(self,e):
        self._view.txt_result.controls.clear()
        if self._view.dd_corsi.value is None:
            self._view.create_alert("Non è stato selezionato nessun corso!")
        else:
            parole=self._view.dd_corsi.value.split("(")
            codice=parole[1].strip(")")

            results=self._model.cerca_iscritti_corsoo(codice)

            for studente in results:
                self._view.txt_result.controls.append(ft.Text(studente.__str__()))
            self._view.update_page()

    def handle_cerca_studente(self,e): #1 prendo la matricola e mi dà i corsi a cui è iscritta

        if self._view.txt_matricola.value == "":
            self._view.create_alert("Non è stata inserita alcuna matricola")
        else:
            #3 qua richiamo la funzione del model che richiama il DAO
            matricola=int(self._view.txt_matricola.value)
            results=self._model.cerca_studentee(matricola)
            if len(results)==0:
                self._view.create_alert("Non esiste questo studente")
            else:
                studente=results[0]


                self._view.txt_nome.value=studente.nome
                self._view.txt_cognome.value=studente.cognome
                self._view.update_page()
    def handle_corsi_studente(self,e):
        self._view.txt_result.controls.clear()
        if self._view.txt_matricola.value == "":

            self._view.create_alert("Non è stata inserita alcuna matricola")
        else:
            matricola = int(self._view.txt_matricola.value)
            results=self._model.corsi_studentee(matricola)
            if len(results)==0:
                self._view.create_alert("Non esiste questo studente")
            for corso in results:
                self._view.txt_result.controls.append(ft.Text(corso.__str__()))
            self._view.update_page()


