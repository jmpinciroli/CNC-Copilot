def generar_perfil(segmentos):

    lineas = []

    n = 100

    for segmento in segmentos:

        if segmento["tipo"] == "linea":

            lineas.append(
                f"N{n} G01 X{segmento['x']} Z{segmento['z']}"
            )

            n += 10

    return "\n".join(lineas)
``
