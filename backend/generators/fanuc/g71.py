def generar_g71(
    diametro_inicial,
    diametro_final,
    longitud,
    profundidad,
    sobrematerial_x,
    sobrematerial_z,
    rpm,
    avance
):

    return f"""
%
O1001

(G71 GENERADO POR CNC COPILOT)

G21
G18
G40
G99

T0101

G97 S{rpm} M03

G00 X{diametro_inicial + 2} Z2

G71 U{profundidad} R1.0

G71 P100 Q200 U{sobrematerial_x} W{sobrematerial_z} F{avance}

N100
G00 X{diametro_inicial} Z0

G01 X{diametro_final} Z-{longitud}

N200

G70 P100 Q200

M05

M30
%
"""
