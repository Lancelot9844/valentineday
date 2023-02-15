from django.urls import path
from . import views
urlpatterns= [
    path('',views.Bibek, name="Bibek"),
    path('',views.name, name="name"),
    
    path('',views.index, name="index"),
    
]