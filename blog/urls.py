from django.urls import path
from .views import BlogListView, BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('',BlogListView.as_view(),name = 'blogs'),
    path('detail/<int:pk>',BlogDetailView.as_view(),name ='blogs_detail'),
    path('post/new',BlogCreateView.as_view(), name = 'create_blog'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name = 'update_plog'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name = 'delete_plog'),
]