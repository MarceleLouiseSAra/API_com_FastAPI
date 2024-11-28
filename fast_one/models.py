# onde colocamos os modelos de bancos de dados

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import (  # registra metadados
    Mapped,
    mapped_column,
    registry,
)

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:  # objeto python escalar (row no db)
    __tablename__ = 'users'  # nome da tabela no banco de dados
    id: Mapped[int] = mapped_column(
        init=False, primary_key=True
    )  # chave primária: mantém a integridade dos registros
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    # os atributos são as colunas da tabela
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )  # qual foi a última vez que esse usuário foi alterado; init=False: o banco sabe qual o próximo id
