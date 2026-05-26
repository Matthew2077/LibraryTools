# REVIEW VERSION 1.0 
LibraryTools is an API-first back-end project designed to manage and structure knowledge, notes, through categories and tags. 

## Feature List:
- Create, edit, read, and delete notes
- Manage note status (draft, published, archived)
- Create, edit, read, and delete categories
- Create, edit, read, and delete tags
- Tags have a many-to-many relationship
- Create, edit, read, and delete users

## Project Architecture:
The project follows a layered architecture to ensure separation of concerns and scalability:
- **API layer**: Fast-API handles routing and request/response validation
- **Service layer**: contains the program logic
- **Repository layer**: manages database interactions
- **Data layer**: SQLAlchemy ORM with relational models

### Tech Stack
**Backend**
- Python 3.11+
- FastAPI**
- Uvicorn (ASGI server)

**Database**
- SQLite → MVP / Development
- PostgreSQL → Production 

**ORM & DB layer**
- SQLAlchemy 2.0*
- Alembic(migrazioni)

**Data validation / schema**
- Pydantic v2 per: request / response models and API & DB schema separation


## Basic Entity Definitions:
### Note:
Notes are the heart of the program; they are composed of text and have relationships with tags, categories, and users. In detail:
- Title: Editable title of the note
- Snail: Derived from the title at the time of creation. It is one of the references for easily obtaining a note.
- Content: Content of the note, text only
- Status: Status of the note, it is an enum: DRAFT, PUBLISHED, ARCHIVED, DELETED
- Author_id: ID of the user who created the user.
- Category_id: ID of the category it belongs to
- tag: Many-to-many relationship with tag

### Categories:
Categories are defined by a name (the actual name of the category) and a label (which further describes it). Categories have a 1-to-N relationship to notes.

### Tags:
Tags are free-form structures used to make notes easier to find and determine their content. Tags have a many-to-many relationship to notes.

### Users
Users have a username and login credentials. In this version, there is no authentication or permission system. The author has a 1-to-N relationship to notes, meaning authors can create many notes.


## Architecture::
```
/librarytools
├── main.py
│
├── api/v1
│ ├── category.py
│ ├── note.py
│ ├── tag.py
│ └── user.py
│
├── core/
│ ├── database.py
│ └── models.py
│
├── repositories/
│ ├── category_repository.py
│ ├── note_repository.py
│ ├── tag_repository.py
│ └── user_repository.py
│
├── schemas/
│ ├── category_schemas.py
│ ├── note_schemas.py
│ ├── tag_schemas.py
│ └── user_schemas.py
│
├── services/
│ ├── category_service.py
│ ├── note_service.py
│ ├── tag_service.py
│ └── user_service.py
│
```


## Endpoints:
|Method|Meaning|Usage|
|---|---|---|
|GET|Read|Display data|
|POST|Create|New resource|
|PUT / PATCH|Modify|Update|
|DELETE|Delete|Clear|

You can see everything at: http://127.0.0.1:8000/docs#/
