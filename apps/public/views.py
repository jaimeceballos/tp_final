#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404

# Create your views here.

def home(request):

	return render_to_response('public/index.html',{},context_instance=RequestContext(request))
