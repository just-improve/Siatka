import tkinter as tk

from Controller import Controller
from model import Model
from View import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Dinozaury siatki')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)

        controller.create_list_of_players()



if __name__ == '__main__':
    app = App()
    app.mainloop()

#na początku musiałby zczytywać umiejętności z excela do obiektów - to raczej jest możliwe w tych tabelach były by obecności i ewentualnie ilość zapłaconych pieniedzy
#jeśli ja bym wybrał składy i kliknął zapisz obecność to te składy powinny uzupełnić obecność i automatycznie plik z obecnością powinien być nadpisany
#można też wprowadzić entry i jak zaczne wpisywać to wyskoczy jakis gość w nowym oknie i wtedy wyskoczy też tam entry i jak wpiszę kwotę to nadpisze się rubryka w excelu