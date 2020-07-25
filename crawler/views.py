from django.shortcuts import render

# Create your views here.

def crawler(request):
    return render(request, 'crawler.html')