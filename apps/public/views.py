#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from apps.core.views import verificar_sugeridos

# Create your views here.

def home(request):
	values = {}
	
	return render_to_response('public/index.html',values,context_instance=RequestContext(request))
