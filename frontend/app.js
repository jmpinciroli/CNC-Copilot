function generar() {

    const codigo = `% 
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
`;

    document.getElementById("resultado").textContent = codigo;
}
