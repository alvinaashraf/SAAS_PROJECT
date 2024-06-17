from django.http import HttpResponse
from django.shortcuts import  render

from visits.models import PageVisit

def home(request,*args ,**kwargs):
    my_title='new page'
    query=PageVisit.objects.all()
    PageVisit.objects.create()

    context={
        'title': my_title,
        'query':query.count()
    }
    return render(request,'home.html',context)