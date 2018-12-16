from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<id>/', views.movie_detail, name='details'),
    path('', views.movie_search, name='home'),
    # path('<query:query>/', views.movie_search, name='movies_list'),
    
    
]