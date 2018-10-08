import requests
from xml.etree import ElementTree

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
  print("Name: %s, Date: %s, Number: %s, TopPrize: %s" % (drawName, drawDate, drawNumber, drawTopPrize))
  for structure in child.iter('Structure'):
    for tier in structure.iter('Tier'):
      winners = tier.find('Winners').text
      match = tier.find('Match').text
      prizeType = tier.find('PrizeType').text
      prize = tier.find('Prize').text 
      print("Winners: %s, Match: %s, PrizeType: %s, Prize: %s" % (winners, match, prizeType, prize))


  
#  print('{} {}'.format(todo_item['id'], todo_item['summary']))
