from pydantic import BaseModel


class EventoSchema(BaseModel):
    titulo: str
    descricao: str
    duracao: str
    classificacao: str
    horario: str
    data: str
    sala: str
    num_lugares: int
