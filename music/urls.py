from django.conf.urls import url
from . import views
# . is the dame directory
app_name='music'
# the app name


urlpatterns=[
    #/music/
    # now we will inport the definition about the index.html, to use those functions, use as_view()
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    #/music/712/
    # the seond is to connect to the vire function
    # "name" is the name of the function
    # /music/<album_id>/favorite/

    # /music/album/add/
    # because we have created another new album, so there is no primary key
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add')

]