import requests


class ClassGetRecord:
    """Clase para obtener datos del servidor."""

    def _init_(self):
        self.__url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def obtener_ultimo_registro(self):
        """Obtiene el último registro de la API."""
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            if data:
                return data[-1]  # Devuelve el último registro
            else:
                return None
        except Exception as e:
            raise Exception(f"Error al obtener registros: {e}")