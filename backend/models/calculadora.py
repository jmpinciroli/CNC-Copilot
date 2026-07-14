import math


def calcular_rpm(vc, diametro):
    rpm = (vc * 1000) / (math.pi * diametro)
    return round(rpm)
