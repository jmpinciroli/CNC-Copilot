# Generador Cilindrado Fanuc

## Entradas

Diametro Inicial

Diametro Final

Longitud

RPM

Avance

Herramienta

---

## Salida

Programa G-Code Fanuc

---

## Ejemplo

Entrada

Diametro Inicial = 100

Diametro Final = 80

Longitud = 120

RPM = 800

Avance = 0.25

Salida

%

O1000

G21
G18
G40
G99

T0101

G97 S800 M03

G00 X102 Z2

G01 X100 Z0 F0.25

G01 X80 Z-120

M30

%

---

## Reglas

La herramienta debe posicionarse 2 mm fuera de la pieza.

X Seguridad = Diametro Inicial + 2

Z Seguridad = 2
