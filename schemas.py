from sqlmodel import SQLModel


class CategoriaBase(SQLModel):
    nombre: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(SQLModel):
    nombre: str | None = None


class CategoriaRead(CategoriaBase):
    id: int


class VideojuegoBase(SQLModel):
    titulo: str
    plataforma: str
    precio: float
    stock: int = 0
    categoria_id: int | None = None


class VideojuegoCreate(VideojuegoBase):
    pass


class VideojuegoUpdate(SQLModel):
    titulo: str | None = None
    plataforma: str | None = None
    precio: float | None = None
    stock: int | None = None
    categoria_id: int | None = None


class VideojuegoRead(VideojuegoBase):
    id: int


class VideojuegoReadConCategoria(VideojuegoRead):
    categoria: CategoriaRead | None = None


class CategoriaReadConVideojuegos(CategoriaRead):
    videojuegos: list[VideojuegoRead] = []
