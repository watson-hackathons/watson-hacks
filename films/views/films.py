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

from films.models import Genres, Films, Survey, Personality

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


class FormAPI(forms.Form):
  openness = forms.DecimalField(required=False)
  consientiousness = forms.DecimalField(required=False)
  extraversion = forms.DecimalField(required=False)
  agreeableness = forms.DecimalField(required=False)
  emotionalrange = forms.DecimalField(required=False)
  challenge = forms.DecimalField(required=False)
  closeness = forms.DecimalField(required=False)
  curiosity = forms.DecimalField(required=False)
  excitement = forms.DecimalField(required=False)
  harmony = forms.DecimalField(required=False)
  ideal = forms.DecimalField(required=False)
  liberty = forms.DecimalField(required=False)
  love = forms.DecimalField(required=False)
  practicality = forms.DecimalField(required=False)
  expression = forms.DecimalField(required=False)
  stability = forms.DecimalField(required=False)
  structure = forms.DecimalField(required=False)

def runQuery(field, value):
  replyArray = []

  filtrationGTE = field + '__gte'
  filtrationLTE = field + '__lte'

  pHigh = Personality.objects.filter(**{ filtrationGTE: value }).order_by(field).first()
  if pHigh is not None:
    rowHigh = {}
    rowHigh['film'] = pHigh.film.title
    rowHigh['score'] = str(getattr(pHigh, field, 0))
    replyArray.append(rowHigh)

  pLow = Personality.objects.filter(**{ filtrationLTE: value }).order_by(field).last()
  if pLow is not None:
    rowLow = {}
    rowLow['film'] = pLow.film.title
    rowLow['score'] = str(getattr(pLow, field, 0))
    replyArray.append(rowLow)

  return replyArray

def prepareQuery(queryData):
  data = {}
  for q in queryData:
    data[q] = runQuery(q, queryData[q])
  reply = {"data": data}
  return reply


@csrf_exempt
def filmfor(request):
  results = {}
  theData = {"error":"If you see this message then something has gone badly wrong"}

  validRequest = False
  logger.info("Checking request method")
  if request.method == "GET":
    logger.info("Request is a GET")
    theData = {"error":"Only POST is supported for this API"}
    validRequest = False

  if request.method == "POST":
    logger.info("Request is a POST")
    queryFor = {}
    form = FormAPI(request.POST)
    if form.is_valid():
      for d in ['openness', 'consientiousness', 'extraversion',
        'agreeableness', 'emotionalrange', 'challenge', 'closeness',
        'curiosity', 'excitement', 'harmony', 'ideal', 'liberty',
        'love', 'practicality', 'expression', 'stability',
        'structure']:
        v = form.cleaned_data[d]
        if v is not None:
          queryFor[d] = v
      theData = prepareQuery(queryFor)
      validRequest = True
    else:
      logger.info("The form is not valid")

  results["results"] = theData
  return HttpResponse(json.dumps(results), content_type="application/json")
