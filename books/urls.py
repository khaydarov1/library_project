from django.urls import path
from .views import BookListApiView, BookDetailApiView, BookCreateApiView, BookDeleteApiView, BookUpdateApiView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookListApiView, basename='books')

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('book/<int:pk>/', BookDetailApiView.as_view()),
    path('create/', BookCreateApiView.as_view()),
    path('<int:pk>/update/', BookUpdateApiView.as_view()),
    path('delete/<int:pk>/', BookDeleteApiView.as_view())

]
urlpatterns = urlpatterns + router.urls
