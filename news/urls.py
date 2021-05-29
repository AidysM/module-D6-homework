from django.urls import path
from .views import PostList, PostDetailView, Search, PostCreateView
from .views import PostDeleteView, PostUpdateView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post'),
    path('search/', Search.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create'), # Ссылка на создание товара
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]
