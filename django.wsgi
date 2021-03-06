import os
import sys

current_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(current_directory)
module_name = os.path.basename(current_directory)

sys.path.insert(0, parent_directory)
sys.path.insert(0, current_directory)

# os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % module_name
import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
