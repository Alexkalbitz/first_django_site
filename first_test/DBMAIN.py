import django
django.setup()

from crawler.models import Newsdatabase
import os
import pickle
import datetime


filenamelist=['weltsave.p','jungefreiheitsave.p']
#filename='M:\\crypto\\geschäfte\\first_django_site\\first_test\\crawler\\mytest\\mytest\\spiders\\jungefreiheitsave.p'
filepath='M:\\crypto\\geschäfte\\first_django_site\\first_test\\crawler\\mytest\\mytest\\spiders\\'
#filename='M:\\crypto\\geschäfte\\first_django_site\\first_test\\crawler\\mytest\\mytest\\spiders\\test.p'


print

def spider_saves_to_db():
    for n in filenamelist:
        file=filepath+n
        with open(file, 'rb') as data:
            mystuff = pickle.load(data)
            news_to_db(mystuff)




def news_to_db(file):
    date = datetime.datetime.utcnow()
    dateutc=attach_utc_to_naive_datetime(date)
    print(dateutc.isoformat(timespec='minutes'))
    for n in file:
        db = Newsdatabase()
        headline = n
        url = file[n]
        homepage=file[n].split('/')[2]
        if homepage.endswith('.de') == True:
            db.source = homepage
            db.url = url
            db.headline = headline
            db.dateadded = dateutc
            db.save()
            print('just saved:', headline)

        else:
            print('ERROR IN URL!!!!: {}'.format(url))




def attach_utc_to_naive_datetime(dt):
    from django.utils.timezone import utc
    assert dt.tzinfo is None
    dt = dt.replace(tzinfo=utc)
    return dt

#a=Newsdatabase
#a.objects.all().delete()
#news_to_db(mystuff)
spider_saves_to_db()
print
