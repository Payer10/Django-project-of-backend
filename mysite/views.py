from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    
    return render(request,'index.html')
def about(request):
    newtext = request.GET.get('text','default')
    getans = request.GET.get('removefunc','off')
    charactercount = request.GET.get('charactercount','off')
    fullcaps = request.GET.get('fullcaps','off')
    if getans == 'on':
        all_punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        new_ans = ""
        for chr in newtext:
            if chr not in all_punctuations:
                new_ans += chr
            prams = {'a':'removed punctuations','b':new_ans}
        newtext = new_ans
       # return render(request,'about.html',prams)
    if(fullcaps == 'on'):
        new_ans = ""
        for chr in newtext:
            new_ans += chr.upper()
            prams = {'a':'character count','b':new_ans}
    if(charactercount == 'on'):
        new_ans = 0
        for chr in newtext:
            if chr != " ":
                new_ans += 1
            prams = {'a':'character count','b':new_ans}
    return render(request,'about.html',prams)
    