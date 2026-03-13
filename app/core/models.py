from sqlalchemy.orm import Mapped, mapped_column, Session, ForeignKey, Enum, relationship
from datetime import datetime
from typing import Optional, Dict, List

class NoteState(enum.Enum):
    BOZZA = "bozza"
    PUBBLICATO = "pubblicato"
    ARCHIVIATO = "archiviato"
    

class Notes(Base):
    # Info tabella:
    __tablename__ = "Notes"

    NoteID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    NotesURL: Mapped[str] = mapped_column(unique=True, index=True)
    Title: Mapped[str] # forse qui servirebbe tipo un limite di caratteri ;/ 
    Body: Mapped[str]
    State: Mapped[str] = mapped_column(Enum(NoteState), default=NoteState.BOZZA)

    ## Date Gestite
    DateCreation: Mapped[datetime] = mapped_column(datetime.now())
    DateLastEdit: Mapped[datetime] = mapped_column(datetime.now())
    DatePublish: Mapped[datetime] = mapped_column(nullable=True)

    # Foreing keys
    tags: Mapped[List[Tags]] = relationship(
        back_populates="notes"
    )
    Category: Mapped[Categories] = mapped_column(ForeignKey("Categories.CatID"))
    AuthorName: Mapped[str] = mapped_column(ForeignKey("User.UserID"))

    
    
class Categories(Base):
    __tablename__ = "Categories"

    CatID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    CatName: Mapped[str] = mapped_column(unique=True)
    Description: Mapped[Optional[str]]



class Tags(Base):
    __tablename__ = "Tags"

    TagID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    Label: Mapped[str] = mapped_column(unique=True)


class User(Base):
    __tablename__ = "User"

    UserID: Mapped[int] = mapped_column(primary_key=True, unique=True)
    UserName: Mapped[str]
    Email: Mapped[Optional[str]]
    Password: Mapped[Optional[str]] # rivedi dopo

    def __repr__(self) -> str: #rappresentazione
        return f"<user(AuthorID={self.UserID}, AuthorName={self.UserName}"
    









# Tabella di associazione per la relazione Many-to-Many tra Note e Tag
class NoteTag(Base):
    __tablename__ = "note_tags"
    note_id: Mapped[int] = mapped_column(ForeignKey("Notes.NoteID"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("Tags.id"), primary_key=True)

class Notes(Base):
    __tablename__ = "Notes"

    NoteID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    NotesURL: Mapped[str] = mapped_column(String(255), unique=True, index=True) # Lo slug
    Title: Mapped[str] = mapped_column(String(200))
    Body: Mapped[str] = mapped_column(String) # Testo lungo
    State: Mapped[NoteState] = mapped_column(Enum(NoteState), default=NoteState.BOZZA)

    # Date gestite automaticamente
    DateCreation: Mapped[datetime] = mapped_column(server_default=func.now())
    DateLastEdit: Mapped[datetime] = mapped_column(onupdate=func.now(), server_default=func.now())
    DatePublish: Mapped[Optional[datetime]] = mapped_column(nullable=True)

    # Foreign Keys (I collegamenti fisici nel DB)
    category_id: Mapped[int] = mapped_column(ForeignKey("Categories.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))

    # Relationships (Gli oggetti Python per accedere ai dati correlati)
    category: Mapped["Categories"] = relationship(back_populates="notes")
    author: Mapped["Users"] = relationship(back_populates="notes")
    tags: Mapped[List["Tags"]] = relationship(
        secondary="note_tags", # Usa la tabella di mezzo definita sopra
        back_populates="notes"
    )