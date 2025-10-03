## AgendaPython

AgendaPython is a contact management application developed with Python and Django, using SQLite as the database.
## Agenda (AgendaPython)

This project is a simple contact management application built with Python and Django, using SQLite as the default database.

Main features
- Manage contacts (create, edit, delete)
- Photo upload per contact (stored under `media/`)

Project layout
- `agenda/`: Django project settings
- `contacts/`: Django app with models, views, templates and API
- `templates/`: HTML templates
- `media/`: file uploads
- `db.sqlite3`: local SQLite database file
- `manage.py`: Django management script

Prerequisites
- Python 3.8+ (3.9 recommended)

Development setup

1. Clone the repository

```bash
git clone https://github.com/luizcurti/python-agenda.git
cd python-agenda
```

2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply database migrations

```bash
python manage.py migrate
```

5. (Optional) Create a superuser to access the admin

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. The admin is available at `/admin/`.

Serving media files in development

`MEDIA_URL` and `MEDIA_ROOT` are configured in `agenda/settings.py`. The project is set up to serve media files when `DEBUG=True` via `agenda/urls.py`, so no additional configuration is required other than ensuring `media/` is writable.

Running tests

```bash
python manage.py test
```

API (REST)

Basic API endpoints implemented using Django REST Framework:
- List/Create: `GET/POST /api/contacts/`
- Retrieve: `GET /api/contacts/<id>/`

CI

A GitHub Actions workflow is included at `.github/workflows/ci.yml` which runs migrations and tests on push/PR to `main`.

Notes and recommendations
-- You may want to make `Contact.photo` nullable (`null=True`) if you want the DB to allow explicit NULL values for that field — I can make that change and add the migration upon request.
- It's recommended to set `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'` in `agenda/settings.py` to silence warnings.
- Dependencies are listed in `requirements.txt`.

Contributing

PRs and issues are welcome. If you want, I can open a PR with the changes I made (API, tests, CI, README).
