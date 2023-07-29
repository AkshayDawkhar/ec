# EC Map


Project Name is a Django web application that allows users to manage places with geographical information. Users can add, view, update, and delete places on the map.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Features

- Add a new place with a name, description, and geographical location (latitude and longitude).
- View a list of all places on the map.
- Filter places by name and description using the search functionality.
- Update the details of a place.
- Delete a place from the map.

## Prerequisites

- Python (3.x)
- Django (3.x)
- Django REST Framework (3.x)
- PostgreSQL with PostGIS extension
- Leaflet (for the front-end map)

## Installation
No need of setup postgres Database
1. Clone the repository.

```bash
git clone https://github.com/your-username/project-name.git
```
2 . install the required Python packages.
``` bash
cd project-name
pip install -r requirements.txt
```
3. runserver
```
python manage.py runserver
```

Open your web browser and go to http://localhost:8000/ to access the application.
Use the application to manage places on the map.
try to search things like python, pune, django, etc
## API Endpoints

The application provides RESTful API endpoints to perform CRUD operations on places:
```api 
GET/api/places/:
```
Get a list of all places or filter places by name and description.
```
POST /api/places/:
```
Add a new place with name, description, latitude, and longitude.
```
GET /api/places/<int:pk>/:
```
Retrieve details of a specific place.
```
PUT /api/places/<int:pk>/: 
```
Update details of a specific place.
```
DELETE /api/places/<int:pk>/:
```
Delete a specific place.

## Technologies Used

    Django
    Django REST Framework
    PostgreSQL with PostGIS extension for spatial data
    Leaflet for interactive map visualization
