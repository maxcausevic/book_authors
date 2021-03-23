from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('authors', views.authors_index),
    path('create_book', views.create_book),
    path('create_author', views.create_author),
    path('display_book', views.display_book),
    path("display_book/<book_id>",views.display_book),
    path('display_author/<author_id>', views.display_author),
    path('add_author', views.add_author),
    path('add_book', views.add_book)
]