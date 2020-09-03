from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render_to_response, render
from django.shortcuts import redirect
from django.db import connection
from django.db.models import Count, Avg, Sum
from django.utils.timezone import utc
from django.db.models import Q
from django.contrib.auth import logout, authenticate, login as auth_login
#from django_openid_auth.models import UserOpenID
#from django_openid_auth.views import parse_openid_response
from django.core.serializers.json import DjangoJSONEncoder

import urllib, json, glob, os, math, random
from tf2tags.models import *
from datetime import *
from datetime import timedelta as timedelta
from random import shuffle
import time
import tf2tags.tf2 as tf2
import hmac
import hashlib
import base64
import urllib

ADMINS      = ["76561198041892999"] #criticalflaw
ADS         = False #Adsense
TRACKING    = False #Analytics
SPYCHECK    = False #Anonymous submissions

# Setup the slur filter.
REV_SLURS   = ["reggin", "sreggin", "toggaf", "stoggaf", "gaf", "sgaf", "tnuc", "stnuc", "hctib", "sehctib", "regg1n", "sregg1n", "t0ggaf", "st0ggaf"]
SLURS = []
for slur in REV_SLURS:
    SLURS.append(slur[::-1])
tf = tf2.TF()

ROOT	= "/var/www/html/tf2tags/"
URL 	= "0.0.0.0:8000/"	# "http://tf2tags.com/"
