from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'new.html')



def analyze(request):
    djtext = request.GET.get('text', 'default')
    hey=request.GET.get('hey', 'off')
    print(hey)
    print(djtext)
    if hey=="on":
        punc=''';:'".,/?[{}]"'''
        analyze=""
        for char in djtext:
            if char not in punc:
                analyze = analyze+char  
                rohit={'purpose':'Removed Punctuation', 'analyze_text': analyze}


        return render(request,'ana.html',rohit)
    else:
        return HttpResponse("Error")