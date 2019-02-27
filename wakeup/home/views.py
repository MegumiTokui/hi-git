from django.shortcuts import render
from django.http import HttpResponse



posts=[

    {
        'date':'beautiful',
        'title':'india'
    },
    {
        'hoby':'playing the piano',
        'name':'megumi'
    }
]
def top(request):
   
    return HttpResponse("Hi , I'm  Megu")

def first(request):
    context={
        "posts":posts  #why shold I Add ""
    }
    return render(request, 'home/top.html',context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')


