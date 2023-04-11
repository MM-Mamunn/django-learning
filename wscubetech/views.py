from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userform
def homepage(request):
    finalans = 0
    data={}
    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'ans':finalans,
            }
            url ="/answer/?anss={}".format(finalans)
            return HttpResponseRedirect(url)
        
            # this return the data dictionary to the ans2.html
            # return render(request,"ans2.html",data)
    except:
        pass

    return render(request,"index.html",data)

def course(request):
    return render(request,"course.html")

def courseDetails(request,courseid):
    return HttpResponse(f"your course {courseid}")

def price(request):
    fn =userform()
    data={'form':fn,'n1':10}
    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'ans':finalans,
                'form':fn,
            }
            url ="/answer/?anss={}".format(finalans)
            return HttpResponseRedirect(url)
        
            # this return the data dictionary to the ans2.html
            # return render(request,"ans2.html",data)
    except:
        pass
    return render(request,"price.html",data)

def answer(request):
    if request.method =="GET":
        ans= request.GET.get("anss")
    return render(request,"answer.html",{'ans':ans})

def evenodd(request):
    data={
        'c':'',
        'n':'',
    }
    
    if request.method =="POST":
        n= eval(request.POST.get("num"))
        if n%2 == 0:
            c='EVEN'
        elif n%2 != 0:
            c ='ODD'
        else:
            c='ERROR'
        data={
            'c':c,
            'n':n,
        }
    return render(request,"evenodd.html",data)
    