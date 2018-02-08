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
from django.db import models

# Create your models here.

class Genres(models.Model):
  genre = models.CharField(max_length=100,  verbose_name="Genre")
  def __str__(self):
    return self.genre

class Films(models.Model):
  title = models.CharField(max_length=100,  verbose_name="Film Title")
  genre = models.ForeignKey(Genres, default=1)
  def __str__(self):
    return self.title

class Survey(models.Model):
  GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Non Binary'))
  HEALTHCARE_CHOICES = (('public','Free at the point of use'),('private','Paid for privately'))
  DRUG_CHOICES = (('prison','Jail'),('rehab','Rehab'))
  EDUCATION_CHOICES = (('state','Paid for by the state'),('graduate', 'Paid for by a graduate tax'),('private','Paid for by the student'))
  film = models.ForeignKey(Films, default=1, verbose_name="Your favourite film")
  genre = models.ForeignKey(Genres, default=1, verbose_name="Your favourite film genre")
  age = models.IntegerField(verbose_name="Your age")
  children = models.IntegerField(verbose_name="How many children you have")
  gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='nonbinary', verbose_name="You see your self as")
  health = models.CharField(max_length=10, choices=HEALTHCARE_CHOICES, default='public', verbose_name="Healthcare should be")
  education = models.CharField(max_length=10, choices=EDUCATION_CHOICES, default='public', verbose_name="Tertiary education should be")
  drug = models.CharField(max_length=10, choices=DRUG_CHOICES, default='rehab', verbose_name="Drug users should be sent to")
  def __str__(self):
    return self.film.title + ' ' + self.genre.genre + ' ' + str(self.age)

class Personality(models.Model):
  film = models.ForeignKey(Films, default=1, verbose_name="Your favourite film")
  openness = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Personality Openness")
  consientiousness = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Personality Conscientiousness")
  extraversion = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Personality Extraversion")
  agreeableness = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Personality Agreeableness")
  emotionalrange = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Personality Emotional Range")
  challenge = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Challenge")
  closeness = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Closeness")
  curiosity = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Curiosity")
  excitement = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Excitement")
  harmony = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Harmony")
  ideal = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Ideal")
  liberty = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Liberty")
  love = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Love")
  practicality = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Practicaltiy")
  expression = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Expression")
  stability = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Stability")
  structure = models.DecimalField(max_digits=5, decimal_places=4, verbose_name="Needs Strucure")
  def __str__(self):
    return self.film.title + ' ' + str(self.openness) + ' ' + str(self.challenge)
