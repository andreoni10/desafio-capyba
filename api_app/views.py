from django.views import View
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
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

        film = Films.objects.create(**film_data)

        data = {
            "messege": f"New item added to List with id: {film.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        page_number = request.GET.get('page_number', 1)
        paginatedFilms = filterAndPaginate(request.GET, Films.objects.all())
        films_data = []
        
        for film in paginatedFilms.page(page_number).object_list:
            films_data.append({
                'film_name': film.film_name,
                'film_release': film.film_release,
                'film_genre': film.film_genre,
            })

        data = {
            'films': films_data,
            'count': paginatedFilms.count,
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

def filterAndPaginate(GET, films):
    page_size = GET.get('page_size', 5)
    name = GET.get('name')
    order_by = GET.get('order_by')

    if(name):
        films = films.filter(film_name__contains = name)

    films = films.order_by(order_by or 'film_release')

    return Paginator(films, page_size)