# LibraryTools Extra Infos

## Core Features
- **Notes**
The program's structured entities are notes, which are text documents with a title, body text, and category. Each note has metadata that determines its identity, status, and visibility.
Data about the note's author will also be included. Finally, it's possible to attach tags to the note that describe its content to improve internal note searches.

- **Categories**
Categories are structures characterized by a specific name and designed to group similar notes in one place.
You can search for desired notes by category.

- **Tags**
Tags are free structures that serve to make notes easier to find. They serve to indicate the type of content contained in the note. Tags are created by the note authors themselves.

- **Users**:
A user can create, edit, and manage their own Notes. The system provides user roles with different permissions (Admin, Moderator, User).
In the current version, user access is available but very simple; authentication and security will be improved in future versions. This version is not intended for the public.
It will be possible to view notes even without registering.

- **Editor**:
The system supports content in Markdown format, allowing for a structured and interoperable representation across different interfaces.

- **Search**:
The internal search allows you to find content and notes by title, tags, and categories. Filters for advanced searches will be added later.

## Basic Entities:
### Notes:
Notes are the heart of the program; all other basic entities converge here. Simply put, a note is a text document with three main characteristics: a title, content (which may also include images and links, but is primarily text), and a category. To these three, NoteSlug is added to ensure you don't lose access to notes just by changing the title (even by a single letter), and the Status, i.e., whether the note is a draft, published, or archived.
Each note will also have a creation date, last modification date, and publication date.

#### Basic Features;
- **NoteID**: A unique numeric code that identifies the note. Characteristics: unique, numeric, auto-incrementing.
- **NoteSlug**: Name, text string, that uniquely refers to a note. In technical jargon, it's called a slug;
- **Title**: Text string that serves as the title of the note.
- **Body**: Material that makes up the note itself, text, URLs, images, etc.;
- **State**: Definition of the note; the status affects permissions for editing, viewing, etc. It can be: draft, published, archived;
- **DateCreation**: Indicates the date the note was created.
- **DateLastEdit: Useful for versioning.
- **DatePublish**: When it was published.

#### foreign keys;
- **CategoryID**: Category to which it belongs, mandatory. Linked to the CatID of the Category table.
- **AuthorID**: Name of the person who wrote the note. Linked to the UserID of the User table.
- **Tags**: Must have at least 3 tags associated with it;

### Category:
Categories are structures characterized by a specific name with the purpose of grouping notes with similar content in one place.

#### Basic Features;
- **CatID**: Unique numeric code that identifies the category. Characteristics: unique, numeric, auto-incrementing.
- **CatName**: Name of the category; this may change over time. Example: Fantasy stories, cooking Notes, Rise of Kingdoms Notes, etc.
- **Description**: Description of the category, specifying what the category should contain and what it does not.

### Tags
Tags are free structures that serve to make notes easier to find. They serve to indicate the type of content contained in the note. Tags are created by the authors of the notes themselves as they wish.

#### Basic Features;
- **TagID:** Unique numeric code that identifies the tag;
- **Label**: Name displayed to users. Example: Python, RoK, History, Fantasy;

### User:
The user is the person using the application. Depending on their permissions, they can perform various actions, from creating and archiving notes, to sharing and viewing.

NB: There will be no authentication in MVPv1.

### Relations:
```
User 1 ──── N Note
Category 1 ─ N Note
Note N ──── N Tag
Note 1 ──── N Reference
Note N ──── N Note
```

## Architecture:
The project is structured to separate tasks in a modular way, thus allowing for greater scalability over time. Below, I summarize the key characteristics of each file and folder.

### Folder characteristics:
api/
Under construction. I'll place the fast-api endpoints in this folder.

core/
Folder containing the files that form the heart of the application; this folder contains the table models and DB initialization.

repositories/
Database operations, all queries, are used by services.

schemas/
In this folder, I'll place the Pydantic classes used to validate incoming and outgoing data. Each basic entity has its own file containing different Pydantic classes depending on the operation performed.

services/
Under construction. All the actual program operations will be contained here.

### Characteristics of each file and the work performed:
main.py
File that manages the app's initialization

core/database.py
This file contains the SQLalchemy database engine, the Base declaration (required for tables in models), and the get_db() function used to call the database in the program. Session management is also present here.

core/models.py
This file declares the main tables used in the system using SQLalchemy syntax: Notes, Tags, Categories, and Users.

### Architecture Schema
```
/librarytools
├── main.py    
│
├── api/ (routes/)     
│   ├── notes.py        
│   └── categories.py  
│
├── core/
│   ├── database.py      
│   └── models.py       
│
├── repositories/
│   ├── note_repository.py
│   └── category_repository.py
│
├── schemas/            
│   ├── category.py
│   ├── note.py
│   ├── tag.py
│   └── user.py
│
├── services/            
│   ├── note_service.py
│   └── cat_service.py
│
```

## APIs - Endpoints (prototype):
*UNDER REVIEW*

|Method|Meaning|Usage|
|---|---|---|
|GET|Read|Display data|
|POST|Create|New resource|
|PUT / PATCH|Modify|Update|
|DELETE|Delete|Clear|

The endpoints can therefore be composed as follows:
/api/APIversion/whatdoIwanttomanipulate/{parameters}

### Endpoints for Notes:
GET /api/v1/notes
POST /api/v1/notes
GET /api/v1/notes/{id}
PATCH /api/v1/notes/{id}
DELETE /api/v1/notes/{id}

### Endpoints for Categories:
GET /api/v1/categories
POST /api/v1/categories
GET /api/v1/categories/{id}
PATCH /api/v1/categories/{id}
DELETE /api/v1/categories/{id}
GET /api/v1/categories/{id}/notes

### Endpoints for TAGs:
GET /api/v1/tags
GET /api/v1/tags/{id}
GET /api/v1/tags/{id}/notes

**Example:**
`/api/v1/notes/{id}`
