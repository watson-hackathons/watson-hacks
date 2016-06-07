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

from django.conf.urls import url, include
from django.views.generic.edit import CreateView
from .views import ideas
from .views.ideas import TeamListView, TeamCreateView
from .views.ideas import TeamMemberListView, TeamMemberCreateView
from .views.ideas import TeamIdeaListView, TeamIdeaCreateView, TeamIdeaUpdateView
from .views.ideas import TeamSubsListView, TeamSubsCreateView, TeamSubmissionUpdateView
from .views.ideas import AllIdeasListView

from .models import Team


urlpatterns = [
#    url(r'^teams$', ideas.teamlist, name='teamlist'),     
    url(r'^teams$', TeamListView.as_view(), name='teamlist'), 
    url (r'^create_team$', TeamCreateView.as_view(success_url = 'teams'), \
                           name="registerteam"), 

    url(r'^teammembers$', TeamMemberListView.as_view(), name='teammemberlist'),     
    url (r'^create_teammember$', TeamMemberCreateView.as_view(success_url = 'teammembers'), \
                           name="registerteammember"),

    url(r'^teamideas$', TeamIdeaListView.as_view(), name='teamidealist'),  
    url(r'^tutti$', AllIdeasListView.as_view(), name='allidealist'), 

    url (r'^create_teamidea$', TeamIdeaCreateView.as_view(success_url = 'teamideas'), \
                           name="registerteamidea"), 


	  url (r'^editteamidea_(?P<pk>\d+)$', \
		         TeamIdeaUpdateView.as_view(success_url="teamideas"), \
		         name="editteamidea"),

    url(r'^teamsubmissions$', TeamSubsListView.as_view(), name='teamsubmissionlist'),         

    url (r'^create_teamsubmission$', TeamSubsCreateView.as_view(success_url = 'teamsubmissions'), \
                           name="registerteamsubmission"), 


    url (r'^editteamsubmission_(?P<pk>\d+)$', \
             TeamSubmissionUpdateView.as_view(success_url="teamsubmissions"), \
             name="editteamsubmission"),    

]