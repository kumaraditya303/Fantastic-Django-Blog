# -*- coding: utf-8 -*-

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoblog.settings")

application = get_asgi_application()
