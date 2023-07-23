# Mi Negocio

---

# Index

- [Prerequisites](#prerequisites-) 📋
- [Installation](#installation-) 🔧
- [Setting Environment Variables](#setting-environment-variables-) 📦
- [Execution](#execution-) ⚙️
- [Tests](#tests-) 🧪
- [Tools](#tools-) 🛠️
- [Endpoints](#endpoints-) 📩
- [Postman](#postman)
- [Tasks](#tasks-) 📚
- [Authors](#authors-) ✒️

---

# Let's go 🚀

_These instructions will allow you to get a working copy of the project on your local machine for development and testing purposes._

# Prerequisites 📋

[Index](#index)

Before you begin, make sure you have the following installed:

- [Python 3.8.0](https://www.python.org/downloads/release/python-380/)

# Installation 🔧

[Index](#index)

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

# Setting Environment Variables 📦

[Index](#index)

Ensure that you have the environment and necessary environment variables configured for the project. Create an **.env file** with the following settings, you will also find an example **.env.dist file**

```
DEBUG=True
```

# Execution ⚙️

[Index](#index)

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

# Tests 🧪

[Index](#index)

To run the tests, use the following command:

```bash
python manage.py test --verbosity=2
```

# Tools 🛠️

[Index](#index)

- [Python](https://www.python.org/) - is an easy language to read and write due to its great similarity to human language. Plus, it's an open source, cross-platform language and therefore free!

- [Django](https://www.djangoproject.com/) - is one of the most popular frameworks for developing web applications using the Python language. It has advantages such as its use of software architecture patterns, its flexibility, the high quality of its documentation, and its large community of developers.

- [DjangoRestFramework](https://www.django-rest-framework.org/) - is a framework that allows us to easily develop a REST API in Python. It has several advantages such as authentication, security, serialization, pagination, direct interaction with the Django ORM among others.

- [pdb](https://docs.python.org/3/library/pdb.html) - it's a really easy python debugger, to check a code snippets or whole streams, recommended for beginners in debugging
  
- [threading](https://docs.python.org/3/library/threading.html) - is a simple way to carry out tasks running on background

- [SQLite](https://www.sqlite.org/index.html) - is  a small, fast, self-contained, high-reliability, full-featured, SQL database engine. For this project a powerful database manager was not needed, like PostgreSQL for example.

# [Endpoints](extra/ENDPOINTS.md) 📩

[Index](#index)

Below is a list of the available endpoints:

- ## [Client](extra/ENDPOINTS.md#client)

- ## [Address](extra/ENDPOINTS.md#address)

---

# Postman  

[Index](#index)

You can find a postman_collenction file to replicate ([here](API.postman_collection.json))

# Tasks

[Index](#index)

Implementar las siguientes funcionalidades:

- Funcionalidad para buscar y obtener un listado de clientes. ✅([see](extra/ENDPOINTS.md#list-client))
- Funcionalidad para crear un nuevo cliente con la dirección matriz ✅([see](extra/ENDPOINTS.md#create-client))
- Funcionalidad para editar los datos del cliente ✅([see](extra/ENDPOINTS.md#update-client))
- Funcionalidad para eliminar un cliente ✅([see](extra/ENDPOINTS.md#delete-client))
- Funcionalidad para registrar una nueva dirección por cliente ✅([see](extra/ENDPOINTS.md#create-address))
- Funcionalidad para listar las direcciones adicionales del cliente ✅([see](extra/ENDPOINTS.md#list-addresses))

----

# Authors ✒️

[Index](#index)

- **Mauricio Aguilera** - _IT Enginneer_
  - [Github](https://github.com/maguilera0810)
  - [Linkedin](https://www.linkedin.com/in/maguilera-jaramillo/)

----
