# [Make A Trip](https://www.makeatrip.live)

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/KfirGerman/MakeATrip.git
$ cd MakeATrip
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```
<br/>

## Unit Test
How to test:
```bash
$ # authentication/tests
$ # home/tests
$ cd MakeATrip
$ python manage.py test # for all tests
$ python manage.py test apps.home # for home application test only.
$ python manage.py test apps.authentication # for home authentication test only.
```


## Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                                     # Implements app configuration
   |    |-- settings.py                          # Defines Global Settings
   |    |-- wsgi.py                              # Start the app in production
   |    |-- urls.py                              # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                                # A simple app that serve HTML files
   |    |    |-- views.py                        # Serve HTML pages for authenticated users
   |    |    |-- urls.py                         # Define some super simple routes  
   |    |
   |    |-- authentication/                      # Handles auth routes (login and register)
   |    |    |-- urls.py                         # Define authentication routes  
   |    |    |-- views.py                        # Handles login and registration  
   |    |    |-- forms.py                        # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images, JQuery>               # CSS files, Javascripts files
   |    |
   |    |-- templates/                           # Templates used to render pages
   |         |-- includes/                       # HTML chunks and components
   |         |    |-- navigation.html            # Top menu component at Admin Pages
   |         |    |-- sidebar.html               # Sidebar component at Admin Pages
   |         |    |-- footer.html                # App Footer at Admin Pages
   |         |    |-- scripts.html               # Scripts common to Admin pages
   |         |    |-- travel_navigation.html     # Top menu Travel Pages
   |         |    |-- travel_navigation.html     # App Footer at Travel Pages
   |         |    |-- travel_scripts.html        # Scripts common to Travel pages
   |         |
   |         |-- layouts/                        # Master pages
   |         |    |-- base-auth.html              # Used by Authentication pages
   |         |    |-- base_dashboard.html         # Used by Admin Panel pages
   |         |    |-- base-travel.html            # Used by Travel pages
   |         |    |-- base.html                   # Used by Error pages
   |         |
   |         |-- accounts/                        # Authentication pages
   |         |    |-- login.html                  # Login page
   |         |    |-- register.html               # Register page
   |         |    |-- accounts/                   # Reset Password Pages
   |         |        |-- *.html/                 # Reset Password page
   |         |
   |         |-- home/                            # UI Kit Pages
   |              |-- index.html                  # Index page
   |              |-- 404-page.html               # 404 page
   |              |-- 500-page.html               # 404 page
   |              |-- *.html                      # All other pages
   |
   |-- requirements.txt                           # Development modules - MySQL storage
   |
   |-- .env                                       # Inject Configuration via Environment
   |-- manage.py                                  # Start the app - Django default start script
   |
   |-- ************************************************************************
```

## Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github
