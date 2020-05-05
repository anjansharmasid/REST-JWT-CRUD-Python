# REST-JWT-CRUD-Python
Simple python rest application with basic CRUD functionality and use of access and refresh token.

# Test commit
Packages to install to start development:

pip install django==2.2
pip install djangorestframework
pip install django-serializer
pip install djangorestframework_simplejwt
pip install request

// Test
Commands to run during development:

dango-admin startproject pythonrest
python manage.py startapp restserver
python manage.py createsupperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Basic djangorestframework with Create, Retrive, Update and Delete (CRUD) api and JWT. Follow the steps as given below:

1. Create a folder 'Python-REST', add a django project 'pythonrest' add a application called 'restserver', make migrations and migrate, create createsupperuser and again do migrations and migrate.

2. Create a Model class called Customer 

3. Create a new file (package) called serializers. Add a class called CustomerSerializerand inherits functionality from serializers.ModelSerializer given by the rest framework.

4. Add a class called Customer to view. Inherit from rest_framework.viewsets. Supply CustomerSerializer to the framework.

5. Add app urls.py file.  rest_framework provider routers CRUD url for application out of the box. No need to create separate view for CRUD url when using routers. Add login a login page by adding  "path('api-auth/', include('rest_framework.urls')"  CRUD url by adding "path('',include(router.urls))" and access token url by  adding " path('api/token/', TokenObtainPairView.as_view()), path('api/token/refresh/', TokenRefreshView.as_view())" 


6. Add urls to project urls " path('', include('restserver.urls')),"
7. Register to admin site "admin.site.register(Customer)"

8. On the project setting file add the followings
 DEFAULT_PERMISSION_CLASSES  and DEFAULT_AUTHENTICATION_CLASSES area added to the application
 through setting for all end points.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_PERMISSION_CLASSES' : ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',)
}

9. Create a test application to test the solution, login to site with admin account and get access token, use access token to make api call.

