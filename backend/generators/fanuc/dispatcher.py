from generators.fanuc.cilindrado import generar_cilindrado
from generators.fanuc.g71 import generar_g71
from generators.fanuc.g76 import generar_g76_metrica_exterior


def generar_programa(datos):

    operacion = datos["operacion"]

    if operacion == "cilindrado":
        return generar_cilindrado(
            diametro_inicial=datos["diametro_inicial"],
            diametro_final=datos["diametro_final"],
            longitud=datos["longitud"],
            rpm=datos["rpm"],
            avance=datos["avance"]
        )

    if operacion == "g71":
        return generar_g71(
            diametro_inicial=datos["diametro_inicial"],
            diametro_final=datos["diametro_final"],
            longitud=datos["longitud"],
            profundidad=datos["profundidad"],
            sobrematerial_x=datos["sobrematerial_x"],
            sobrematerial_z=datos["sobrematerial_z"],
            rpm=datos["rpm"],
            avance=datos["avance"]
        )

    if operacion == "g76":
        return generar_g76_metrica_exterior(
            diametro=datos["diametro"],
            paso=datos["paso"],
            longitud=datos["longitud"],
            rpm=datos["rpm"]
        )

    raise ValueError("Operacion no soportada")
