from sqlmodel import Session, select

from models import Categoria, Videojuego
from schemas import (
    CategoriaCreate,
    CategoriaUpdate,
    VideojuegoCreate,
    VideojuegoUpdate,
)


def listar_categorias(session: Session):
    return session.exec(select(Categoria)).all()


def obtener_categoria(session: Session, categoria_id: int):
    return session.get(Categoria, categoria_id)


def crear_categoria(session: Session, datos: CategoriaCreate):
    categoria = Categoria.model_validate(datos)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def actualizar_categoria(session: Session, categoria_id: int, datos: CategoriaUpdate):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        return None
    categoria.sqlmodel_update(datos.model_dump(exclude_unset=True))
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def eliminar_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        return None
    for juego in categoria.videojuegos:
        juego.categoria_id = None
        session.add(juego)
    session.delete(categoria)
    session.commit()
    return categoria


def listar_videojuegos(session: Session, skip: int = 0, limit: int = 100):
    return session.exec(select(Videojuego).offset(skip).limit(limit)).all()


def obtener_videojuego(session: Session, videojuego_id: int):
    return session.get(Videojuego, videojuego_id)


def crear_videojuego(session: Session, datos: VideojuegoCreate):
    juego = Videojuego.model_validate(datos)
    session.add(juego)
    session.commit()
    session.refresh(juego)
    return juego


def actualizar_videojuego(session: Session, videojuego_id: int, datos: VideojuegoUpdate):
    juego = session.get(Videojuego, videojuego_id)
    if not juego:
        return None
    juego.sqlmodel_update(datos.model_dump(exclude_unset=True))
    session.add(juego)
    session.commit()
    session.refresh(juego)
    return juego


def eliminar_videojuego(session: Session, videojuego_id: int):
    juego = session.get(Videojuego, videojuego_id)
    if not juego:
        return None
    session.delete(juego)
    session.commit()
    return juego
