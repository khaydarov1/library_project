from django.urls import path
from .views import BookListApiView,BookDetailApiView,BookCreateApiView,BookDeleteApiView,BookUpdateApiView
urlpatterns = [
    path('book/', BookListApiView.as_view()),
    path('book/<int:pk>/', BookDetailApiView.as_view()),
    path('create/', BookCreateApiView.as_view()),
    path('<int:pk>/update/', BookUpdateApiView.as_view()),
    path('delete/<int:pk>/', BookDeleteApiView.as_view())

]
