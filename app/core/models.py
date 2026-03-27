import enum
from sqlalchemy.orm import Mapped, mapped_column, Enum, relationship
from sqlalchemy import ForeignKey, Enum
from datetime import datetime
from typing import Optional
from core import Base

class NoteState(enum.Enum):
    BOZZA = "bozza"
    PUBBLICATO = "pubblicato"
    ARCHIVIATO = "archiviato"
    
# Praticamente creo un record che e' composto dal noteID in Notes e il tag_ID
class NoteTag(Base):
    __tablename__ = "note_tags"
    note_id: Mapped[int] = mapped_column(ForeignKey("Notes.NoteID"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("Tags.id"), primary_key=True)


class Note(Base):
    # Info tabella:
    __tablename__ = "Notes"

    NoteID: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True, index=True)
    NotesURL: Mapped[str] = mapped_column(unique=True, index=True)
    Title: Mapped[str] = mapped_column(nullable=True, index=True)
    Body: Mapped[str] 
    State: Mapped[NoteState] = mapped_column(Enum(NoteState), default=NoteState.BOZZA)

    ## Date Gestite
    DateCreation: Mapped[datetime] = mapped_column(default=datetime.now)
    DateLastEdit: Mapped[datetime] = mapped_column(default=datetime.now, nullable=True)
    DatePublish: Mapped[datetime] = mapped_column(default=datetime.now, nullable=True)

    # Foreing keys
    CategoryID: Mapped[int] = mapped_column(ForeignKey("Categories.CatID"), index=True)
    
    AuthorID: Mapped[int] = mapped_column(ForeignKey("Users.UserID"))
    author: Mapped["User"] = relationship(back_populates="notes") 
    tags: Mapped[list["Tag"]] = relationship(
        secondary="note_tags",
        back_populates="notes"
    ) # in schemas/note.py i tags sono una lista di int. Quindi passa IDs.


class Category(Base):
    __tablename__ = "Categories"

    CatID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    CatName: Mapped[str] = mapped_column(unique=True)
    Description: Mapped[Optional[str]] = mapped_column(nullable=True)
    notes: Mapped[list["Note"]] = relationship(back_populates="categories")


class Tag(Base):
    __tablename__ = "Tags"

    TagID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Label: Mapped[str] = mapped_column(nullable=False)
    notes: Mapped[list["Note"]] = relationship(
        secondary="note_tags",
        back_populates="tags"
    )

class User(Base):
    __tablename__ = "Users"
    # IL MVP v1 non prevede il deploy pubblico, quindi l'accesso sara' semplice
    UserID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    UserName: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    Email: Mapped[Optional[str]] = mapped_column(nullable=True)
    Password: Mapped[Optional[str]] = mapped_column(nullable=True)
    notes: Mapped[list["Note"]] = relationship(back_populates="author")

    def __repr__(self) -> str: #rappresentazione
        return f"<user(UserID={self.UserID}, UserName={self.UserName}"