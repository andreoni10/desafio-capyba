from ast import Delete
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Films
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Film(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        f_name = data.get('film_name')
        f_release = data.get('film_release')
        f_genre = data.get('film_genre')

        film_data = {
            'film_name': f_name,
            'film_release': f_release,
            'film_genre': f_genre,
        }

        list_film = Films.objects.create(**film_data)

        data = {
            "messege": f"New item added to List with id: {list_film.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        films_count = Films.objects.count()
        films = Films.objects.all()
        
        films_data = []
        for film in films:
            films_data.append({
                'film_name': film.film_name,
                'film_release': film.film_release,
                'film_genre': film.film_genre,
            })

            data = {
                'films': films_data,
                'count': films_count,
            }
            return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class FilmUpdate(View):
    def patch(self, request, film_id):
        data = json.loads(request.body.decode("utf-8"))
        film = Films.objects.get(id=film_id)
        film.film_genre = data['film_genre']
        film.save()

        data = {
            'messege' : f'Film {film_id} has benn updated'
        }
        return JsonResponse(data)

    def delete(self, request, film_id):
        film = Films.objects.get(id=film_id)
        film.delete()

        data = {
            'messege' : f'Film {film_id} has been deleted'
        }
        return JsonResponse(data)