
import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from datetime import datetime
from typing import Optional, List
from core import Base


class note_state(enum.Enum):
    BOZZA = "bozza"
    PUBBLICATO = "pubblicato"
    ARCHIVIATO = "archiviato"
    ELIMINATO = "eliminato"

# Praticamente creo un record che e' composto dal noteID in notes e il tag_ID
class NoteTag(Base):
    __tablename__ = "note_tags"
    note_id: Mapped[int] = mapped_column(ForeignKey("notes.NoteID"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("Tags.TagID"), primary_key=True)


class Note(Base):
    __tablename__ = "notes"
    NoteID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    noteslug: Mapped[str] = mapped_column(unique=True, index=True)
    Title: Mapped[Optional[str]] = mapped_column(nullable=True, index=True)
    Body: Mapped[str]
    State: Mapped[note_state] = mapped_column(Enum(note_state), default=note_state.BOZZA)

    DateCreation: Mapped[datetime] = mapped_column(default=datetime.now)
    DateLastEdit: Mapped[Optional[datetime]] = mapped_column(default=datetime.now, nullable=True)
    DatePublish: Mapped[Optional[datetime]] = mapped_column(default=None, nullable=True)

    CategoryID: Mapped[int] = mapped_column(ForeignKey("Categories.CatID"), index=True)
    AuthorID: Mapped[int] = mapped_column(ForeignKey("Users.UserID"))

    author: Mapped["User"] = relationship(back_populates="notes")
    category: Mapped["Category"] = relationship(back_populates="notes")  # ✅ aggiunto
    tags: Mapped[List["Tag"]] = relationship(secondary="note_tags", back_populates="notes")


class Category(Base):
    __tablename__ = "Categories"
    CatID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    CatName: Mapped[str] = mapped_column(unique=True)
    Description: Mapped[Optional[str]] = mapped_column(nullable=True)

    notes: Mapped[List["Note"]] = relationship(back_populates="category")  # ✅ corretto


class Tag(Base):
    __tablename__ = "Tags"
    TagID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Label: Mapped[str] = mapped_column(nullable=False)

    notes: Mapped[List["Note"]] = relationship(secondary="note_tags", back_populates="tags")


class User(Base):
    __tablename__ = "Users"
    # IL MVP v1 non prevede il deploy pubblico, quindi l'accesso sara' semplice
    UserID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    UserName: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    Email: Mapped[Optional[str]] = mapped_column(nullable=True)
    Password: Mapped[Optional[str]] = mapped_column(nullable=True)

    notes: Mapped[List["Note"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"<User(UserID={self.UserID}, UserName={self.UserName})>"
    