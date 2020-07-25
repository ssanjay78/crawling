from django.shortcuts import render, redirect
from django.contrib import messages
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
# Create your views here.
link_sets = set()

def crawler(request):
    if request.method == "POST":
        url = request.POST['url']

        find_url(url)
        messages.info(request, link_sets)
        print()
        return redirect('/')

    return render(request, 'crawler.html')


def find_url(url):
    global link_sets
    html = urlopen(url)
    page = soup(html, 'html.parser')
    for link in page.findAll("a",{'href':re.compile('^http')}):
        if ('href' in link.attrs):
            if link.attrs['href'] not in link_sets:
                newLink = link.attrs['href']
                if 'rirm.in' in newLink:
                    print(newLink)
                    link_sets.add(newLink)
                    find_url(newLink)
