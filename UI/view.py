import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self.dd_corsi = None
        self.btn_iscritti_corso=None
        self._title = None
        self.txt_result = None
        self.txt_matricola = None
        self.txt_nome= None
        self.txt_cognome = None
        self.btn_corsi_studente=None
        self.btn_cerca_studente=None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("LAB05", color="blue", size=24)
        self._page.controls.append(self._title)
        self.corsi=self._controller.get_corsii()
        self.dropdown_options = [
            ft.dropdown.Option(corso.__str__())
            for corso in self.corsi
        ]

        self.dd_corsi = ft.Dropdown(width=1000,
                                    hint_text="Selezionare un corso dal menu a tendina",
                                    label="Corsi",
                                    options= self.dropdown_options)
        self.btn_iscritti_corso=ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_iscritti_corso)
        self.txt_matricola=ft.TextField(hint_text="Matricola")
        self.txt_nome=ft.TextField(hint_text="Nome", read_only=True)
        self.txt_cognome=ft.TextField(hint_text="Cognome", read_only=True)
        self.btn_cerca_studente=ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cerca_studente)
        self.btn_corsi_studente=ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_corsi_studente)

        row1=ft.Row([self.dd_corsi, self.btn_iscritti_corso], alignment=ft.MainAxisAlignment.CENTER)
        row2=ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        row3=ft.Row([self.btn_cerca_studente,self.btn_corsi_studente],alignment=ft.MainAxisAlignment.CENTER)
        # text field for the name


        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)


        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
