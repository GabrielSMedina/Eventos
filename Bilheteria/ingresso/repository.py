import random
import string

from sqlalchemy.orm import Session

from database import SessionLocal
from evento.repository import buscar_evento_por_id_retorna_evento
from ingresso.model import Ingresso


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def comprar_ingresso(db: Session, id_evento: int):
    # Busca o evento pelo ID
    evento = buscar_evento_por_id_retorna_evento(db, id_evento)

    # Verifica se o evento existe
    if not evento:
        return {'Ingresso': 'Evento não encontrado!'}

    # Cria o ingresso
    _ingresso = Ingresso(
        num_pedido=_gerar_numero_pedido(),
        evento_id=evento.id
    )

    try:
        db.add(_ingresso)
        db.commit()
        db.refresh(_ingresso)
        return {'Ingresso': 'Ingresso comprado com sucesso!'}
    except Exception as e:
        db.rollback()  # Faz rollback para evitar problemas no banco de dados
        return {'Ingresso': f'Erro durante a compra do ingresso! \n {e}'}


def listar_ingressos_comprados(db: Session):
    try:
        _ingresso = db.query(Ingresso).all()
        if _ingresso is not None:
            return {'Ingresso': _ingresso}
        else:
            return {'Ingresso': 'Nenhum ingresso encontrado'}

    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a busca dos ingressos! \n {e}'}


def buscar_ingresso_por_id(db: Session, id_ingresso: int):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.num_pedido == id_ingresso).first()
        if _ingresso is not None:
            return {'Ingresso': _ingresso}
        else:
            return {'Ingresso': 'Ingresso não encontrado'}
    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a busca do ingresso! \n {e}'}
    finally:
        db.close()


def devolver_ingresso_por_id(db: Session, id_ingresso: int):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.id == id_ingresso).first()
        if _ingresso is not None:
            db.delete(_ingresso)
            db.commit()
            return {'Ingresso': 'Ingresso apagado com sucesso!'}
        else:
            return {'Ingresso': 'Ingresso não encontrado!'}

    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a exclusão do ingresso! \n {e}'}


def devolver_ingresso_por_num_pedido(db: Session, num_pedido: str):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.num_pedido == num_pedido).first()
        if _ingresso is not None:
            db.delete(_ingresso)
            db.commit()
            return {'Ingresso': 'Ingresso apagado com sucesso!'}
        else:
            return {'Ingresso': 'Ingresso não encontrado!'}

    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a exclusão do ingresso! \n {e}'}


def _gerar_numero_pedido():
    # Gera dois números aleatórios
    _numero = ''.join(random.choices(string.digits, k=2))

    # Gera dois caracteres aleatórios]
    _caracteres = ''.join(random.choices(string.ascii_uppercase, k=2))

    # Concatena os números e os caracteres
    _codigo = _numero + _caracteres

    return _codigo
