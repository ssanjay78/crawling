from django.shortcuts import render, redirect
from django.contrib import messages
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
# Create your views here.
link_sets = set()

def crawler(request):
    if request.method == "POST":
        url1 = request.POST['url']
        url = 'https://' + str(url1)

        if not url1:
            messages.info(request, "URL cannot be blank!")
            return redirect('/')

        find_url(url, str(url1))
        result = sorted(link_sets)
        urls_found = len(link_sets)
        
        return render(request, 'result.html', {'result':result, 'url':url1, 'urls_found':urls_found })
        
    return render(request, 'crawler.html')


def find_url(url, url1):
    global link_sets
    try:
        html = urlopen(url)
        page = soup(html, 'html.parser')
    
        for link in page.findAll("a",{'href':re.compile('^http')}):
            if ('href' in link.attrs):
                if link.attrs['href'] not in link_sets:
                    newLink = link.attrs['href']
                    if (url1 in newLink) and ('.jpg' not in newLink) and ('#' not in newLink):
                        if len(link_sets)==100:
                            break
                        print(newLink)
                        link_sets.add(newLink)
                        find_url(newLink,url1)
    except Exception:
        pass

def result(request):
    return render(request, 'result.html')
