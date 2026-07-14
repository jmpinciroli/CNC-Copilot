# Motor Generador G-Code V1

## Objetivo

Transformar parámetros de mecanizado en programas CNC válidos para cada control.

---

# Flujo General

Usuario

↓

Máquina

↓

Control CNC

↓

Operación

↓

Herramienta

↓

Material

↓

Dimensiones

↓

Generador

↓

Código G

---

# Control Inicial

Fanuc

---

# Operaciones Iniciales

## Refrentado

Parámetros

- Diámetro Inicial
- Posición Z
- RPM
- Avance

Salida

G00
G01
M03
M30

---

## Cilindrado

Parámetros

- Diámetro Inicial
- Diámetro Final
- Longitud
- RPM
- Avance

Salida

G00
G01

---

## Ciclo G71

Parámetros

- Diámetro Inicial
- Perfil
- Profundidad de pasada
- Sobrematerial acabado

Salida

G71
G70

---

## Roscado G76

Parámetros

- Diámetro
- Paso
- Longitud
- Altura de filete

Salida

G76

---

# Fórmulas

## RPM

RPM = (Vc × 1000) / (PI × D)

Donde:

Vc = Velocidad de corte

D = Diámetro

---

## Avance

F = RPM × Fz

---

# Estructura del Programa

%

O1000

G21

G40

G99

T0101

M03

(OPERACION)

M30

%

---
