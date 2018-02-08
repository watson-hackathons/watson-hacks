# -*- coding: utf-8 -*-
# Copyright 2018 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from films.models import Genres, Films, Survey

import json

import logging
logger = logging.getLogger(__name__)


class SurveyForm(forms.ModelForm):
  film = forms.ModelChoiceField(queryset=Films.objects.order_by('genre__genre'))
  class Meta:
    model = Survey
    fields = ['film', 'genre', 'age',  'children', \
            'gender', 'health', 'education', 'drug' ]

class SurveyCreateView(generic.CreateView):
  template_name = 'films/submitsurvey.html'
  model = Survey
  form_class = SurveyForm

class SurveyThanksCreateView(generic.CreateView):
  template_name = 'films/thanks.html'
  model = Survey
  form_class = SurveyForm
