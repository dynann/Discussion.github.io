from django.urls import path 
from .views import PostView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView
urlpatterns = [
   path('', PostView.as_view(), name='post'),
   path('/new', PostCreateView.as_view(), name='post_new'),
   path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
   path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
   path('/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]  