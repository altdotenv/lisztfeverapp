from django.urls import include, path  #django 2.0 version url dispatcher
from . import views

app_name = "artists"
urlpatterns = [
    path("search/", view=views.SearchArtist.as_view(), name='search_artist'),
    path("<str:artist_id>/", view=views.Artist.as_view(), name='artist'),
]
