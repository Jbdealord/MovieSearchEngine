from django.shortcuts import render
import tmdbsimple as tmdb
from pprint import pprint
from operator import itemgetter

tmdb.API_KEY = '7acc9f790b3d36958f609e757ec9baca'



def movie_search(request):
    """
    View for home page and movies listing using search box.
    Sorting movies list through 'vote_average'
    """
    movie_list = None
    query = str(request.GET.get('query', ''))
    print("\n\n\n")
    print(query)

    if query:
        result = tmdb.Search().movie(query=query)['results']
        movie_list = sorted(result, key=itemgetter('vote_average'),reverse = True)
        # pprint(movie_list)
        # movie_list = 

    return render(request,'movies/home.html',
        {'movie_list': movie_list,
        'query': query})


def movie_detail(request, id):
    """
    Movie detail view.
    """
    movie = tmdb.Movies(id)
    
    video = movie.videos()['results']
    
    trailers = list(filter(lambda x: x['type'] == 'Trailer', video))
    images = movie.images()
    # pprint(video)
    # pprint(images)
    # pprint(movie.credits())
    # pprint(movie.credits()['cast'][:10])
    # pprint(movie.credits()['crew'][:10])
    
    movie_data = {
        "info": movie.info(), #Primary info
        "altname": movie.alternative_titles()['titles'], #Alternative titles
        "cast": movie.credits()['cast'][:10], #Cast
        "crew": movie.credits()['crew'][:10], #Crew

        "images": images, #Images (posters, backdrops)
        
        "keywords": movie.keywords()['keywords'], #Plot keywords
        "year": movie.info()['release_date'][:4], #Release Information
        
        "trailer": trailers[:1], #Picking one Trailer from list
        
        "reviews": movie.reviews()['results'], #Reviews
    }
    pprint(movie_data['trailer'])

    return render(request, "movies/details.html",
        {'movie_data': movie_data,
        'query': movie.info(),
        })