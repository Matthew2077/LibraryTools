# LibraryTools
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, API-first backend for managing and structuring knowledge through notes, categories, and tags.
Built with **FastAPI** and **SQLAlchemy 2.0**, designed for clarity and future growth.


## What It Does
LibraryTools helps you organize information by creating notes that are:
- **Categorized** — group notes into structured categories
- **Tagged** — assign multiple tags for flexible filtering
- **Status-tracked** — manage note lifecycle (draft → published → archived)

Perfect for personal knowledge bases, documentation systems, or as a foundation for larger content management platforms.


## Project Structure:
```
librarytools/
├── api/v1/          # FastAPI routes
├── core/            # Database & models
├── repositories/    # Data access layer
├── schemas/         # Pydantic models
└── services/        # Business logic
```
For a detailed technical overview, see [`v1_review.md`](./v1_review.md).

## Quick Start

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Matthew2077/LibraryTools.git
cd librarytools

# 2. Build docker image
sudo docker build -t librarytools .

# 3. Run container
sudo docker run -p 5000:5000 librarytools

The API will be available at http://127.0.0.1:5000/docs


# Usefull commands:
# Remove all not used images
sudo docker system prune
# view active containers
sudo docker ps

```
