from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from AppBlogs.models import Articles


class ArticlesListView(ListView):
    model = Articles
    template_name = 'AppBlogs/list_articless.html'


class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    fields = ('title', 'subTitle', 'body', 'author', 'date', 'image')
    success_url = reverse_lazy('list_articless') 
   
   
   
    def form_valid(self, form):
    
        self.object = form.save()
       
        self.object.creador = self.request.user
        self.object.save()
              
              
        return super().form_valid(form)
    

class ArticlesDetailView( DetailView):
    model = Articles
    success_url = reverse_lazy('list_articless')
 
class ArticlesUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    fields = ('title', 'subTitle', 'body', 'author', 'date', 'image')
    success_url = reverse_lazy('list_articless')

class ArticlesDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy('list_articless')

def about(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="about.html",
        context=contexto,
    )
    return http_response

def create(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="create.html",
        context=contexto,
    )
    return http_response

