def generar_g76_metrica_exterior(
    diametro,
    paso,
    longitud,
    rpm=400
):

    altura = 0.61343 * paso

    diametro_final = diametro - (2 * altura)

    profundidad_micras = round(altura * 1000)

    return f"""
%
O1002

(G76 GENERADO POR CNC COPILOT)

G21
G18
G40
G99

T0404

G97 S{rpm} M03

G00 X{diametro + 2} Z2

G76 P020060 Q100 R0

G76 X{diametro_final:.3f} Z-{longitud} P{profundidad_micras} Q400 F{paso}

M05

M30
%
"""

