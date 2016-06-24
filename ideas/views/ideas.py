# -*- coding: utf-8 -*-
# Copyright 2016 IBM Corp. All Rights Reserved.
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

from ideas.models import Team, TeamMember, TeamIdea, Hackathon, TeamSubmission

import json

import logging
logger = logging.getLogger(__name__)


class TeamListView(generic.ListView):
  template_name = 'ideas/teamlist.html'
  model = Team
  context_object_name = 'teamlist'


class TeamForm(forms.ModelForm):
  hackathon = forms.ModelChoiceField(queryset=Hackathon.objects.filter(active=True))
  class Meta:
    model = Team
    fields = ['hackathon', 'name']


class TeamCreateView(generic.CreateView):
  template_name = 'ideas/registerteam.html'
  model = Team
  form_class = TeamForm


class TeamMemberListView(generic.ListView):
  template_name = 'ideas/teammemberlist.html'
  model = TeamMember
  context_object_name = 'teammemberlist'

  def get_queryset(self):
    return TeamMember.objects.order_by('team')

class TeamMemberForm(forms.ModelForm):
  team = forms.ModelChoiceField(queryset=Team.objects.filter(hackathon__active=True))
  class Meta:
    model = TeamMember
    fields = ['team', 'twitterID', 'emailID']

class TeamMemberCreateView(generic.CreateView):
  template_name = 'ideas/registerteammember.html'
  model = TeamMember
  form_class = TeamMemberForm

class TeamIdeaListView(generic.ListView):
  template_name = 'ideas/teamidealist.html'
  model = TeamIdea
  context_object_name = 'teamidealist'

  def get_queryset(self):
    return TeamIdea.objects.order_by('team__name')

class AllIdeasListView(generic.ListView):
  template_name = 'ideas/allidealist.html'
  model = TeamIdea
  context_object_name = 'teamidealist'
  paginate_by = 10

  def get_queryset(self):
    return TeamIdea.objects.order_by('team__hackathon__event','team__name')

class TeamIdeaForm(forms.ModelForm):
  team = forms.ModelChoiceField(queryset=Team.objects.filter(hackathon__active=True))
  class Meta:
    model = TeamIdea
    fields = ['team', 'idea',  'flow', 'data', \
            'alchemyLanguage', 'conceptExpansion', 'conceptInsights', \
            'dialog', 'documentConversion', 'languageTranslation', \
            'naturalLanguageClassifier', 'personalityInsights', \
            'relationshipExtraction', 'rankRetrieve', 'toneAnalyser', \
            'speechText', 'textSpeech', 'alchemyVision' , 'visualInsights', \
            'visualRecognition', 'alchemyNews', 'tradeoffAnalytics' ]

  def clean(self):
    ts = self.cleaned_data["team"];
    t = Team.objects.filter(name=ts)[:1].get()
    activeEvent = t.hackathon.active

    if not activeEvent:
      msg = "The {0} hackathon at {1} has been archived, and no registrations are allowed".format(
                                                                                        t.hackathon.event,
                                                                                        t.hackathon.location)
      raise forms.ValidationError(msg)

    return super(TeamIdeaForm, self).clean()

class TeamIdeaCreateView(generic.CreateView):
  template_name = 'ideas/registerteamidea.html'
  model = TeamIdea
  form_class = TeamIdeaForm


class TeamIdeaUpdateForm(forms.ModelForm):
  class Meta:
    model = TeamIdea
    fields = ['team', 'idea',  'flow', 'data', \
            'alchemyLanguage', 'conceptExpansion', 'conceptInsights', \
            'dialog', 'documentConversion', 'languageTranslation', \
            'naturalLanguageClassifier', 'personalityInsights', \
            'relationshipExtraction', 'rankRetrieve', 'toneAnalyser', \
            'speechText', 'textSpeech', 'alchemyVision' , 'visualInsights', \
            'visualRecognition', 'alchemyNews', 'tradeoffAnalytics' ]

  def clean(self):
    ts = self.cleaned_data["team"];
    t = Team.objects.filter(name=ts)[:1].get()
    activeEvent = t.hackathon.active

    if not activeEvent:
      msg = "The {0} hackathon at {1} has been archived, and no updates are allowed".format(
                                                                                        t.hackathon.event,
                                                                                        t.hackathon.location)
      raise forms.ValidationError(msg)

    return super(TeamIdeaUpdateForm, self).clean()

class TeamIdeaUpdateView(generic.UpdateView):
  template_name = 'ideas/editteamidea.html'
  model = TeamIdea
  form_class = TeamIdeaUpdateForm

  def get_context_data(self, **kwargs):
    context = super(TeamIdeaUpdateView, self).get_context_data(**kwargs)
    t = self.object.team
    s = TeamSubmission.objects.filter(team = t)
    context['submissions'] = s
    return context


class TeamSubsListView(generic.ListView):
  template_name = 'ideas/teamsubmissionlist.html'
  model = TeamSubmission
  context_object_name = 'teamsubmissionlist'

  def get_queryset(self):
    return TeamSubmission.objects.order_by('team__name')

class TeamSubsForm(forms.ModelForm):
  team = forms.ModelChoiceField(queryset=Team.objects.filter(hackathon__active=True))
  class Meta:
    model = TeamSubmission
    fields = ['team', 'url', 'gallery']


class TeamSubsCreateView(generic.CreateView):
  template_name = 'ideas/registerteamsubmission.html'
  model = TeamSubmission
  form_class = TeamSubsForm

class TeamSubmissionUpdateView(generic.UpdateView):
  template_name = 'ideas/editteamsubmission.html'
  model = TeamSubmission
  fields = ['team', 'url', 'gallery']
