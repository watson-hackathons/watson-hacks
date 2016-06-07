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

from django.db import models

# Create your models here.

class Hackathon(models.Model):
  location = models.CharField(max_length=100,  verbose_name="Location")
  event = models.CharField(max_length=100,  verbose_name="Event") 
  event_date = models.DateField(verbose_name="Event date")
  active = models.BooleanField(verbose_name="Submissions are active")
  def __str__(self):
    return self.event


class Team(models.Model):
  hackathon = models.ForeignKey(Hackathon, default=1)  
  name = models.CharField(max_length=100,  verbose_name="Team name")
  def __str__(self):
    return self.name

class TeamMember(models.Model):
  team = models.ForeignKey(Team)
  twitterID = models.CharField(max_length=50, verbose_name="Twitter ID")
  emailID = models.EmailField(verbose_name="Email", null=True, default=None)
  tell_me = models.BooleanField(verbose_name="Watson can tell me about me",default=False)
  def __str__(self):
    return self.twitterID

class TeamIdea(models.Model):
  team = models.ForeignKey(Team)
  idea = models.TextField(verbose_name="Team Idea")
  flow = models.TextField(verbose_name="Process Flow")
  data = models.TextField(verbose_name="Data Source")
  alchemyLanguage = models.BooleanField(verbose_name="Alchemy Language")
  conceptExpansion = models.BooleanField(verbose_name="Concept Expansion")
  conceptInsights = models.BooleanField(verbose_name="Concept Insights")
  dialog = models.BooleanField(verbose_name="Dialog")
  documentConversion = models.BooleanField(verbose_name="Document Conversion")
  languageTranslation = models.BooleanField(verbose_name="Language Translation")
  naturalLanguageClassifier = models.BooleanField(verbose_name="Natural Language Classifier")
  personalityInsights = models.BooleanField(verbose_name="Personality Insights")
  relationshipExtraction = models.BooleanField(verbose_name="relationshipExtraction")
  rankRetrieve = models.BooleanField(verbose_name="Rank and Retrieve")
  toneAnalyser = models.BooleanField(verbose_name="Tone Analyser")
  speechText = models.BooleanField(verbose_name="Speech to Text")
  textSpeech = models.BooleanField(verbose_name="Text to Speech")
  alchemyVision = models.BooleanField(verbose_name="Alchemy Vision")
  visualInsights = models.BooleanField(verbose_name="Visual Insights")
  visualRecognition = models.BooleanField(verbose_name="Visual Recognition")
  alchemyNews = models.BooleanField(verbose_name="AlchemyDataNews")
  tradeoffAnalytics = models.BooleanField(verbose_name="Tradeoff Analytics")
  
  def __str__(self):
    return self.idea


class TeamSubmission(models.Model):
  team = models.ForeignKey(Team)
  url = models.URLField(verbose_name="Application URL")
  gallery = models.BooleanField(verbose_name="App Gallery Interest", default=False)  
  def __str__(self):
    return self.url
