def generar_cilindrado(
    diametro_inicial,
    diametro_final,
    longitud,
    rpm,
    avance,
    herramienta="T0101"
):

    return f"""
%
O1000

(GENERADO POR CNC COPILOT)

G21
G18
G40
G99

{herramienta}

G97 S{rpm} M03

G00 X{diametro_inicial + 2} Z2

G01 X{diametro_inicial} Z0 F{avance}

G01 X{diametro_final} Z-{longitud}

G00 X{diametro_final + 5}

M05

M30
%
"""
