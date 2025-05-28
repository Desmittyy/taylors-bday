from django.shortcuts import render


# Create your views here.
def mainpage_views(request):
    return render(request, 'home.html')