# Mi Negocio

## Requirements

Before you begin, make sure you have the following installed:

- [Python 3.8.0](https://www.python.org/downloads/release/python-380/)

## Installation

1. Clone the repository or download it as a ZIP file.

```bash
git clone <REPOSITORY_URL>
```

2. Navigate to the project's root directory.

```bash
cd mi_negocio
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Configuration

1. Ensure that you have the environment and necessary environment variables configured for the project.



## Execution

To run the project, follow these steps:

1. Apply migrations to create the database.

```bash
python manage.py migrate
```

2. Create a superuser to access the Django admin panel. (Only in the case you want to see the data on de django admin interface, is not necesary)

```bash
python manage.py createsuperuser
```

3. Start the development server.

```bash
#local
python manage.py runserver --settings=settings.dev
#dev
python manage.py runserver --settings=settings.local
#prod
python manage.py runserver --settings=settings.prod
```

The project will be available at `http://127.0.0.1:8000/`.
You can access the admin panel at `http://127.0.0.1:8000/admin/`.

## Tests

To run the tests, use the following command:

```bash
python manage.py test --verbosity=2
```
