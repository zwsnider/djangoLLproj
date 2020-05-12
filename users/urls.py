#We import the path function, and then import the include function so we can
# include some default authentification URLs that Django has defined.
from django.urls import path, include


app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]
