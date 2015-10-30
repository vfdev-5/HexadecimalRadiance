# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from models import Data


# Create your views here.
def main(request, template_name='main.html'):

    context={}
    if cache.get('can_access', False):
        context['can_access']=True

        try:
            data = Data.objects.get(name='default')
            print "Data: ", data.name, data.appFile, data.googlePlayUrl
            context['googlePlayUrl'] = data.googlePlayUrl
            context['appFile'] = data.appFile
        except ObjectDoesNotExist:
            print "Default data is not found"
            pass


    return render(request, template_name, context)


def verification(request, template_name='verification.html'):

    context={}
    if request.method == "POST":

        day = request.POST.get("day", None)
        month = request.POST.get("month", None)
        p1 = request.POST.get("p1", None)
        p2 = request.POST.get("p2", None)
        if day and month and p1 and p2:
            if day == '6' and \
                month == '12' and \
                p1.lower() == u"шевр" and \
                p2.lower() == u"ипо":
                print "OK"
                cache.set('can_access', True)

        return redirect("/main/")


    return render(request, template_name, context)



