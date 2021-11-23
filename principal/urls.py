from django.urls import path
from .views import *

app_name = "principal"

urlpatterns = [
    path('', index, name="index"),
    path('publicaciones/', Publicaciones.as_view(), name="publicaciones"),
    path('comentar/', ComentarPublicacion.as_view(), name="comentarios"),
    path('publicacion/<int:pk>', Publicacion.as_view(), name="publicacion")
]
