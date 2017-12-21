from django.conf.urls import url
from .views import (
    CocktailListAPIView,
    CocktailCreateAPIView,
    CocktailRetrieveAPIView,
    CocktailDeleteAPIView,
    CocktailUpdateAPIView,
    UserCreateAPIView,
    PostCreateAPIView)
urlpatterns = [
    url(r'^cocktail/$', CocktailListAPIView.as_view(), name = 'list'),
    url(r'^cocktail/create$', CocktailCreateAPIView.as_view(), name='create'),
    url(r'^cocktail/(?P<pk>\d+)/$', CocktailRetrieveAPIView.as_view(), name = 'detail'),
    url(r'^cocktail/edit/(?P<pk>\d+)/$', CocktailUpdateAPIView.as_view(), name = 'update'),
    url(r'^cocktail/delete/(?P<pk>\d+)/$', CocktailDeleteAPIView.as_view(), name = 'delete'),
    url(r'^comment/create$', PostCreateAPIView.as_view(), name='post'),
    url(r'^usercreate/$', UserCreateAPIView.as_view(), name='createuser'),
]