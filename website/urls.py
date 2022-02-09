from django.urls import path, include
from .views import about_us, contact_us, index, our_services, our_team, portfolio, main_home, main_blog

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('home/', main_home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('our-team/', our_team, name='our-team'),
    path('our-services/', our_services, name='our-services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('main-blog/', main_blog, name='main-blog'),
    path('contact-us/', contact_us, name='contact-us'),
    # path('about/', about, name='blog-about'),

]
