# Base de Datos V1 - CNC Copilot

# Usuarios

## usuarios

| Campo | Tipo |
|---------|---------|
| id | UUID |
| nombre | VARCHAR |
| email | VARCHAR |
| password | VARCHAR |
| fecha_creacion | DATETIME |

---

# Máquinas

## maquinas

| Campo | Tipo |
|---------|---------|
| id | UUID |
| nombre | VARCHAR |
| tipo | VARCHAR |

Ejemplo:

- Torno Leadwell
- Haas ST20
- Haas VF2
- Mazak QT200

---

# Controles CNC

## controles

| Campo | Tipo |
|---------|---------|
| id | UUID |
| nombre | VARCHAR |
| fabricante | VARCHAR |

Ejemplo:

- Fanuc
- Haas
- Siemens
- Fagor
- Heidenhain

---

# Materiales

## materiales

| Campo | Tipo |
|---------|---------|
| id | UUID |
| codigo | VARCHAR |
| descripcion | VARCHAR |
| vc_torneado | DECIMAL |
| vc_fresado | DECIMAL |

Ejemplo:

SAE1045

Vc Torneado = 180

Vc Fresado = 150

---

# Herramientas

## herramientas

| Campo | Tipo |
|---------|---------|
| id | UUID |
| codigo | VARCHAR |
| descripcion | VARCHAR |
| tipo | VARCHAR |
| diametro | DECIMAL |
| radio | DECIMAL |
| fabricante | VARCHAR |
| vc_recomendada | DECIMAL |
| avance_recomendado | DECIMAL |

---

# Operaciones

## operaciones

| Campo | Tipo |
|---------|---------|
| id | UUID |
| nombre | VARCHAR |
| maquina | VARCHAR |

Ejemplo:

- Refrentado
- Cilindrado
- Ranurado
- Tronzado
- G71
- G76
- Planeado
- Taladrado

---

# Programas CNC

## programas

| Campo | Tipo |
|---------|---------|
| id | UUID |
| usuario_id | UUID |
| nombre | VARCHAR |
| fecha | DATETIME |
| operacion | VARCHAR |
| codigo_g | TEXT |

---

# Biblioteca de Insertos

## insertos

| Campo | Tipo |
|---------|---------|
| id | UUID |
| codigo_iso | VARCHAR |
| forma | VARCHAR |
| radio_punta | DECIMAL |
| aplicacion | VARCHAR |

Ejemplos:

CNMG120408

DNMG150608

TNMG160404

VNMG160404

---

# Historial

## historial_programas

| Campo | Tipo |
|---------|---------|
| id | UUID |
| programa_id | UUID |
| fecha_modificacion | DATETIME |
| usuario_id | UUID |
