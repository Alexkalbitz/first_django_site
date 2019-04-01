from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .models import Newsdatabase
import datetime


'#http request for Django DB'


def attach_utc_to_naive_datetime(dt):
    from django.utils.timezone import utc
    assert dt.tzinfo is None
    dt = dt.replace(tzinfo=utc)
    return dt


def news_to_db(file):
    #Getting Datetime to save for the Database
    date = datetime.datetime.utcnow()
    dateutc = attach_utc_to_naive_datetime(date)
    for n in file:
        db = Newsdatabase()
        headline = n
        url = file[n]
        homepage = file[n].split('/')[2]
        result = homepage.replace("www.", "")
        check = Newsdatabase.objects.filter(url__icontains=url)
        if check.count() == 0:
            db.source = result
            db.url = url
            db.headline = headline
            db.dateadded = dateutc
            db.save()
            print('just saved:', headline)


@ensure_csrf_cookie
def crawler(request):
    #check if theres a POST request
    if request.method.lower() == 'post':
        #Check the Password or the POST data
        if request.POST.get('password') == '123456':
            #get the json
            my_json = request.POST.get('data')
            #convert the json back to a dict
            data = json.loads(my_json)
            print('everything working till here')
            #save the json data to DB
            news_to_db(data)
        else:
            print('Failed POST to /crawler')
            pass
    else:
        return render(request, 'news/crawler.html')


def index(request):
    data = 'whatever, this can be anything'
    query = request.GET.get('this has to be set in the html')
    template = 'news/index.html'
    context = {
        'data': data,
    }
    return render(request, template, context)


def home(request):
    data = 'whatever, this can be anything'
    query = request.GET.get('this has to be set in the html')
    template = 'news/home.html'
    context = {
        'data': data,
    }
    return render(request, template, context)


def news(request):
    data = 'whatever, this can be anything'
    template = 'news/news.html'
    get = request.GET.get('search_field')

    #check if a search via GET has been done
    if get is None:
        get = ''
        query = Newsdatabase.objects.all().order_by('-dateadded')
    if len(get) > 0:
        print(get)
        q = Q(headline__icontains=get) | Q(url__icontains=get)
        q = q | Q(source__icontains=get)
        query = Newsdatabase.objects.filter(q).order_by('-dateadded')
        if len(query) == 0:
            search_result = 'Your search for "{}" did not yield any results'.format(get)
        else:
            search_result = 'You searched for: "{}" '.format(get)
    else:
        search_result = 'No search has been done!'
        query = Newsdatabase.objects.all().order_by('-dateadded')
    # Paginator
    page = request.GET.get('page')
    paginator = Paginator(query, 20)
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        query = paginator.page(1)
    except EmptyPage:
        query = paginator.page(paginator.num_pages)

    context = {
        'get': get,
        'data': data,
        'search_result': search_result,
        'news': query,
    }
    return render(request, template, context)
