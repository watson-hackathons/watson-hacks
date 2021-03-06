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

# Import all settings from base.py
from .base import *

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import json
from django.core.exceptions import ImproperlyConfigured
from hacks.utils.vcap import get_vcap_settings

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

db_creds = get_vcap_settings('postgresql')

if db_creds:
  db_host = str(db_creds['hostname'])	
  db_user = str(db_creds['username'])	
  db_pass = str(db_creds['password'])	
  db_port = str(db_creds['port'])	
  db_name = str(db_creds['name'])	
else:
  error_msg = "Could not find database credentials"
  raise ImproperlyConfigured(error_msg)
  	

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name, 
        'USER' : db_user,		
        'PASSWORD' : db_pass, 		
        'HOST' : db_host,  		
        'PORT' : db_port, 		
    }
}
