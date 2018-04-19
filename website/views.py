# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'website/home.html')

def contact(request):
    return render(request, 'website/basic.html', {'content':['email ', 'nikoaditya6@gmail.com']})

