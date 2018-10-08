import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottofacts.settings")
import django
from xml.etree import ElementTree


django.setup()

from lottofactsapp.models import Lotto, Draw, Prizes

drawTypes = ["Lotto", "LottoPlus1", "LottoPlus2", "EuroMillions", "EuroMillionsPlus", "DailyMillion", "DailyMillionPlus", "Lotto_54321", "LottoPlus1_54321", "LottoPlus2_54321"]


resp = requests.get('https://resultsservice.lottery.ie/rest/GetResults?drawType=Lotto&lastNumberOfDraws=50')
if resp.status_code != 200:
  raise APIError('GET /rest/GetResults {}'.format(resp.status_code))

tree = ElementTree.fromstring(resp.content)

for child in tree.iter('DrawResult'):
  drawName = child.find('DrawName').text
  drawDate = child.find('DrawDate').text
  drawMessage = child.find('Message').text
  drawNumber = child.find('DrawNumber').text
  drawTopPrize = child.find('TopPrize').text
  drawResult = []
  drawBonus = []
  for resultNumArray in child.iter('Numbers'):
    for resultNum in resultNumArray.iter('DrawNumber'):
      if resultNum.find('Type').text == "Standard":
        drawResult.append(resultNum.find('Number').text)
      elif resultNum.find('Type').text == "Bonus":
        drawBonus.append(resultNum.find('Number').text)

  print("Name: %s, Date: %s, Number: %s, TopPrize: %s, Result: %s, Bonus: %s" % (drawName, drawDate, drawNumber, drawTopPrize, drawResult, drawBonus))
  for structure in child.iter('Structure'):
    for tier in structure.iter('Tier'):
      winners = tier.find('Winners').text
      match = tier.find('Match').text
      prizeType = tier.find('PrizeType').text
      prize = tier.find('Prize').text 
      print("Winners: %s, Match: %s, PrizeType: %s, Prize: %s" % (winners, match, prizeType, prize))
  

  
