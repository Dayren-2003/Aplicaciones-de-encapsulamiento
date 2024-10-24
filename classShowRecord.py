import tkinter as tk

class ClassShowRecord:
    """Clase para mostrar los datos en la interfaz gráfica."""

    def _init_(self, master):
        self.__master = master
        self.__resultado_label = tk.Label(master, text="")
        self.__resultado_label.pack()

        self._fetch_button = tk.Button(master, text="Obtener Último Registro", command=self._mostrar_registro)
        self.__fetch_button.pack()

class ShowRecord:
    def __mostrar_registro(self):
        """Muestra el último registro al hacer clic en el botón."""
        try:
            ultimo_registro = self.__record_fetcher.obtener_ultimo_registro()
            if ultimo_registro:
                self.__mostrar_datos(ultimo_registro)
            else:
                self.__resultado_label.config(text="No se encontraron registros.")
        except Exception as e:
            self.__resultado_label.config(text=str(e))

    def __mostrar_datos(self, registro):

        texto = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Calle: {registro['calle']}"
        )
        self.__resultado_label.config(text=texto)