# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text1','default')
    remove=request.POST.get('removepunc','off')
    upper=request.POST.get('uppercase','off')
    newline=request.POST.get('newlineremover','off')
    space=request.POST.get('spaceremover','off')
    charc=request.POST.get('charcount','off')
    if (remove=="on"):
        analyze =" "
        punchutations='''(/[-[\]{}()*+?.,\\^$|#\]/g,'"\\$&");'''
        for char in djtext:
            if char not in punchutations:
                analyze=analyze+char
        params={'pourpose':'Remove Punctions','analyzed_text':analyze}
        djtext=analyze

    if (upper=="on"):
        analyze=""
        for char in djtext:
            analyze=analyze + char.upper()
        params = {'pourpose': 'Change to upper case', 'analyzed_text': analyze}
        djtext = analyze

    if newline=="on":
        analyze=""
        for char in djtext:
            if char != "\n" and char != "\r" :
                analyze=analyze + char
        params = {'pourpose': 'Remove new line', 'analyzed_text': analyze}
        djtext = analyze

    if space=="on":
        analyze=""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyze= analyze+char
        params = {'pourpose': 'Space Remover', 'analyzed_text': analyze}
        djtext = analyze

    if charc=="on":
        x = len(djtext)
        params = {'pourpose': 'Chracter Count', 'analyzed_text': x}
        return render(request, 'analyze.html', params)

    if(remove!="on" and upper!="on" and newline!="on" and space!="on"):
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)
def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')