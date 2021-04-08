from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        list = {'purpose': 'Removed Punctations', 'analyzed_text': analyzed}
        # return render(request,'analyze.html',list)
        djtext = analyzed
#  To convert the string into capitilized
    if (fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        list = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        # return render(request,'analyze.html',list)
        djtext = analyzed

# To remove the lines from text
    if(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != "/n" and char != "/r":
                analyzed = analyzed+char
            list = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        # return render(request,'analyze.html',list)
        djtext = analyzed

# To remove the extra space from text
    if(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed+char
            list = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', list)

# def ex1(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))
