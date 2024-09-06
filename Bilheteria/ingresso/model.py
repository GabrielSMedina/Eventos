from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Ingresso(Base):
    __tablename__ = "ingresso"

    id = Column(Integer, primary_key=True, index=True)
    num_pedido = Column(String)

    evento_id = Column(Integer, ForeignKey("evento.id"))

    # Relacionamento com Evento
    evento = relationship("Evento", back_populates="ingressos")
