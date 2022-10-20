# 👋 Hi everyone! :smile:

### Database development
<br>
- I thought about how I could make a database up similar to Pinterest's database and made an ER diagram:
<img src="https://github.com/RicardoRobledo/calling-art-backend/blob/main/diagrams/calling-art-er-diagram.png" width="700" height="400">
<br>


- The database was made up in Django's ORM.
- For development purposes Clever Cloud was used due to you can make a free account there: https://www.clever-cloud.com/.

<br>
<hr>

### API development and programming
<br>

- python-decouple was added to isolate our credentials like database name, password, host and Django's secret key in enviroment variables inside a 'settings.ini' file.
- Django REST Framework was implemented to create an API that a fronted can query, for tests Postman was used. You can watch tests here: [Tests](https://github.com/RicardoRobledo/calling-art-backend/tree/main/postman_tests).

#### This is an image about tests:
<img src="https://github.com/RicardoRobledo/calling-art-backend/blob/main/postman_tests/tests.png" width="700" height="400">

<br>

- djangorestframework-simplejwt has been used to have access tokens by time. 
- django-filter was added to make querys depend on your search parameters like user, by an id or name.
- drf_yasg was added to have documentation of this API in each view that we can use like define what is returned and what type of parameters we can introduce to help frontends to query this API.

<br>
<hr>

### Deployment

- [Heroku](https://www.heroku.com/) was chosen for deploy and pyscopg2 was installed due to Heroku use PostgreSQL.
- dj-database-url was installed. Like Heroku use postgre we get an URL with all data of connection, due to this we need to implements this library.
- django-cors-headers has been added to can share information through internet, if we don't use it we can't share information around internet.
- whitenoise was implemented to can serve static files, in this case Heroku didn't let me deploy my API even if I didn't deal with images.
- gunicorn was added to use servers Unix.

<br>
<hr>

### Configuration

- Once deployed our API we need to move our enviroment variables inside from our 'setting.ini' file to Heroku, you can do it on graphic interface or through commands.

<br>
<hr>

#### :thumbsup: Thanks you and enjoy this repository.
#### :clap: Happy learning.
