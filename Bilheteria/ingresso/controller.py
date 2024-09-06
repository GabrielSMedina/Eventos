from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ingresso.repository import get_db, listar_ingressos_comprados, buscar_ingresso_por_id, comprar_ingresso, \
    devolver_ingresso_por_id, devolver_ingresso_por_num_pedido

ingresso_router = APIRouter(prefix="/ingresso")


@ingresso_router.get('/',
                     summary='Listar Todos os Ingressos',
                     description='Esta rota é responsavel por listar todos os ingressos',
                     tags=['Ingresso'])
def get_todos_ingressos_comprados(db: Session = Depends(get_db)):
    response = listar_ingressos_comprados(db)

    return response


@ingresso_router.get('/{id_ingresso}',
                     summary='Buscar Ingresso Por Id',
                     description='Esta rota é responsavel por listar ingressos com base em seus IDs',
                     tags=['Ingresso'])
def get_ingresso_por_id(id_ingresso: int, db: Session = Depends(get_db)):
    response = buscar_ingresso_por_id(db, id_ingresso)

    return response


@ingresso_router.post('/',
                      summary='Comprar Ingresso',
                      description='Esta rota é responsavel por comprar ingressos, sendo necessário o envio do ID do '
                                  'evento desejado',
                      tags=['Ingresso'])
def post_ingresso(id_evento: int, db: Session = Depends(get_db)):
    response = comprar_ingresso(db, id_evento)

    return response


@ingresso_router.delete('/{id}',
                        summary='Devolver Ingresso Usando Id',
                        description='Esta rota é responsavel pela devolução de ingressos com base no ID',
                        tags=['Ingresso'])
def delete_ingresso_por_id(id_evento: int, db: Session = Depends(get_db)):
    response = devolver_ingresso_por_id(db, id_evento)

    return response


@ingresso_router.delete('/',
                        summary='Devolver Ingresso Usando Numero de pedido',
                        description='Esta rota é responsavel pela devolução de ingressos com base no numero do pedido',
                        tags=['Ingresso'])
def delete_ingresso_por_num_pedido(nume_pedido: str, db: Session = Depends(get_db)):
    response = devolver_ingresso_por_num_pedido(db, nume_pedido)

    return response
