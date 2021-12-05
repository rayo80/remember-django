from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.detail, name='detailname'),
    path('rooms',views.rooms,name='rooms'),
    path('new',views.new,name='new')
]