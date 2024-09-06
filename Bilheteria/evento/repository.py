from sqlalchemy.orm import Session

from database import SessionLocal
from evento.model import Evento
from evento.schema import EventoSchema


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def criar_evento(db: Session, evento: EventoSchema):
    if _existe_evento():
        return {'Evento': 'Evento já existe!'}
    _evento = Evento(
                     titulo=evento.titulo,
                     descricao=evento.descricao,
                     duracao=evento.duracao,
                     classificacao=evento.classificacao,
                     horario=evento.horario,
                     data=evento.data,
                     sala=evento.sala,
                     num_lugares=evento.num_lugares
                     )
    try:
        db.add(_evento)
        db.commit()
        db.refresh(_evento)
        return {'Evento': 'Evento criado com sucesso!'}
    except Exception as e:
        db.rollback()
        return {'Evento': f'Erro durante a criação do evento! \n {e}'}


def listar_todos_eventos(db: Session):
    try:
        _evento = db.query(Evento).all()

        if _evento is not None:
            return {'Eventos': _evento}
        else:
            return {'Eventos': 'Nenhum evento encontrado'}

    except Exception as e:
        return {'Eventos': f'Erro durante a busca dos eventos! \n {e}'}


def buscar_evento_por_id(db: Session, id_evento: int):
    try:
        _evento = db.query(Evento).filter(Evento.id == id_evento).first()

        if _evento is not None:
            return {'Evento': _evento}
        else:
            return {'Evento': 'Evento não encontrado'}
    except Exception as e:
        db.rollback()
        return {'Evento': f'Erro durante a busca do evento! \n {e}'}
    finally:
        db.close()


def buscar_evento_por_id_retorna_evento(db: Session, id_evento: int):
    try:
        _evento = db.query(Evento).filter(Evento.id == id_evento).first()

        if _evento is not None:
            return _evento
        else:
            return None
    finally:
        db.close()


def deletar_evento(db: Session, id_evento: int):
    try:
        _evento = db.query(Evento).filter(Evento.id == id_evento).first()

        if _evento is not None:
            db.delete(_evento)
            db.commit()
            return {'Evento': 'Evento apagado com sucesso!'}
        else:
            return {'Evento': 'Evento não encontrado!'}

    except Exception as e:
        db.rollback()
        return {'Eventos': f'Erro durante a exclusão do evento! \n {e}'}


def _existe_evento():
    pass
