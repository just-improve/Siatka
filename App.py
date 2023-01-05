import tkinter as tk

from Controller import Controller
from model import Model
from View import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)

        controller.creating_players_from_csv()


if __name__ == '__main__':
    app = App()
    app.mainloop()