# API REST V1

## Materiales

GET /materiales

GET /materiales/{id}

POST /materiales

PUT /materiales/{id}

DELETE /materiales/{id}

---

## Herramientas

GET /herramientas

GET /herramientas/{id}

POST /herramientas

PUT /herramientas/{id}

DELETE /herramientas/{id}

---

## Operaciones

GET /operaciones

---

## Programas

GET /programas

GET /programas/{id}

POST /programas

DELETE /programas/{id}

---

## Generador CNC

POST /generar

Entrada:

{
 "control":"fanuc",
 "operacion":"cilindrado",
 "diametro_inicial":100,
 "diametro_final":80,
 "longitud":120
}

Salida:

{
 "codigo":"..."
}
