from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Album



class IndexView(generic.ListView):
    # specify what template to use, use index.html to display the album
    template_name = 'music/index.html'
    # the name return by default is object_list, but we can re-written it
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


# when we have created notre class, we can do the things following to add the new albums
class AlbumCreate(CreateView):
    model = Album
    # what attributes, in models.py
    fields = ['artist','album_title','genre','album_logo']
