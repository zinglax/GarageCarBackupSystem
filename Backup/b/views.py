from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict

import ultrasonic

# Dictionary to add objects passed to the through to the HTML
script_args = {}
script_args['theme'] = "a"
    

def home(request):

  u = ultrasonic.UltraSonicSensor(24, 25, "BCM")

  script_args['distance'] = u.read()


  return render_to_response("b/home.html", script_args)
