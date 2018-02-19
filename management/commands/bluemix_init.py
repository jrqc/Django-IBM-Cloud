# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand
import sys


class Command(BaseCommand):
    args = ''
    help = 'check'

    def add_arguments(self, parser):
        parser.add_argument('application_name', type=str)

    def handle(self, *args, **options):
        application_name = options['application_name']
        base = settings.BASE_DIR
        python_version = sys.version.split(' ')[0]
        project_name = settings.WSGI_APPLICATION.split(".")[0]
        try:
            f = open(base + "/Procfile", "w")
            f.write("web: python manage.py migrate && gunicorn {}.wsgi --log-file -".format(project_name))
            f.close()
        except IOError:
            print "IO"
        try:
            m = open(base + "/manifest.yml", "w")
            m.write(" applications: \n  - name: {} ".format(application_name))
            m.close()
        except Exception as e:
            print e

        try:
            v = open(base + "/runtime.txt", "w")
            v.write("python-{}".format(python_version))
            v.close()
        except Exception as E:
            print E

        self.stdout.write('Project successfully configured for: %s \n' % str(application_name))
