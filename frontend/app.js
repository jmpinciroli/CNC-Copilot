async function generarCodigo() {

    const diametroInicial =
        Number(document.getElementById("diametroInicial").value);

    const diametroFinal =
        Number(document.getElementById("diametroFinal").value);

    const longitud =
        Number(document.getElementById("longitud").value);

    const datos = {
        material: "SAE1045",
        herramienta: "CNMG120408",
        diametro_inicial: diametroInicial,
        diametro_final: diametroFinal,
        longitud: longitud
    };

    try {

        const respuesta = await fetch(
    "https://ominous-potato-jrrjpxvj6v7vfq4rq-8000.app.github.dev/generar/cilindrado-auto",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(datos)
    }
    );

        const resultado = await respuesta.json();

        document.getElementById("codigo").textContent =
            resultado.codigo_g;

    } catch (error) {

        document.getElementById("codigo").textContent =
            "Error conectando con la API";

        console.error(error);
    }
}
