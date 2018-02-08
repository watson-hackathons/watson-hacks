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



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME' : 'ibmx_77818476d3b7f6c',
        'USER' : 'bc1387eee66200',
        'PASSWORD': 'c8692677',
        'HOST' : 'eu-cdbr-sl-lhr-01.cleardb.net',
        'PORT' : '3306',
    }
}

#"credentials": {
#                "jdbcUrl": "jdbc:mysql://eu-cdbr-sl-lhr-01.cleardb.net/ibmx_77818476d3b7f6c?user=bc1387eee66200&password=c8692677",
#                "uri": "mysql://bc1387eee66200:c8692677@eu-cdbr-sl-lhr-01.cleardb.net:3306/ibmx_77818476d3b7f6c?reconnect=true",
#                "name": "ibmx_77818476d3b7f6c",
#                "hostname": "eu-cdbr-sl-lhr-01.cleardb.net",
#                "port": "3306",
#                "username": "bc1387eee66200",
#                "password": "c8692677"
#            },
