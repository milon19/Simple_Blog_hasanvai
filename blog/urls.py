from django.urls import path
from .views import Home, BlogDetailView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),

]
