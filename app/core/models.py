
class Guide(Base): 
    __tablename__ = "Guide"

    NoteID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    GuideURL: Mapped[str] = mapped_column(unique=True)
    Title: Mapped[str]
    Contenuto: Mapped[str]
    Categoria: Mapped[str]
    tags: Mapped[list[str]]
    Stato: Mapped[str]

    # Info Autore
    NomeAutore: Mapped[str]

    # Date Gestite
    DataCreazione: Mapped[datetime]
    DataUltimaModifica: Mapped[datetime]
    DataPubblicazione: Mapped[datetime]

    
    
class Categorie(Base):
    __tablename__ = "Categorie"

    CatID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    CatName: Mapped[str] = mapped_column(unique=True)
    Descrizione: Mapped[Optional[str]]



class Tags(Base):
    __tablename__ = "Tags"

    TagID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    Label: Mapped[str] = mapped_column(unique=True)


class Autore(Base):
    __tablename__ = "Autore"

    AuthorID: Mapped[int] = mapped_column(primary_key=True, unique=True)
    AuthorName: Mapped[str]
    Bio: Mapped[Optional[str]]

    def __repr__(self) -> str: #rappresentazione
        return f"<user(AuthorID={self.AuthorID}, AuthorName={self.AuthorName}, Bio={self.Bio})"1