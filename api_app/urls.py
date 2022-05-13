from django.urls import path
from .views import Film, FilmUpdate

urlpatterns = [
    path('film/', Film.as_view()),
    path('update-film/<int:film_id>', FilmUpdate.as_view()),
]