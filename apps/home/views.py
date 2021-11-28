# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Temp, TempTravel, TempGeneral, FAQGeneral, FAQTravel, FAQ, AboutUs, ContactUs


######################################################################
#                          Views Functions                           #
######################################################################

def temp(request):
    temp = Temp.objects.all()
    temp_general = TempGeneral.objects.all()
    temp_travel = TempTravel.objects.all()
    context = {'temp': temp, 'temp_general': temp_general, 'temp_travel': temp_travel}
    return render(request, 'home/temp.html', context)


def faq(request):
    faq = FAQ.objects.all()
    faq_general = FAQGeneral.objects.all()
    faq_travel = FAQTravel.objects.all()
    context = {'faq': faq, 'faq_general': faq_general, 'faq_travel': faq_travel}
    html_template = loader.get_template('home/FAQ.html')
    return HttpResponse(html_template.render(context, request))


def about_us(request):
    about = AboutUs.objects.all()
    context = {'about': about}
    html_template = loader.get_template('home/about-us.html')
    return HttpResponse(html_template.render(context, request))


def contact_us(request):
    contact = ContactUs.objects.all()
    context = {' contact': contact}
    html_template = loader.get_template('home/contact-us.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

######################################################################
#                     System Functions & Classes                     #
######################################################################
