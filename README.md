# LibraryTools

## Stato del progetto:
Obbiettivo: finire l'MVP, ovvero la versione alpha funzionante del programma. Vedi MVP sotto
Stato di completamento: 5%
Completamento aspettato per: fine marzo

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
- **NoteID**: univoco, numerico, auto increment (parte da 100000). Le note con ID < di 1000000 sono note di sistema o usate per altri scopi
- **GuideURL**: Nome non cambiabile della guida, in modo che possa essere usato per raggiungere le guide anche se il titolo viene cambiato;
- **Titolo**: Deve essere maggiore di 3 lettere con un massimo di 50/70, può essere cambiato
- **Contenuto**: Stringa
- **Categoria**: Deve appartenere ad una categoria. Per ora sarà una sola

**Altri Contenuti:**
- **tags**: Lista di stringhe. Nei meta data possono essere aggiunti dei tags che aiutano l'utente nella ricerca dei contenuti. Questi tag dovrebbero descrivere il contenuto. La funzione dei tag è quindi una funzione prettamente di supporto nella ricerca, non di categorizzazione e quindi di strutturazione.
- **NomeAutore**: Definire chi ha scritto la guida
- **DataCreazione**: Indica la data di creazione della guida
- **DataUltimaModifica:** utile per il versioning
- **DataPubblicazione**: Quando è stata pubblicata
- **Stato**: può essere bozza, pubblicato, archiviato (nota: capire come gestire le modifiche);

#### Categorie:
Le categorie sono insiemi di guide che condividono uno stesso tema o argomento. Ogni categoria deve avere:
- **CatID:** univoco, numerico, autoincrement
- **CatName**: Identificativo che sarà usato nel sistema per riconoscere e usare la categoria. Deve essere univoco
- **Descrizione**: Cosa rientra in questa categoria, regole e definizione. 

- **Parentele**: una categoria può stare da sola, ma per maggiore chiarezza è bene creare un sistema complesso di categorie che migliorare l'organizzazione delle guide nel sistema. 

#### Tags 
I tags sono strutture libere che servono ad aumentare la facilità di ricerca delle guide. Essi possono essere aggiunti dall'autore nel header della guida, non sono  case sensitive (così riduco ridondanza e riduce ambiguità). I tags sono liberi, possono essere creati dagli autori stessi nella loro aggiunta, pertanto nessuno possiede un tag, i tag esistono finché c'è qualcuno che lo usa. 

I tags possono essere visti in una visualizzazione specifica che permette di vedere tutti i tags esistenti, quali note sono legate ad esse ed esplorare. 

Ogni tag deve avere:
- **TagID:** univoco, numerico, auto incrementale (parte da 1);
- **label**: Deve avere un nome che lo identifica, come "python", "RoK" etc

#### Autore:
L'autore è colui che scrive le guide, le può modificare, eliminare, archiviare etc. **Caratteristiche dell'autore:**
- **AuthorID:** univoco, numerico (parte da 10000 fino a 99999)
- **AuthorName:** Deve essere univoco, sarà usato nel sistema per riferisi a quell'autore. Deve essere lungo minimo 3 caratteri e per un massimo di 20.
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
*IN REVISIONE*
```
/librarytools
├── main.py              # Inizializza l'app e include i router
├── core/
│   ├── database.py      # Engine, SessionLocal
│   └── models.py        # Classi SQLAlchemy (Guide, Category, Tag, Author)
│
├── api/ (o routes/)     # endpoints FastAPI
│   ├── guides.py        # @router.post("/guides") -> chiama service
│   └── categories.py    idem
│
├── services/            # Azioni del programma
│   ├── guide_service.py # Funzioni come: create_guide(), get_all_guides()
│   └── cat_service.py
│
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
