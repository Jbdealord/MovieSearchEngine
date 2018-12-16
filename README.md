# TMDb movie search engine

A movie-search engine developed on Django using TMDb api.
## Contents
- Search movie
- Results on detail page:
  - Primary info
  - Alternative titles
  - Cast
  - Crew
  - Images (posters, backdrops)
  - Plot keywords
  - Release information
  - Trailers
  - Reviews

## Dependencies

- **`Django 2.1`**: Python web framework.
- **`tmdbsimple`**: TMDb V3 API for python.
- **`django-mathfilters`**: Python module that provides different simple math filters for Django.


### Install Dependencies

- **pip:**
  ```
    sudo -H pip3 install -U pipenv
    pipenv --python 3.6
    pipenv shell
    
    pip install -r requirements.txt
  ```
- **Run Django Server:**
    ```
        python manage.py runserver
    ``` 

