from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session

import crud
from database import get_session
from schemas import (
    CategoriaCreate,
    CategoriaRead,
    CategoriaReadConVideojuegos,
    CategoriaUpdate,
    VideojuegoCreate,
    VideojuegoRead,
    VideojuegoReadConCategoria,
    VideojuegoUpdate,
)

app = FastAPI(title="Tienda de Videojuegos")


@app.get("/")
def root():
    return {"mensaje": "API de la tienda de videojuegos andando"}


@app.post("/categorias", response_model=CategoriaRead, status_code=201)
def crear_categoria(datos: CategoriaCreate, session: Session = Depends(get_session)):
    return crud.crear_categoria(session, datos)


@app.get("/categorias", response_model=list[CategoriaRead])
def listar_categorias(session: Session = Depends(get_session)):
    return crud.listar_categorias(session)


@app.get("/categorias/{categoria_id}", response_model=CategoriaReadConVideojuegos)
def obtener_categoria(categoria_id: int, session: Session = Depends(get_session)):
    categoria = crud.obtener_categoria(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria


@app.put("/categorias/{categoria_id}", response_model=CategoriaRead)
def actualizar_categoria(categoria_id: int, datos: CategoriaUpdate, session: Session = Depends(get_session)):
    categoria = crud.actualizar_categoria(session, categoria_id, datos)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria


@app.delete("/categorias/{categoria_id}")
def eliminar_categoria(categoria_id: int, session: Session = Depends(get_session)):
    categoria = crud.eliminar_categoria(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return {"mensaje": f"Categoria '{categoria.nombre}' eliminada"}


@app.post("/videojuegos", response_model=VideojuegoReadConCategoria, status_code=201)
def crear_videojuego(datos: VideojuegoCreate, session: Session = Depends(get_session)):
    if datos.categoria_id is not None and not crud.obtener_categoria(session, datos.categoria_id):
        raise HTTPException(status_code=404, detail="La categoria indicada no existe")
    return crud.crear_videojuego(session, datos)


@app.get("/videojuegos", response_model=list[VideojuegoRead])
def listar_videojuegos(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return crud.listar_videojuegos(session, skip, limit)


@app.get("/videojuegos/{videojuego_id}", response_model=VideojuegoReadConCategoria)
def obtener_videojuego(videojuego_id: int, session: Session = Depends(get_session)):
    juego = crud.obtener_videojuego(session, videojuego_id)
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return juego


@app.put("/videojuegos/{videojuego_id}", response_model=VideojuegoReadConCategoria)
def actualizar_videojuego(videojuego_id: int, datos: VideojuegoUpdate, session: Session = Depends(get_session)):
    if datos.categoria_id is not None and not crud.obtener_categoria(session, datos.categoria_id):
        raise HTTPException(status_code=404, detail="La categoria indicada no existe")
    juego = crud.actualizar_videojuego(session, videojuego_id, datos)
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return juego


@app.delete("/videojuegos/{videojuego_id}")
def eliminar_videojuego(videojuego_id: int, session: Session = Depends(get_session)):
    juego = crud.eliminar_videojuego(session, videojuego_id)
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return {"mensaje": f"Videojuego '{juego.titulo}' eliminado"}
