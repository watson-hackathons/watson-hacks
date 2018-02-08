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

from django.conf.urls import url, include
from django.views.generic.edit import CreateView
from .views import films
from .views.films import SurveyCreateView, SurveyThanksCreateView, filmfor

from .models import Survey


urlpatterns = [
#    url(r'^teams$', ideas.teamlist, name='teamlist'),
    url (r'^$', SurveyCreateView.as_view(success_url = 'survey'), \
                           name="submitsurvey"),
    url (r'^survey$', SurveyThanksCreateView.as_view(success_url = 'survey'), \
                               name="thanks"),
    url(r'^filmfor$', filmfor, name='apifilmfor'),
]
