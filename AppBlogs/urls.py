from django.urls import path

from AppBlogs.views import (
 ArticlesListView, ArticlesDetailView, ArticlesCreateView, ArticlesUpdateView, ArticlesDeleteView, about, create
)

# Son las URLS de la app Appblogs
urlpatterns = [
    # URLS de cursos (funciones)




    path("pages/", ArticlesListView.as_view(), name="list_articless"),
    path("pages/<int:pk>/", ArticlesDetailView.as_view(), name="ver_articles"),
    path("create-articles/", ArticlesCreateView.as_view(), name="create_articles"),
    path("edit-articles/<int:pk>/", ArticlesUpdateView.as_view(), name="edit_articles"),
    path("delete-articles/<int:pk>/", ArticlesDeleteView.as_view(), name="delete_articles"),
    path('about/', about, name="about"),
    

   
]
