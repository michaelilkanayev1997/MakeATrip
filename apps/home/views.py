# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import date, timedelta, datetime
import datetime
from django.db.models import Count
from django.views.decorators.csrf import csrf_protect
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .models import *
from .forms import *
from .google_maps.places import *
import pprint


######################################################################
#                          Views Functions                           #
######################################################################
def system_integrity_check(request):
    now = datetime.now()
    earlier = now - timedelta(days=7)
    maximum_days = now - timedelta(days=1000)

    count = ContactUs.objects.filter(subject='2').count()
    count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
    count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
    count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                   created_date__range=(maximum_days, earlier)).count()

    context = {'asd': complaint, 'count': count, 'count_handled': count_handled,
               'count_unhandled': count_unhandled, 'count_administrator': count_administrator}
    html_template = loader.get_template('home/system_integrity_check.html')
    return HttpResponse(html_template.render(context, request))


def monthly_inquiries_report(request):
    total, count_total, total_list = ContactUs.objects.all(), 0, []
    complaints, count_complaints, complaints_list = ContactUs.objects.filter(subject='2'), 0, []
    general, count_general, general_list = ContactUs.objects.filter(subject='1'), 0, []

    month = request.POST.get('month')

    if month:
        for report in total:
            if str(report.created_date)[0:7] == month:
                total_list.append(report)
        for report in complaints:
            if str(report.created_date)[0:7] == month:
                complaints_list.append(report)
        for report in general:
            if str(report.created_date)[0:7] == month:
                general_list.append(report)

    context = {'total': total, 'complaints': complaints,
               'general': general, 'total_list': total_list,
               'complaints_list': complaints_list, 'general_list': general_list, 'month': month}
    html_template = loader.get_template('home/monthly_inquiries_report.html')
    return HttpResponse(html_template.render(context, request))


def review_project(request):
    feedback = Review.objects.all()

    if request.method == "POST":
        form = ReviewpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReviewpForm()
    context = {'form': form, 'page': Review, 'feedback': feedback}
    html_template = loader.get_template('home/Review.html')
    return HttpResponse(html_template.render(context, request))


def complaints(request):
    now = datetime.now()
    earlier = now - timedelta(days=7)
    maximum_days = now - timedelta(days=1000)

    count = ContactUs.objects.filter(subject='2').count()
    count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
    count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
    count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                   created_date__range=(maximum_days, earlier)).count()

    context = {'asd': complaint, 'count': count, 'count_handled': count_handled,
               'count_unhandled': count_unhandled, 'count_administrator': count_administrator}
    html_template = loader.get_template('home/complaints.html')
    return HttpResponse(html_template.render(context, request))


def complaint(request, pk):
    now = datetime.now()
    earlier = now - timedelta(days=7)
    maximum_days = now - timedelta(days=1000)
    if pk == "total_complaints":
        complaint = ContactUs.objects.filter(subject='2')
        count = ContactUs.objects.filter(subject='2').count()
        count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
        count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
        count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                       created_date__range=(maximum_days, earlier)).count()
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
                                                       created_date__range=(maximum_days, earlier)).count()
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
                                                       created_date__range=(maximum_days, earlier)).count()
        if request.POST:
            complete = request.POST["complete"]
            print(int(complete))
            check = ContactUs.objects.get(id=int(complete))
            check.complete = True
            check.save()
    elif pk == "system_administrator":

        complaint = ContactUs.objects.filter(subject='2', complete='0', created_date__range=(maximum_days, earlier))
        count = ContactUs.objects.filter(subject='2').count()
        count_handled = ContactUs.objects.filter(subject='2', complete='1').count()
        count_unhandled = ContactUs.objects.filter(subject='2', complete='0').count()
        count_administrator = ContactUs.objects.filter(subject='2', complete='0',
                                                       created_date__range=(maximum_days, earlier)).count()
        if request.POST:
            complete = request.POST["complete"]
            print(int(complete))
            check = ContactUs.objects.get(id=int(complete))
            check.complete = True
            check.save()

    context = {'complaint': complaint, 'count': count,
               'count_handled': count_handled, 'count_unhandled': count_unhandled,
               'count_administrator': count_administrator}
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
    all_travels = ItineraryPlanner.objects.all()
    if request.method == "POST":
        planner_form = ItineraryPlannerForm(request.POST)
        category_form = ItineraryCategoryForm(request.POST)
        if planner_form.is_valid() and category_form.is_valid():
            if request.user.is_anonymous:
                category = category_form.save()
                planner = planner_form.save(commit=False)
                planner.user = None
                planner.category = category
                planner_form.save()

            elif request.user.is_authenticated:
                category = category_form.save()
                planner = planner_form.save(commit=False)
                planner.user = request.user
                planner.category = category
                planner.save()

            return redirect('/')

    else:
        planner_form = ItineraryPlannerForm
        category_form = ItineraryCategoryForm

    context = {'planner_form': planner_form,
               'category_form': category_form,
               'travel': all_travels}
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


def system_usages(request):
    admin = 0
    user = 0
    print(request.POST.get('month'))
    month = request.POST.get('month')

    # 2021-12-15 20:03:05.157077+00:00
    admins = User.objects.filter(is_superuser=True)
    for obj in admins:
        if str(obj.last_login)[0:7] == month:
            admin += 1
    users = User.objects.filter(is_superuser=False)
    for obj in users:
        if str(obj.last_login)[0:7] == month:
            user += 1
    print('admins', admin)
    print('users', user)

    context = {
        "lable": ['Users', 'Admins'],
        "data": [user, admin],
    }

    return render(request, 'home/system_usages.html', context)


def system_usages_by_month(request, pk):
    admins = User.objects.filter(is_superuser=True)
    users = User.objects.filter(is_superuser=False)

    lable = [admins, users]
    data = [admins.count(), users.count()]
    context = {
        "lable": lable,
        "data": data,
    }
    return render(request, 'home/system_usages.html', context)


def report_most_popular(request):
    destination = ItineraryPlanner.objects.values('destination').annotate(Number=Count('destination')).filter(
        Number__gt=1)

    lable = [destination]
    data = [destination]
    context = {
        "lable": lable,
        "data": data,
        "destination": destination,
    }
    html_template = loader.get_template('home/report_most_popular.html')
    return HttpResponse(html_template.render(context, request))


def employees_report(request):
    admins = User.objects.filter(is_superuser=True)

    lable = [admins]
    data = [admins]
    context = {
        "lable": lable,
        "data": data,
        "admins": admins,
    }
    return render(request, 'home/employees_report.html', context)


def call_google_api():
    pass
    # gpc = GooglePlaces('Eilat', 'campground')
    # gpc.search_places_by_coordinate()
    # gpc.get_data()
    # print((gpc.get_name()))


def places_data_processing():
    culture = ['art_gallery', 'hindu_temple', 'aquarium', 'church', 'museum']
    parks = ['amusement_park', 'campground', 'park', 'amusement_park', 'aquarium', 'zoo']
    calm = ['movie_theater', 'night_club', 'spa', 'stadium', 'bowling_alley']
    shopping = ['shoe_store', 'shopping_mall', 'clothing_store', 'jewelry_store']
    food = ['bakery', 'cafe', 'bar', 'restaurant']
    category_list = {'culture': culture, 'parks': parks, 'calm': calm, 'shopping': shopping, 'food': food}


def get_places_data(user):
    category_check = {'culture': None, 'parks': None, 'calm': None, 'shopping': None, 'food': None}
    travel = ItineraryPlanner.objects.filter(user_id=user)
    print(travel.values_list('destination', 'start_date', 'end_date').first())
    category_id = travel.values_list('category').first()[0]
    category = ItineraryCategory.objects.filter(id=category_id).values_list('culture', 'parks', 'calm',
                                                                            'shopping', 'food').first()
    for key, cat in zip(category_check, category):
        category_check[key] = cat
    print(category_check)


def trip(request):
    #get_places_data(request.user)
    context = {'segment': 'terms-of-use'}
    html_template = loader.get_template('home/trip.html')
    return HttpResponse(html_template.render(context, request))


def report_analysis(request):
    context = {}
    html_template = loader.get_template('home/report_analysis.html')
    return HttpResponse(html_template.render(context, request))

######################################################################
#                     System Functions & Classes                     #
######################################################################
