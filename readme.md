## AgendaPython

AgendaPython is a contact management application developed with Python and Django, using SQLite as the database.

# Features
Contact Management: Allows adding, editing, and deleting contacts.

Photo Upload: Supports uploading photos for each contact, storing them in the media/photos/ directory.

# Project Structure
* agenda/: Contains the main configurations of the Django project.
* contacts/: Includes the application responsible for managing contacts.
* media/photos/: Directory where contact photos are stored.
* templates/: Contains the HTML templates used for rendering the pages.
* db.sqlite3: SQLite database storing the application data.
* manage.py: Django management script for running administrative commands.

# Prerequisites
* Python 3.x
* Django
* SQLite

## How to Run

1. Clone the repository:
* git clone https://github.com/luizcurti/agendaPython.git

2. Navigate to the project directory:
* cd agendaPython

3. Install the dependencies:
* pip install django

4. Run database migrations:
* python manage.py migrate

5. Start the development server:
* python manage.py runserver

Access the application in your browser at http://127.0.0.1:8000/.

## Notes
Ensure that the media/photos/ directory has the appropriate read and write permissions, allowing the upload and display of contact photos.

To add new contacts, use the Django admin interface at http://127.0.0.1:8000/admin/ and register a superuser.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests with improvements and bug fixes.