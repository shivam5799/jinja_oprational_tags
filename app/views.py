from django.shortcuts import render

# Create your views here.



def forloop(request):
    details={
        'name':'shivam',
        'age':22,
        'gender':'male'
    }

    return render(request,'index.html',details)


def ifcond(request):
    d={'a':12,'b':10,'c':300}

    return render(request,'index.html',d)