from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    # return HttpResponse("<h1>i am the index page</h1> ")

    # params ={'name':'rashmi','age':23}
    # return render(request,'index.html',params)
    return render(request,'index.html')

def analyze(request):
    textme=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    if removepunc=="on":
        analyze=""
        for char in textme:
             if char not in string.punctuation:
                analyze=analyze + char
    else:
        analyze=textme

    params ={'purpose':'remove punctuations','analyzed_text':analyze}
    return render(request,'analyze.html',params)
    # return HttpResponse("<h1>i am about page=</h1> ")