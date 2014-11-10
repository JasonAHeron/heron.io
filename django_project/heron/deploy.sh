#!/bin/sh
cd /home/django/django_project/heron
git pull origin master
service gunicorn restart
