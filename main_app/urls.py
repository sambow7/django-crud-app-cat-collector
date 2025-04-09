from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'), # Define a URL pattern for the home page
    path('about/', views.about, name='about'), # Define a URL pattern for the about page
]
