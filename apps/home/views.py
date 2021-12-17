# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import date,timedelta,datetime
from django.utils import timezone
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
from .models import FAQGeneral, FAQTravel, FAQ, AboutUs, Contact, Temp, ItineraryPlanner, Career, PrivacyPolicy, Review #users
from .forms import ContactForm, TempForm, AboutUsForm, ItineraryPlannerForm, ItineraryCategoryForm, FaqTravelForm, FaqGeneralForm,administrator_complaintsForm,complaintform,ReviewpForm #usersForm


######################################################################
#                          Views Functions                           #
######################################################################
@csrf_protect
def Monthly_Complaints_report(request):
    count_complaints = ContactUs.objects.filter(subject='2').count()
    count_general = ContactUs.objects.filter(subject='1').count()
    context={'page':Monthly_Complaints_report,'count_complaints':count_complaints,'count_general':count_general}
    html_template = loader.get_template('home/Monthly_Complaints_report.html')
    return HttpResponse(html_template.render(context, request))

def review_project(request):
    if request.method == "POST":
        form = ReviewpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReviewpForm()
    context = {'form': form}
    html_template = loader.get_template('home/Review.html')
    return HttpResponse(html_template.render(context, request))


@csrf_protect
def complaints(request):
    # complaint = ContactUs.objects.filter(subject='2')
    count = ContactUs.objects.filter(subject='2').count()
    count_handled = ContactUs.objects.filter(subject='2',complete='1').count()
    count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
    count_administrator = ContactUs.objects.filter(subject='2', complete='0',created_date = datetime.now() - timedelta(days=1)).count()

    context = {'asd': complaint,'count': count,'count_handled':count_handled,
               'count_unhandled':count_unhandled,'count_administrator':count_administrator}
    html_template = loader.get_template('home/complaints.html')
    return HttpResponse(html_template.render(context, request))

def complaint(request, pk):
    if pk == "total_complaints":
        complaint = ContactUs.objects.filter(subject='2')
        count = ContactUs.objects.filter(subject='2').count()
        count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
        count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
        count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                       created_date=datetime.now() - timedelta(days=1)).count()
        if request.POST:
            complete = request.POST["complete"]
            print(int(complete))
            check = ContactUs.objects.get(id=int(complete))
            check.complete = True
            check.save()
    elif pk == "complaints_handled":
        complaint = ContactUs.objects.filter(subject='2', complete=1)
        count = ContactUs.objects.filter(subject='2').count()
        count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
        count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
        count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                       created_date=datetime.now() - timedelta(days=1)).count()
        if request.POST:
            complete = request.POST["complete"]
            print(int(complete))
            check = ContactUs.objects.get(id=int(complete))
            check.complete = True
            check.save()
    elif pk == "unhandled_complaints":
        complaint = ContactUs.objects.filter(subject='2', complete=0)
        count = ContactUs.objects.filter(subject='2').count()
        count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
        count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
        count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                       created_date=datetime.now() - timedelta(days=1)).count()
        if request.POST:
            complete = request.POST["complete"]
            print(int(complete))
            check = ContactUs.objects.get(id=int(complete))
            check.complete = True
            check.save()
    elif pk == "system_administrator":
        complaint = ContactUs.objects.filter(subject='2', complete='0',created_date = datetime.now() - timedelta(days=1))
        count = ContactUs.objects.filter(subject='2').count()
        count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
        count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
        count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                       created_date=datetime.now() - timedelta(days=1)).count()
        if request.POST:
            complete = request.POST["complete"]
            print(int(complete))
            check = ContactUs.objects.get(id=int(complete))
            check.complete = True
            check.save()

        

    context = {'complaint': complaint,'count': count,
               'count_handled':count_handled,'count_unhandled':count_unhandled,'count_administrator':count_administrator}
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

def to_do_list(request):
    context = {'segment': 'to_do_list'}
    html_template = loader.get_template('home/to_do_list.html')
    return HttpResponse(html_template.render(context, request))

def recent_trips(request):
    context = {'segment': 'recent_trips'}
    html_template = loader.get_template('home/recent_trips.html')
    return HttpResponse(html_template.render(context, request))


def usage(request):
    data = "Current Data"

    #users = users.objects.all()

    #if request.method == 'POST':
      #  form = usersForm(request.POST)
        #if form.is_valid():
         #   form.save()
          #  return redirect('index')
   # else:
       # form = usersForm()

    context = {
        "data": data,


    }

    return render(request, 'home/for_usage.html', context)

######################################################################
#                     System Functions & Classes                     #
######################################################################
