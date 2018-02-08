# in order to use the 404 faux messages, we should import the phrase
# from django.http import Http404
from django.http import HttpResponse
from .models import Album, Song
from django.template import loader
from django.shortcuts import render, get_object_or_404




# take html and make it available
def index(request):
    all_albums=Album.objects.all()
    # connecting to the HTML
    return render(request,'music/index.html',{'all_albums':all_albums})
# for the step aboeve, we have shown the albums, now we will add the link to each album


def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request, 'music/detail.html', {'album':album})
    ## return HttpResponse("<h2>Details for Album id:"+str(album_id)+"</h2>")
    # what we should do instead is to see if the id is valide or not

# just like the details, whenver we cll the favorite, il will call the album_id
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
#         get the value of the song whose name is "song", and the value is "song.id"
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message':"You did not select a valid song",
        })
    else:
        # to change the attribute
        selected_song.is_facorite=True
        # store the changes in the database
        selected_song.save()
        # if every thing works smoothly, we just return the page
        return render(request, 'music/detail.html', {'album': album})
