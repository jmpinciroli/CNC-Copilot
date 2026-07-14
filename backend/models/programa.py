from pydantic import BaseModel


class ProgramaCilindrado(BaseModel):
    diametro_inicial: float
    diametro_final: float
    longitud: float
    rpm: int
    avance: float
