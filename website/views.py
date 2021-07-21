from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'website/index.html')


def main_home(request):
    return render(request, 'website/home-3.html')


def about_us(request):
    return render(request, 'website/page-about.html')


def our_team(request):
    return render(request, 'website/page-team.html')


def our_services(request):
    return render(request, 'website/page-services.html')


def portfolio(request):
    return render(request, 'website/portfolio-3.html')


def main_blog(request):
    return render(request, 'website/blog-grid.html')


def contact_us(request):
    return render(request, 'website/index.html')
