from fastapi import FastAPI
from pydantic import BaseModel

from models.calculadora import calcular_rpm
from models.materiales import MATERIALES
from fastapi import FastAPI
from pydantic import BaseModel
from models.herramientas import HERRAMIENTAS

from generators.fanuc.cilindrado import generar_cilindrado
from generators.fanuc.g71 import generar_g71
from generators.fanuc.g76 import generar_g76_metrica_exterior

app = FastAPI(
    title="CNC Copilot API",
    version="0.1.0"
)


class CilindradoRequest(BaseModel):
    diametro_inicial: float
    diametro_final: float
    longitud: float
    rpm: int
    avance: float


class G71Request(BaseModel):
    diametro_inicial: float
    diametro_final: float
    longitud: float
    profundidad: float
    sobrematerial_x: float
    sobrematerial_z: float
    rpm: int
    avance: float


class G76Request(BaseModel):
    diametro: float
    paso: float
    longitud: float
    rpm: int

    
class RPMRequest(BaseModel):
    material: str
    diametro: float
    

class CilindradoAutoRequest(BaseModel):
    material: str
    herramienta: str
    diametro_inicial: float
    diametro_final: float
    longitud: float


@app.get("/")
def home():
    return {
        "app": "CNC Copilot",
        "version": "0.1.0",
        "estado": "online"
    }


@app.post("/generar/cilindrado")
def generar_cilindrado_api(datos: CilindradoRequest):

    codigo = generar_cilindrado(
        diametro_inicial=datos.diametro_inicial,
        diametro_final=datos.diametro_final,
        longitud=datos.longitud,
        rpm=datos.rpm,
        avance=datos.avance
    )

    return {
        "operacion": "cilindrado",
        "codigo_g": codigo
    }


@app.post("/generar/g71")
def generar_g71_api(datos: G71Request):

    codigo = generar_g71(
        diametro_inicial=datos.diametro_inicial,
        diametro_final=datos.diametro_final,
        longitud=datos.longitud,
        profundidad=datos.profundidad,
        sobrematerial_x=datos.sobrematerial_x,
        sobrematerial_z=datos.sobrematerial_z,
        rpm=datos.rpm,
        avance=datos.avance
    )

    return {
        "operacion": "g71",
        "codigo_g": codigo
    }


@app.post("/generar/g76")
def generar_g76_api(datos: G76Request):

    codigo = generar_g76_metrica_exterior(
        diametro=datos.diametro,
        paso=datos.paso,
        longitud=datos.longitud,
        rpm=datos.rpm
    )

    return {
        "operacion": "g76",
        "codigo_g": codigo
    }

    
@app.post("/calcular/rpm")
def calcular_rpm_api(datos: RPMRequest):

    if datos.material not in MATERIALES:
        return {
            "error": "Material no encontrado"
        }

    vc = MATERIALES[datos.material]["vc"]

    rpm = calcular_rpm(
        vc=vc,
        diametro=datos.diametro
    )

    return {
        "material": datos.material,
        "vc": vc,
        "diametro": datos.diametro,
        "rpm": rpm
    }

@app.post("/generar/cilindrado-auto")
def generar_cilindrado_auto(datos: CilindradoAutoRequest):

    if datos.material not in MATERIALES:
        return {
            "error": "Material no encontrado"
        }

    if datos.herramienta not in HERRAMIENTAS:
        return {
            "error": "Herramienta no encontrada"
        }

    vc = MATERIALES[datos.material]["vc"]

    avance = HERRAMIENTAS[datos.herramienta]["avance"]

    rpm = calcular_rpm(
        vc=vc,
        diametro=datos.diametro_inicial
    )

    codigo = generar_cilindrado(
        diametro_inicial=datos.diametro_inicial,
        diametro_final=datos.diametro_final,
        longitud=datos.longitud,
        rpm=rpm,
        avance=avance
    )

    return {
        "material": datos.material,
        "herramienta": datos.herramienta,
        "vc": vc,
        "rpm": rpm,
        "avance": avance,
        "codigo_g": codigo
    }


@app.get("/materiales")
def obtener_materiales():
    return MATERIALES

@app.get("/materiales/{codigo}")
def obtener_material(codigo: str):

    if codigo not in MATERIALES:
        return {
            "error": "Material no encontrado"
        }

    return MATERIALES[codigo]

@app.get("/herramientas")
def obtener_herramientas():
    return HERRAMIENTAS

@app.get("/herramientas/{codigo}")
def obtener_herramienta(codigo: str):

    if codigo not in HERRAMIENTAS:
        return {
            "error": "Herramienta no encontrada"
        }

    return HERRAMIENTAS[codigo]

@app.get("/catalogos")
def obtener_catalogos():
    return {




        "materiales": MATERIALES,
        "herramientas": HERRAMIENTAS
    }

