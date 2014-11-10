#!/bin/sh
git pull origin master
service gunicorn restart
