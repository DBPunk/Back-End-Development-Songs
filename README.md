# Songs Microservice

A Django REST API microservice for managing songs, artists, and their lyrics.

## Environment Setup
- Environment name: backend-songs-venv
- Python version: 3.9.x
- Setup script: bin/setup.sh

## Technologies
- Python 3.10+
- Django
- Django REST Framework

## Local Setup
1. Install dependencies: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Run the server: `python manage.py runserver`
4. The server will start on `http://127.0.0.1:8000`

## API Endpoints
- `GET /api/songs/` - List all songs
- `POST /api/songs/` - Add a new song
- `PUT /api/songs/<id>` - Update a song
- `DELETE /api/songs/<id>` - Delete a song
