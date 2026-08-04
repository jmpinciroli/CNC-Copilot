def generar_cilindrado(
    diametro_inicial,
    diametro_final,
    longitud,
    rpm,
    avance,
    profundidad_pasada=2.0,
    sobremetal=0.3,
    herramienta="T0101"
):
    pasadas = ""

    diametro_actual = diametro_inicial

    diametro_desbaste = diametro_final + (sobremetal*2)

    pasadas += (
            "(PASADA INICIAL)\n"
            f"G00 X{diametro_inicial:.3f} Z2.000\n"
            f"G01 Z-{longitud:.3f} F{avance}\n"
            f"G00 X{diametro_inicial + 2:.3f}\n"
            f"G00 Z2.000\n\n"
)

    while diametro_actual > diametro_desbaste:

        diametro_actual -= profundidad_pasada * 2

        if diametro_actual < diametro_desbaste:
            diametro_actual = diametro_desbaste

        pasadas += (
            f"(DESBASTE)\n"
            f"G00 X{diametro_actual:.3f} Z2.000\n"
            f"G01 Z-{longitud:.3f} F{avance}\n"
            f"G00 X{diametro_inicial + 2:.3f}\n"
            f"G00 Z2.000\n\n"

        )
    pasadas += (
    "(PASADA DE ACABADO)\n"
    f"G00 X{diametro_final + 1:.3f} Z2.000\n"
    f"G01 X{diametro_final:.3f} F{avance * 0.7:.3f}\n"
    f"G01 Z-{longitud:.3f} F{avance * 0.7:.3f}\n"
)

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

G01 X{diametro_inicial} Z2 F{avance}

{pasadas}

G00 X{diametro_final + 5}

M05

M30
%
"""
