from django.urls import path
from .views import PostList, PostDetailView, Search, PostCreateView, subscribe_to_category
from .views import PostDeleteView, PostUpdateView, PostView, CategoryView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post'),
    path('search/', Search.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create'), # Ссылка на создание товара
    # path('create/', PostView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('category/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category/<int:pk>/subscribe_to_category/', subscribe_to_category, name='subscribe_to_category'),
]
