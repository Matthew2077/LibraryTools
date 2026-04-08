# LibraryTools
LibraryTools is an API-first back-end project designed to manage and structure knowledge, notes, through categories and tags. 

## Purpose:
First, let me briefly explain why I decided to start this project. I wanted to create something to prove both my hard skills also building something that truly matters, something useful not only for me, but for a for many others. Out there I've experienced many great applications doing exactly what this project is aiming for: allowing people to take and share notes. However, I want to build is an application where you don't need to log in or deal with anything complex. You should be able to just click a button, write, and share.
This is something Telegraph does very well, in my opinion. The problem, however, is that it lacks tools to organize your notes, and you can't search for them within the app. That’s where I come in: LibraryTools will be an application where you can search through everyone’s notes simply by typing a title or using tags.

### Project Architecture:
The project follows a layered architecture to ensure separation of concerns and scalability:
- **API layer**: Fast-API handles routing and request/response validation
- **Service layer**: contains the program logic
- **Repository layer**: manages database interactions
- **Data layer**: SQLAlchemy ORM with relational models

### Core Features:
- CRUD operations for Notes and Categories
- Tag system with many-to-many relationships
- State management (draft, published, archived)
- Basic search (title and tags)
- Structured content using Markdown

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

**Frontend**
- HTML + CSS
- JavaScript vanilla
- fetch API

## Status:
In development – ​​MVP v1 construction

The first release includes:
- Complete CRUD for:
- Notes
- Categories
- Tags
- Relationship system:
- Notes ↔ Tags (many-to-many)
- Notes → Category (one-to-many)
- Guide status management (draft / published / archived)
- Basic search system (title + tag)
- Data persistence via SQLite
- Automatic API documentation (Swagger / OpenAPI)

## Extra Infos in MVPv1.md