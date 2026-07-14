POST /generar/cilindrado

Entrada

{
  "material":"SAE1045",
  "herramienta":"CNMG120408",
  "diametro_inicial":100,
  "diametro_final":80,
  "longitud":120
}

Proceso

1. Obtener Vc
2. Calcular RPM
3. Obtener avance recomendado
4. Generar Código G

Salida

{
  "rpm":573,
  "avance":0.25,
  "codigo_g":"..."
}
