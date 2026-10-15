from sqlmodel import Field, Relationship, SQLModel


class Categoria(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, unique=True, max_length=50)

    videojuegos: list["Videojuego"] = Relationship(back_populates="categoria")


class Videojuego(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str = Field(index=True, max_length=100)
    plataforma: str = Field(max_length=50)
    precio: float
    stock: int = 0
    categoria_id: int | None = Field(default=None, foreign_key="categoria.id")

    categoria: Categoria | None = Relationship(back_populates="videojuegos")
