#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Fri Sep 08 2017
# File: TencentFinance.py
# 
# Description: 
#
import sys
import os
import django
import io

sys.path.append('../YBRestApi') # 具体路径
os.environ['DJANGO_SETTINGS_MODULE'] = 'RestApi.settings'
django.setup()
