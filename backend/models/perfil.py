class Perfil:

    def __init__(self):
        self.segmentos = []

    def agregar_linea(self, x, z):
        self.segmentos.append({
            "tipo": "linea",
            "x": x,
            "z": z
        })

    def agregar_radio(self, radio):
        self.segmentos.append({
            "tipo": "radio",
            "r": radio
        })

    def obtener_segmentos(self):
        return self.segmentos
