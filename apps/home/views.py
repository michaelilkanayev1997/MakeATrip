# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.decorators.csrf import csrf_protect
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import FAQGeneral, FAQTravel, FAQ, AboutUs, ContactUs, Temp, ItineraryPlanner, ItineraryCategory
from .forms import ContactForm, TempForm, AboutUsForm, ItineraryPlannerForm, ItineraryCategoryForm, FaqTravelForm, \
    FaqGeneralForm
from .models import FAQGeneral, FAQTravel, FAQ, AboutUs, Contact, Temp, ItineraryPlanner, Career, PrivacyPolicy
from .forms import ContactForm, TempForm, AboutUsForm, ItineraryPlannerForm, ItineraryCategoryForm, FaqTravelForm, FaqGeneralForm,administrator_complaintsForm,complaintform


######################################################################
#                          Views Functions                           #
######################################################################
@csrf_protect
def administrator_complaints(request):
    administrator_complaints = ContactUs.objects.filter(subject='2')
    count = ContactUs.objects.filter(subject='2').count()

    # user is posting: get edited node, change comment, and save
    if request.POST:
        complete = request.POST.get('complete')
        edited_node = administrator_complaints.get(complete=complete)
        edited_node.save()

    context = {'administrator_complaints': administrator_complaints,'count': count}
    html_template = loader.get_template('home/administrator_complaints.html')
    return HttpResponse(html_template.render(context, request))

@csrf_protect
def complaints(request):
    complaint = ContactUs.objects.filter(subject='2')
    count = ContactUs.objects.filter(subject='2').count()

    # user is posting: get edited node, change comment, and save
    if request.POST:
        complete = request.POST.get('complete')
        edited_node = complaint.get(complete=complete)
        edited_node.save()

    context = {'complaint': complaint,'count': count}
    html_template = loader.get_template('home/complaints.html')
    return HttpResponse(html_template.render(context, request))


def temp(request):
    context = {}
    html_template = loader.get_template('home/temp.html')
    return HttpResponse(html_template.render(context, request))


def edit_faq(request):
    if request.method == "POST":
        general = FaqGeneralForm(request.POST)
        travel = FaqTravelForm(request.POST)
        form = TempForm(request.POST)
        if form.is_valid() and general.is_valid() and travel.is_valid():
            try:
                general.save()
                form.save()
                return redirect('')
            except:
                pass
    else:
        general = FaqGeneralForm()
        travel = FaqTravelForm()
        form = TempForm()
    context = {'form': form, 'general': general}
    html_template = loader.get_template('home/edit-faq.html')
    return HttpResponse(html_template.render(context, request))


def faq(request):
    faq = FAQ.objects.all()
    faq_general = FAQGeneral.objects.all()
    faq_travel = FAQTravel.objects.all()
    context = {'faq': faq, 'faq_general': faq_general, 'faq_travel': faq_travel}
    html_template = loader.get_template('home/faq.html')
    return HttpResponse(html_template.render(context, request))


def about_us(request):
    about = AboutUs.objects.all()
    context = {'about': about}
    html_template = loader.get_template('home/about-us.html')
    return HttpResponse(html_template.render(context, request))


def create_about_us(request):
    form = AboutUsForm()
    if request.method == "POST":
        form = AboutUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about-us')

    context = {'form': form}
    html_template = loader.get_template('home/edit-about-us.html')
    return HttpResponse(html_template.render(context, request))


def update_about_us(request, pk):
    about_us = AboutUs.objects.get(id=pk)
    form = AboutUsForm(instance=about_us)
    print(pk)
    if request.method == "POST":
        form = AboutUsForm(request.POST, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('about-us')
    context = {'form': form}
    html_template = loader.get_template('home/edit-about-us.html')
    return HttpResponse(html_template.render(context, request))


def delete_about_us(request, pk):
    about_us = AboutUs.objects.get(id=pk)
    if request.method == 'POST':
        about_us.delete()
        return redirect('about-us')
    context = {'about_us': about_us}
    html_template = loader.get_template('home/edit-about-us.html')
    return HttpResponse(html_template.render(context, request))


def terms_of_use(request):
    context = {'segment': 'terms-of-use'}
    html_template = loader.get_template('home/terms-of-use.html')
    return HttpResponse(html_template.render(context, request))


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('')
            except:
                pass
    else:
        form = ContactForm()
    context = {'form': form}
    html_template = loader.get_template('home/contact-us.html')
    return HttpResponse(html_template.render(context, request))

def career(request):
    career = Career.objects.all()
    context = {'career': career}
    html_template = loader.get_template('home/career.html')
    return HttpResponse(html_template.render(context, request))

def job_detail(request, pk):
    career = Career.objects.get(id=pk)
    context = {'career': career}
    html_template = loader.get_template('home/job_detail.html')
    return HttpResponse(html_template.render(context, request))

def privacy_policy(request):
    privacy = PrivacyPolicy.objects.all()
    context = {'privacy': privacy}
    html_template = loader.get_template('home/privacy_policy.html')
    return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
def index(request):
    travel = ItineraryPlanner.objects.all()
    if request.method == "POST":
        planner_form = ItineraryPlannerForm(request.POST)
        category_form = ItineraryCategoryForm(request.POST)
        if planner_form.is_valid() and category_form.is_valid():
            print("%s" % planner_form, "%s" % category_form)

            if request.user.is_anonymous:
                category = category_form.save()
                planner = planner_form.save(commit=False)
                planner.user = None
                planner.category = category
                planner_form.save()
                print("The User Is >> >> >> >> %s" % request.user)

            elif request.user.is_authenticated:
                category = category_form.save()
                planner = planner_form.save(commit=False)  # here
                planner.user = request.user  # here
                planner.category = category
                planner.save()  # here
                print("The User Is >> >> >> >> %s" % request.user)

            return redirect('/')

    else:
        planner_form = ItineraryPlannerForm
        category_form = ItineraryCategoryForm

    context = {'planner_form': planner_form,
               'category_form': category_form,
               'travel': travel}
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
