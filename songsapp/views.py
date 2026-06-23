from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Song
import json

@csrf_exempt
def song_list(request):
    if request.method == 'GET':
        songs = list(Song.objects.values())
        return JsonResponse(songs, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        song = Song.objects.create(title=data['title'], artist=data['artist'], lyrics=data.get('lyrics', ''))
        return JsonResponse({'id': song.id, 'title': song.title, 'artist': song.artist})