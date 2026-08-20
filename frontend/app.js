async function generarCodigo() {

    const material = document.getElementById("material").value;

    const herramienta = document.getElementById("herramienta").value;

    const diametroInicial =
        Number(document.getElementById("diametroInicial").value);

    const diametroFinal =
        Number(document.getElementById("diametroFinal").value);

    const longitud =
        Number(document.getElementById("longitud").value);

    const profundidadPasada =
        Number(document.getElementById("profundidadPasada").value);

    const sobremetal =
        Number(document.getElementById("sobremetal").value);

    const datos = {
        material: material,
        herramienta: herramienta,
        diametro_inicial: diametroInicial,
        diametro_final: diametroFinal,
        longitud: longitud,
        profundidad_pasada: profundidadPasada,
        sobremetal: sobremetal,
    };

    try {

        let apiBase;

        if (window.location.port === "8000") {
            apiBase = window.location.origin;
        } else if (window.location.hostname.endsWith(".app.github.dev")) {
            const apiHostname = window.location.hostname.replace(
                /-\d+(?=\.app\.github\.dev$)/,
                "-8000"
            );
            apiBase = `${window.location.protocol}//${apiHostname}`;
        } else {
            apiBase = `${window.location.protocol}//${window.location.hostname || "localhost"}:8000`;
        }

        const respuesta = await fetch(
            `${apiBase}/generar/cilindrado-auto`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(datos)
            }
        );

        if (!respuesta.ok) {
            throw new Error(`API error ${respuesta.status}`);
        }

        const resultado = await respuesta.json();

        document.getElementById("datosProceso").innerHTML =
        `
        <p><strong>Vc:</strong> ${resultado.vc}</p>
        <p><strong>RPM:</strong> ${resultado.rpm}</p>
        <p><strong>Avance:</strong> ${resultado.avance}</p>
        <p><strong>Profundidad de pasada:</strong> ${resultado.profundidad_pasada}</p>
        <p><strong>Pasadas de desbaste:</strong> ${resultado.cantidad_pasadas_desbaste}</p>
        <p><strong>Pasadas totales:</strong> ${resultado.cantidad_pasadas_total}</p>
        `;

        document.getElementById("codigo").textContent =
            resultado.codigo_g;

    } catch (error) {

        document.getElementById("codigo").textContent =
            `Error conectando con la API: ${error.message}`;

        console.error(error);
    }
}
