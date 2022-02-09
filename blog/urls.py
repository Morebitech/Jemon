from django.urls import path, include
from .views import home, about

app_name = 'blog'

urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
    # path('about/', about, name='blog-about'),

]
