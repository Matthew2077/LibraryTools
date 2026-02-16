# LibraryTools

## Stato del progetto:
Il progetto è stato iniziato in data 10 febbraio 2026, è in fase di costruzione iniziale. L'obbiettivo è finire l'MVP, ovvero la versione alpha funzionante del programma.

### Core Features
- **Guide come entità strutturate**
Le guide devono avere ID, Titolo e Contenuto. Nei Meta dati aggiungere tutte le informazioni aggiuntive: autore, categoria di appartenenza, data creazione, data ultima modifica, stato, hashtags per la ricerca.
- **Riferimenti interni:**
All'interno della guida deve essere facile aggiungere collegamenti ad altre guide per avere interconnessione ad alto livello. Si può anche citare un pezzo di testo proveniente da un altra guida.
Possibiltà di aggiungere collegamenti esterni. 
- **Tags + categorie**
Devono essere creati a livello di sistema delle categorie chiare che definiscano dove le guide stanno. Ogni guida deve essere precisamente allineata in una categoria. I tags possono aggiungere sfumature e possono aiutare nella ricerca delle guide
- **Editor semplice ma solido**
Aggiungere funzionalità base che possano rendere fluibile il contenuto sia ad autori che lettori. Quindi: grassetto, test sottolineato, corsivo, testo evidenziato, diversi tipi di headers 
- **Libreria con ricerca**
Entrando nel sistema l'utente potrà accedere a una schermata a mo' di libreria in cui può cercare le guide che preferisce.
- **Architettura pronta per integrazioni (API / bot)**
Creare endpoints per future integrazioni api e bots

### Entità base:
#### Guide:
Le guide sono il cuore del sistema, essi hanno tre caratteristiche specifiche:
- **ID (NoteID)**: univoco, numerico, auto increment (parte da 100000). Le note con ID < di 1000000 sono note di sistema o usate per altri scopi
- **Titolo**: Non deve essere univoco, deve essere maggiore di 3 lettere con un massimo di 50/70. 
- **Contenuto**: Testo, collegamenti intermi, collegamenti esterni
- **Categoria**: Deve appartenere ad una categoria. 

**Altri Contenuti:**
- **tags**: Nei meta data possono essere aggiunti dei tags che aiutano l'utente nella ricerca dei contenuti. Questi tag dovrebbero descrivere il contenuto. La funzione dei tag è quindi una funzione prettamente di supporto nella ricerca, non di categorizzazione e quindi di strutturazione.
- **Autore**: Definire chi ha scritto la guida
- **DataCreazione**: Indica la data di creazione della guida
- **Data dell'utima modifica:** utile per il versioning
- **Stato**: può essere bozza, pubblicato, archiviato (nota: capire come gestire le modifiche);

#### Categorie:
Le categorie sono insiemi di guide che condividono uno stesso tema o argomento. Ogni categoria deve avere:
- **ID (CatID):** univoco, numerico (parte da 1000 fino a 9999)
- **Nome**: Identificativo che sarà usato nel sistema per riconoscere e usare la categoria. Deve essere univoco
- **Parentele**: una categoria può stare da sola, ma per maggiore chiarezza è bene creare un sistema complesso di categorie che migliorare l'organizzazione delle guide nel sistema. 
- **Descrizione**: Cosa rientra in questa categoria, regole e definizione. 

#### Tags 
I tags sono strutture libere che servono ad aumentare la facilità di ricerca delle guide. Essi possono essere aggiunti dall'autore nel header della guida, non sono  case sensitive (così riduco ridondanza e riduce ambiguità). I tags sono liberi, possono essere creati dagli autori stessi nella loro aggiunta, pertanto nessuno possiede un tag, i tag esistono finché c'è qualcuno che lo usa. 

I tags possono essere visti in una visualizzazione specifica che permette di vedere tutti i tags esistenti, quali note sono legate ad esse ed esplorare. 

Ogni tag deve avere:
- **ID (tagID):** univoco, numerico, auto incrementale (parte da 1);
- **label**: Deve avere un nome che lo identifica, come "python", "RoK" etc

#### Autore:
L'autore è colui che scrive le guide, le può modificare, eliminare, archiviare etc. **Caratteristiche dell'autore:**
- **ID (AuthorID):** univoco, numerico (parte da 10000 fino a 99999)
- **Nome:** Deve essere univoco, sarà usato nel sistema per riferisi a quell'autore. Deve essere lungo minimo 3 caratteri e per un massimo di 20.
- **Bio**: breve testo che lo descrive. (opzionale)

**Cosa può fare l'autore:**
- Creare nuove note
- Modificare le proprie guide
- Cancellare le proprie guide
- Pubblicare una guida
- Archiviare le proprie guide


#### Collegamenti interni (GuideLink)
 I collegamenti interni rappresentano relazioni semantiche tra guide del sistema.  
 Servono a creare un alto livello di interconnessione tra i contenuti e a favorire una comprensione profonda e non lineare della conoscenza.

 Un collegamento interno:
- collega una guida a un’altra guida del sistema
- può riferirsi all’intera guida o a una porzione specifica del contenuto
 - è tracciabile come entità di dominio
 
 I collegamenti interni costituiscono la base del knowledge graph di LibraryTools.

#### Riferimenti esterni (Reference)
I riferimenti esterni sono fonti di supporto al contenuto di una guida.  
Possono includere link a siti web, documentazione, articoli, repository o altre risorse esterne.

I riferimenti:
- non creano relazioni strutturali nel sistema
- servono a fornire contesto, approfondimento o validazione delle informazioni
- sono separati dal contenuto principale della guida

 I riferimenti migliorano la qualità informativa senza alterare la struttura della knowledge base.

#### Relazioni:
Author 1 ──── N Guide
Category 1 ─ N Guide
Guide N ──── N Tag
Guide 1 ──── N Reference
Guide N ──── N Guide (via GuideLink)

### STACK:
#### Backend
- **Python 3.11+**
- **FastAPI**
- **Uvicorn** (ASGI server)

#### Database
- **SQLite** → MVP / sviluppo
- **PostgreSQL** → produzione / crescita

#### ORM & DB layer
- **SQLAlchemy 2.0**
- **Alembic** (migrazioni)
#### Data validation / schema
- **Pydantic v2** per: request / response models e separazione netta tra API schema e DB schema

#### Frontend
- **HTML + CSS**
- **JavaScript vanilla**
- fetch API

### Architettura
```
librarytools/
│
├── app/
│   ├── main.py | Applicazione che esegue il programma
│   │
│   ├── core/ | Core files, servono a tutto il programma
│   │   ├── config.py | passwords, configurazioni, autenticazione (in futuro) etc
│   │   └── database.py | uso del database
│   │
│   ├── models/  | Come vengono salvati i dati. Definiscono tabelle, colonne, relazioni
│   │   ├── guide.py
│   │   ├── category.py
│   │   ├── tag.py
│   │   ├── reference.py
│   │   └── guide_link.py
│   │
│   ├── schemas/ |  Che dati accetto? Che dati restituisco?”
│   │   ├── guide.py
│   │   ├── category.py
│   │   └── tag.py
│   │
│   ├── api/ Definizione endpoints, parsing requests, return responses, chiamata a services
│   │   ├── v1/ | versione 1 delle API
│   │   │   ├── guides.py 
│   │   │   ├── categories.py
│   │   │   └── tags.py
│   │
│   └── services/ | aggiornamento, creazione, controlli di stato, regole, orchestrare più modelli
│       └── guide_service.py
│
├── migrations/ | versioni DB, backups, cronologia schema etc
│
├── tests/ | Per tests di scripts
│
├── README.md | Stato del progetto, How to install, how to use, integrazioni, info utili
└── pyproject.toml | Def dipendenze, versione py, strumenti e packaging (requirements.txt insomma)
```

## MVP:
MVP è la versione base funzionante del programma, ecco un elenco delle funzionalità che dovrebbe avere:
- CRUD Guide (Create, Read, Update, Delete)
- CRUD Category (Create, Read, Update, Delete)
- Tags funzionanti (many-to-many)
- Ricerca base (titolo + tags)
- API documentata via Swagger
- DB persistente (SQLite) 

## APIs - Endpoints:
Definiamo come funzionano gli endpoints, ricordati che sono URLs, con HTTP. Qui i metodi HTTP: 

|Metodo|Significato|Uso|
|---|---|---|
|GET|Leggere|Visualizzare dati|
|POST|Creare|Nuova risorsa|
|PUT / PATCH|Modificare|Update|
|DELETE|Eliminare|Cancellare|

Gli endpoints possono essere quindi composti così:

/api/versioneAPI/cosavogliomanipolare/{parametri}

### Endpoints per Guide:
GET    /api/v1/guides
POST   /api/v1/guides
GET    /api/v1/guides/{id}
PATCH  /api/v1/guides/{id}
DELETE /api/v1/guides/{id}

### Endpoints per Categorie:
GET    /api/v1/categories
POST   /api/v1/categories
GET    /api/v1/categories/{id}
PATCH  /api/v1/categories/{id}
DELETE /api/v1/categories/{id}
GET    /api/v1/categories/{id}/guides

### Endpoints per TAGs:
GET /api/v1/tags
GET /api/v1/tags/{id}
GET /api/v1/tags/{id}/guides

**Esempio:**
`/api/v1/guides/{id}`
