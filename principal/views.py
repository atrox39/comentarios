from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import ListView, CreateView, DetailView
from .models import Comentario, Publicacion
from .forms import CrearComentario

def index(request):
    return render(request, 'index.html')

class Publicaciones(ListView):
    model = Publicacion

class Publicacion(DetailView):
    model = Publicacion
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(Publicacion, self).get_context_data(**kwargs)
        comentarios = Comentario.objects.filter(publicacion=self.kwargs['pk']).order_by("-id")
        context['form'] = CrearComentario
        context['comentarios'] = comentarios
        return context

class ComentarPublicacion(CreateView):
    model = Comentario
    form_class = CrearComentario
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect('/publicacion/'+str(form['publicacion'].value()))