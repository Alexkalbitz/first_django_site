first_test
superuser
ukki - alexkalbitz@yahoo.de -superukki1122


PW

Heroku:
alkal@yahoo.de
H77mmsvs!!
inside CMD.exe
heroku login
Enter your Heroku credentials.
Email: alexkalbitz@yahoo.de
Password: ...

https://ancient-forest-16446.herokuapp.com/

to see the logs of my heroku apps
$ heroku logs --tail



immer runserver.py ausführen im Debug (im Debug modus sind breakpoints tödlich)

views.py brauch ich um sachen aus python in die html zu bekommen

templates/home.html for the new html sites

für return aus funktionen

variable, variable, variable..... = funktion()



'''schleife mit tricks drinnen für die views.py'''
ticks = testing.client.get_tick()
btclist = []
for tick in ticks:
    tick['blabla'] = 'so gibts extra infos{}db'.format(tick['coinTypePair'])
    if tick['coinTypePair'] == 'BTC':
        btclist.append(tick)

'''
liste=[(1516235280, 4.783e-05, 4.783e-05, 4.742e-05, 4.742e-05, 18.6716),(1516235340, 4.707e-05, 4.742e-05, 4.707e-05, 4.742e-05, 2443.6385)]
 so bekommt mans raus !!!!!!   1,2,3,4,5,6=liste[1]
'''

'''{'buy': 4.788e-05,
 'change': 8.8e-07,
 'changeRate': 0.0187,
 'coinType': 'QLC',
 'coinTypePair': 'BTC',
 'datetime': 1516235830000,
 'feeRate': 0.001,
 'high': 4.9e-05,
 'lastDealPrice': 4.788e-05,
 'low': 3.55e-05,
 'sell': 4.789e-05,
 'sort': 0,
 'symbol': 'QLC-BTC',
 'trading': True,
 'vol': 3758462.8653,
 'volValue': 154.68208981}'''



client.get_historical_klines_tv("KCS-BTC", Client.RESOLUTION_15MINUTES, "1 day ago UTC")
returns Data in the order of:
Open, High, Low, Close, Volume
example #a=[(1516482900, 0.00091215, 0.00091839, 0.00090499, 0.00091557, 3750.9021), (1516483800, 0.00091694, 0.00091837, 0.00091397, 0.00091825, 2565.6835),
a[0][0] == 1516482900


dictionarys

for market,klines in mydict.items():
    print(market,klines[:2])


#Pickle for Files (List and Dictionaries)
import pickle

a = ['test value','test value 2','test value 3']
a
['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb')

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'r')
# load the object from the file into var b
b = pickle.load(fileObject)
b
['test value','test value 2','test value 3']
a==b
True

with open("myfilename", 'wb') as file:
    pickle.dump(mystuff, file)

with open("myfilename", 'rb') as file:
    mystuff=pickle.load(file)

import json

# same as pickle

json.dumps(a, indent=4)





#get current working directory, where is your interpreter looking
import os
os.getcwd()
#to set the default for this left click right corner debug 'reiter' -> edit configuratuion -> 4th line (expand environment 'reiter') -> set the path it should try to run
'M:\\crypto\\geschäfte\\Tradingkucoin\\Cryptotrading'

testlist = [
    {
        'market': 'KCS-BTC',
        'mean_10': 5,
        'mean_20': 6,
    },
    {
        'market': 'KCS-BTC',
        'mean_10': 5,
        'mean_20': 6,
    },
    {
        'market': 'KCS-BTC',
        'mean_10': 5,
        'mean_20': 6,
    },
    {
        'market': 'KCS-BTC',
        'mean_10': 5,
        'mean_20': 6,
    },

]


def calc_mean_of_values(liste[])
return float


def get_start_time(hoursback)


def get_prices_since(market_records[], start_time)
return prices[]


def get_market_records(klinesdata{}, marketname)
return market_records


def get_means_of_market(klinesdata{}, marketname):
records = get_market_records()
prices = get_prices_since(records, start_time10)
mean10 = calc_mean_of_values(prices)
prices = get_prices_since(records, start_time20)
mean20 = calc_mean_of_values(prices)
data = {
           'market': 'KCS-BTC',
           'mean_10': mean10,
           'mean_20': mean20,
       },

return data


def get_market_mean_sum(klinesdata{}):
lst = []
for market in markets:
    data = get_means_of_market(klinesdata, market)
    lst.append[data]
return lst



ctrl+shift+f8
debugger exeption breakpoint



#---------- Path variable setzen --------
'''
set PATH=%PATH%;E:\Projects\Django-first\venv\Scripts\
set PATH=%PATH%;M:\Programme\PostgreSQL\10\bin
'''

python manage.py startapp appname

'''DATENBANK DATABASE DB MODELS MODEL MIGRATION ETC'''
# für neue datenbank modelle oder änderungen
django migration für datenbanken
python manage.py makemigrations kucoin_app
python manage.py migrate

#########DATENBANKEN
#-------Database and models stuff
https://docs.djangoproject.com/en/2.0/topics/db/models/
from .models import Person
#------get/Query all objects/models in table "Person"--------
Person.objects.all()
#-------create new personmodel
p=Person
p.first_name='klaus'
p.last_name='mueller'
#------save person to database
p.save()

#-----get shit
Person.objects.get(first_name='klaus')
a=Person.objects.all()[0]
klinemodel=Kline.objects.all()[0]
#oder
klinemodel=Kline.objects.all()
klinemodel[0].timestamp
#oder damit man ne liste hat die auch [-1] kann, geht bei Querys nicht
klinemodel = Kline.objects.all()
klinemodel_als_liste = list(klinemodel)
klinemodel_als_liste[-1].timestamp



#delete the whole Database DB

Kline.objects.all().delete()

#get latest timestamp
mod=Kline.objects.latest('timestamp')
mod.timestamp #OHNE KLAMMERN!!!!!!
Kline.objects.all().count() #zählen

from django.db.models import Max
Kline.objects.all().aggregate(Max('timestamp'))

>>> from django.db.models import Avg
>>> Kline.objects.all().aggregate(Avg('open'))



#Datetime Zeugs

datetime.strftime('%Y-%m-%d %H:%M:%S')
#tabelle für datetime darstellung
https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
time_24_hours_ago = datetime.datetime.now() - datetime.timedelta(days=1)
1_hour_ago= datetime.datetime.now() - datetime.timedelta(hours=1)






'''
def attach_utc_to_naive_datetime(dt):
    from django.utils.timezone import utc
    assert dt.tzinfo is None
    dt = dt.replace(tzinfo=utc)
    return dt
'''

scrapy mystuff

install pywin32

Lib\site-packages\pywin32_sytem32
copy the DLL to
Lib\site-packages\win32

scrapy runspider scraper.py

scrapy shell welt.de



###import stuff
#putting this code in the __init__ of a directory makes the import * viable for all python files in that folder
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]




in der DBMAIN hab ich ENVIRONMENT VARIABLES GESETZT ---> neben dem bedug käfer

in der views.py von cralwer geht das nicht


KANN SEIN DASS ES NIEMALS IN DER VIEWS DIREKT GEHT
EVTL MUSS ICH ALLE DJANGO SCRIPTS MIT RUNSERVER DEBUGGEN
DAMIT ER DIE APPS TATSÄLICH LÄDT.

UM NE MODELSLIST ZU BEKOMMEN:
from django.apps import apps

for app in apps.get_app_configs():
    print(app.verbose_name, ":")
    for model in app.get_models():
        print("\t", model)


#sending a POST request via script

import requests

URL = "http://127.0.0.1:8000/crawler/"
with requests.session() as s:
    s.get(URL)
    csrftoken = s.cookies.get_dict()['csrftoken']
    print(csrftoken)
    s.headers['X-CSRFToken'] = csrftoken
    payload={
        "name": 'value'
    }
    s.post(URL, data=payload)

###scrapy
from crochet import setup, wait_for
setup()

might be a solution to the spider problem