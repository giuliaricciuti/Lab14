import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDStore(self):
        stores = self._model.getAllStores()
        for s in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(text = s.store_name,
                                                                  data = s,
                                                                  on_click = self.readDDStore))
        self._view.update_page()

    def readDDStore(self, e):
        if e.control.data is None:
            self._store = None
        else:
            self._store = e.control.data
            print(self._store)



    def handleCreaGrafo(self, e):
        pass
    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
