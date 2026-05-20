
import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from datetime import datetime
from typing import Optional, List
from core import Base


class NoteState(enum.Enum): #ex: note_state
    BOZZA = "bozza"
    PUBBLICATO = "pubblicato"
    ARCHIVIATO = "archiviato"
    ELIMINATO = "eliminato"

# Praticamente creo un record che e' composto dal noteID in notes e il tag_ID
class NoteTag(Base):
    __tablename__ = "note_tags"
    note_id: Mapped[int] = mapped_column(ForeignKey("notes.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True) # ex: NoteID
    slug: Mapped[str] = mapped_column(unique=True, index=True) # ex: NoteSlug
    title: Mapped[str] = mapped_column(nullable=False, index=True) #ex: Title
    content: Mapped[str] # ex: Body
    state: Mapped[NoteState] = mapped_column(Enum(NoteState), default=NoteState.BOZZA) #ex: State

    creation_date: Mapped[datetime] = mapped_column(default=datetime.now) #ex: DateCreation
    update_date: Mapped[Optional[datetime]] = mapped_column(default=datetime.now, nullable=True) #ex: DateLastEdit
    publish_date: Mapped[Optional[datetime]] = mapped_column(default=None, nullable=True) #ex: DatePublish

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True) #ex: CategoryID
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id")) #ex: AuthorID

    author: Mapped["User"] = relationship(back_populates="notes") 
    category: Mapped["Category"] = relationship(back_populates="notes") 
    tags: Mapped[List["Tag"]] = relationship(secondary="note_tags", back_populates="notes") 


class Category(Base):
    __tablename__ = "categories" # ex: Categories
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True) # ex: CatID
    name: Mapped[str] = mapped_column(unique=True) # ex: CatName
    label: Mapped[Optional[str]] = mapped_column(nullable=True) # ex: Description

    notes: Mapped[List["Note"]] = relationship(back_populates="category") 


class Tag(Base):
    __tablename__ = "tags" # ex: Tags
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # ex: TagID
    name: Mapped[str] = mapped_column(nullable=False) # ex: Label

    notes: Mapped[List["Note"]] = relationship(secondary="note_tags", back_populates="tags") 


class User(Base):
    __tablename__ = "users" # ex:
    # IL MVP v1 non prevede il deploy pubblico, quindi l'accesso sara' semplice
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # ex: UserID
    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False) # ex: UserName
    email: Mapped[Optional[str]] = mapped_column(nullable=True) # ex: Email
    password: Mapped[Optional[str]] = mapped_column(nullable=True) # ex: Password

    notes: Mapped[List["Note"]] = relationship(back_populates="author")