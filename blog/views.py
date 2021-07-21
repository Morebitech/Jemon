from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# function to handle the traffic from homepage


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

# the viewsets is a module in DRF which has classes like ModelViewSet ....
# ModelViewSet helps us define if its a POST or GET request and we don't have to do that explicitly
# class PostView(viewsets.ModelViewSet):
#     queryset = Post.objects.all()  # its just how i am going to query the data from the DB / actually same as how you get them from a render
#     serializer_class = PostSerializer

#
# @api_view(['GET', 'POST'])
# def postView(request):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     return Response(queryset, serializer_class)
