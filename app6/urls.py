from django.urls import path
from .views import * 

urlpatterns = [
    path('',main_view,name='main_view'),
    path('<int:id>/stats/',url_details, name = 'url_details'),
    path('r1edirect/<int:id>/', r1edirect, name = 'r1edirect'),
    path('addurl/', add_url, name = 'add_url'),
    path('deleted/<int:id>',delete_note, name = 'delete_url')

]
