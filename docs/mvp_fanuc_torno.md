# MVP Fanuc Torno

## Configuración General

Unidades:

G21

Plano:

G18

Avance por revolución:

G99

Cancelación compensaciones:

G40

---

## Encendido Husillo

Horario:

M03

Antihorario:

M04

Parada:

M05

---

## Refrigerante

Encendido:

M08

Apagado:

M09

---

## Herramientas

Formato:

T0101

Donde:

01 = posición herramienta

01 = corrector

Ejemplo:

T0202

---

## Ciclo Refrentado

Movimientos:

G00
G01

---

## Ciclo Cilindrado

Movimientos:

G00
G01

---

## Ciclo G71

Formato:

G71 U__ R__

G71 P__ Q__ U__ W__ F__

---

## Ciclo Acabado

G70 P__ Q__

---

## Ciclo Roscado

G76 P__ Q__ R__

G76 X__ Z__ P__ Q__ F__

---

## Fórmula RPM

RPM = (Vc x 1000) / (PI x D)

---

## Fórmula Avance

F = RPM x Fz

---

## Estructura Base de Programa

%

O1000

G21
G18
G40
G99

T0101

M03

(PROCESO)

M30

%
