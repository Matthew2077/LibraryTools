from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base


# Initializazione DB
engine = sa.create_engine('sqlite///memory:', echo=True) # echo per + dettagli
Session = sessionmaker(bind=db) # binda la sessione a questo db
Base = declarative_base() # ?? what is that

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True) # extra info
    username: Mapped[str]
    email: Mapped[str]

    def __repr__(self) -> str: #rappresentazione
        return f"<user(id={self.id}, username={self.username}, email={self.email})"


