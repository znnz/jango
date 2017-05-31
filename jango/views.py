import datetime
import sqlite3
import sys

from django.conf import settings
from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse


def home(request):
    dt = datetime.datetime.now()
    html = '''
<html><body><h1>From django</h1>
<p>Time now: %s.
</body></html>''' % (dt,)
    return HttpResponse(html)


def listproducts(request):
    connection = None
    data = dict()
    data['title'] = "List of products"
    try:
        connection = sqlite3.connect(settings.BASE_DIR+'/mydatabase.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT Id,Name FROM Product")
            data['products'] = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if connection:
            connection.close()
    html = get_template('listproducts.html').render(data)
    return HttpResponse(html)

def product(request, code):
    connection = None
    data = dict()
    data['title'] = 'Product details: '+code
    try:
        connection = sqlite3.connect(settings.BASE_DIR+'/mydatabase.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Product WHERE Id=:Id", {'Id':code})
            data['products'] = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if connection:
            connection.close()
    html = get_template('product.html').render(data)
    return HttpResponse(html)