# LibraryTools

## Stato del progetto:
Obbiettivo: finire l'MVP, ovvero la versione alpha funzionante del programma. Vedi MVP sotto
Stato: In costruzione
File completati: database.py
Obbiettivo completamento: fine marzo


## Core Features
- **Guide come entità strutturate**
Le note devono avere ID, Titolo e Contenuto. Nei Meta dati aggiungere tutte le informazioni aggiuntive: autore, categoria di appartenenza, data creazione, data ultima modifica, stato, hashtags per la ricerca.
- **Riferimenti interni:**
All'interno della nota deve essere facile aggiungere collegamenti ad altre note per avere interconnessione ad alto livello. Si può anche citare un pezzo di testo proveniente da un altra nota.
Possibiltà di aggiungere collegamenti esterni. 
- **Tags + categorie**
Devono essere creati a livello di sistema delle categorie chiare che definiscano dove le note stanno. Ogni nota deve essere precisamente allineata in una categoria. I tags possono aggiungere sfumature e possono aiutare nella ricerca delle note
- **Editor semplice ma solido**
Aggiungere funzionalità base che possano rendere fluibile il contenuto sia ad autori che lettori. Quindi: grassetto, test sottolineato, corsivo, testo evidenziato, diversi tipi di headers 
- **Libreria con ricerca**
Entrando nel sistema l'utente potrà accedere a una schermata a mo' di libreria in cui può cercare le note che preferisce.
- **Architettura pronta per integrazioni (API / bot)**
Creare endpoints per future integrazioni api e bots

## Entità base:
### Notes:
Le note sono il cuore del programma, qui convergono tutte le altre entità base. La nota è in parole semplici un documento di testo che principalmente 3 caratteristiche: un titolo, un contenuto (che potrà includere anche immagini e collegamenti, ma principalmente si parla di testo) e una categoria. A questi tre si aggiungono NoteURL per non perdere l'accesso alle note solo perchè si cambia titolo (anche di una sola lettera) e lo Stato, ovvero se quella nota è una bozza, pubblicata o archiviata.
Ogni nota avrà anche una data di creazione, di ultima modifica e di pubblicazione.

#### Caratteristiche base; 
- **NoteID**: Codice numerico univoco che identifica la nota. Caratteristiche: univoco, numerico, auto incrementativo. 
- **NoteURL**: Nome, stringa di testo, che si riferisce in modo univoco ad una nota In gergo tenico Slug;
- **Title**: Stringa di testo che fa da titolo della nota. 
- **Body**: materiale che compone la nota stessa, testo, urls, immagini etc;
- **State**: Definizione della nota, lo stato influesce permessi di motifica, visione etc. Esso può essere: bozza, pubblicato, archiviato;
- **DateCreation**: Indica la data di creazione della nota
- **DateLastEdit:** utile per il versioning
- **DatePublish**: Quando è stata pubblicata

#### Caratteristiche aggiuntive (foreing keys); 
- **Category**: Categoria di appartenenza, obbligatoria;
- **Tags**: Deve avere almeno 3 tags ad esso associati;
- **AuthorName**: Nome di chi ha scritto la nota

### Categories:
Le categorie sono strutture caratterizzate da un nome ben preciso con lo scopo di raggruppare in un unico posto note simili in contenuto.

#### Caratteristiche base; 
- **CatID**: Codice numerico univoco che identifica la categoria. aratteristiche: univoco, numerico, auto incrementativo. 
- **CatName**: Nome della categoria, esso può variare nel tempo. Esempio: Storie fantastiche, guide di cucina, guide di Rise of Kingdoms etc
- **Description**: Descrizione della categoria, specifica cosa dovrebbe contenere la categoria e cosa non rientra in essa.

### Tags 
I tags sono strutture libere che servono ad aumentare la facilità di ricerca delle note. Essi hanno la funzione di indicare che tipo di contenuto c'è nella nota. I tag sono creati dagli autori delle note stesse a loro piacimento

#### Caratteristiche base; 
- **TagID:** Codice numerico univoco che identifica il tag;
- **Label**: Nome visualizzato dagli utenti. Esempio: Python, RoK, Storia, Fantasy; 

### User:
L'utente è chi usufrisce dell'applicazione, a seconda dei suoi permessi può performare diverse azioni, dalla creazione all'archivio di note, la condivisione e visualizzazione.

NB: in MVPv1 non ci sarà autenticazione vera e propria


#### Caratteristiche base; 
- **UserID**: Codice numerico univoco che identifica l'utente;
- **UserName:** Stringa di testo che rappresenza il nome dell'utente, sarà visualizato dagli altri utenti nel programma. Il nome utente  è il nome dell'autore di una guida
- **Email:** Email per login
- **Password:** Password per il login


### Relazioni:
User 1 ──── N Note
Category 1 ─ N Note
Note N ──── N Tag
Note 1 ──── N Reference
Note N ──── N Note (via GuideLink)

## STACK:
**Backend**
- Python 3.11+
- FastAPI**
- Uvicorn (ASGI server)

**Database**
- SQLite → MVP / sviluppo
- PostgreSQL → produzione / crescita

**ORM & DB layer**
- SQLAlchemy 2.0*
- Alembic(migrazioni)

**Data validation / schema**
- Pydantic v2 per: request / response models e separazione netta tra API schema e DB schema

**Frontend**
- HTML + CSS
- JavaScript vanilla
- fetch API

## Architettura:
```
/librarytools
├── main.py              # Inizializza l'app e include i router
├── core/
│   ├── database.py      # Engine DB, gestione Session, get_db() func
│   └── models.py        # Classi SQLAlchemy (Guide, Category, Tag, User)
│
├── api/ (routes/)     # endpoints FastAPI
│   ├── notes.py        # @router.post("/notes") -> chiama service
│   └── categories.py    idem
│
├── services/            # Azioni del programma
│   ├── note_service.py # Funzioni come: create_note(), get_all_notes()
│   └── cat_service.py
│
```

## MVPv1:
MVP è la versione base funzionante del programma, ecco un elenco delle funzionalità che dovrebbe avere:
- CRUD Guide (Create, Read, Update, Delete)
- CRUD Category (Create, Read, Update, Delete)
- Tags funzionanti (many-to-many)
- Ricerca base (titolo + tags)
- API documentata via Swagger
- DB persistente (SQLite) 

## APIs - Endpoints:
*IN REVISIONE*

Definiamo come funzionano gli endpoints, ricordati che sono URLs, con HTTP. Qui i metodi HTTP: 

|Metodo|Significato|Uso|
|---|---|---|
|GET|Leggere|Visualizzare dati|
|POST|Creare|Nuova risorsa|
|PUT / PATCH|Modificare|Update|
|DELETE|Eliminare|Cancellare|

Gli endpoints possono essere quindi composti così:

/api/versioneAPI/cosavogliomanipolare/{parametri}

### Endpoints per Notes:
GET    /api/v1/notes
POST   /api/v1/notes
GET    /api/v1/notes/{id}
PATCH  /api/v1/notes/{id}
DELETE /api/v1/notes/{id}

### Endpoints per Categorie:
GET    /api/v1/categories
POST   /api/v1/categories
GET    /api/v1/categories/{id}
PATCH  /api/v1/categories/{id}
DELETE /api/v1/categories/{id}
GET    /api/v1/categories/{id}/notes

### Endpoints per TAGs:
GET /api/v1/tags
GET /api/v1/tags/{id}
GET /api/v1/tags/{id}/notes

**Esempio:**
`/api/v1/notes/{id}`
