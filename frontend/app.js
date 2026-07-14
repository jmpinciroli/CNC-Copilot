function generarCodigo(){

    const diametroInicial =
        document.getElementById("diametroInicial").value;

    const diametroFinal =
        document.getElementById("diametroFinal").value;

    const longitud =
        document.getElementById("longitud").value;

    const codigo =
`%
O1000

(GENERADO POR CNC COPILOT)

G21
G18
G40
G99

T0101

G97 S800 M03

G00 X${Number(diametroInicial)+2} Z2

G01 X${diametroInicial} Z0 F0.25

G01 X${diametroFinal} Z-${longitud}

M05

M30
%`;

    document.getElementById("codigo").textContent = codigo;
}
