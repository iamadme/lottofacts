import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottofacts.settings")
import django
from xml.etree import ElementTree


django.setup()

from lottofactsapp.models import Lotto, Draw, Prizes

print Lotto.objects.all()
print Draw.objects.all()
print Prizes.objects.all()
