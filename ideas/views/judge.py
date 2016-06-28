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

from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class FormLogin(forms.Form):
  username = forms.CharField(label = 'ID')
  password = forms.CharField(label = 'Key', widget = forms.PasswordInput)

  def clean(self):
    cleanedData = super(FormLogin, self).clean()
    username = cleanedData.get('username')
    password = cleanedData.get('password')
    if not authenticate(username=username, password=password):
      raise forms.ValidationError('Incorrect ID / Key combination')
    return cleanedData

def judgelogin(request):
  if request.POST:
    form = FormLogin(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        if request.GET.get('next') is not None:
          return redirect(request.GET['next'])
  else:
    form = FormLogin()
  return render(request, 'judges/login.html', {'form': form})

def judgelogout(request):
  logout(request)
  return redirect('hackideas:judge')

@login_required
def judge(request):
  return render(request, 'judges/judge.html')
