import pyautogui as pa
from PIL import Image

def checkmp(mp):
  pixels = mp.load()
  width, height = mp.size

  all_pixel = {'blue': 0, 'white': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      print(cpixel)
      if cpixel[0] > 200:
        all_pixel['white'] = all_pixel['white'] + 1
      else:
        all_pixel['blue'] = all_pixel['blue'] + 1
  return getPercent(all_pixel['blue'], all_pixel['white'])

def checkhp(hp):
  pixels = hp.load()
  width, height = hp.size

  all_pixel = {'red': 0, 'white': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      if cpixel[2] > 200:
        all_pixel['white'] = all_pixel['white'] + 1
      else:
        all_pixel['red'] = all_pixel['red'] + 1
  return getPercent(all_pixel['red'], all_pixel['white'])


def checkBattle():
  battle = pa.screenshot(region=(551, 25, 29, 1))
  battleCondition = checkBattleFrame(battle)
  if battleCondition > 80:
    return True
    print('inbattle: {inbattle}'.format(inbattle=inbattle))
  else:
    return False
    print('inbattle: {inbattle}'.format(inbattle=inbattle))


def checkBattleFrame(battle):
  pixels = battle.load()
  width, height = battle.size

  all_pixel = {'correct': 0, 'incorrect': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      print(cpixel)
      if cpixel[0] < 20 and cpixel[2] > 200:
        all_pixel['correct'] = all_pixel['correct'] + 1
      else:
        all_pixel['incorrect'] = all_pixel['incorrect'] + 1
  print(all_pixel)
  sum = all_pixel['correct'] + all_pixel['incorrect']
  return int((all_pixel['correct'] / sum) * 100)

def getPercent(numa, numb):
  sum = numa + numb
  return int((numa / sum) * 100)

def getDialogArea(dialog):
  pixels = dialog.load()
  width, height = dialog.size

  all_pixel = {'yellow': 0, 'incorrect': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      if cpixel[0] > 200 and cpixel[1] > 100 and cpixel[2] > 75:
        all_pixel['yellow'] = all_pixel['yellow'] + 1
      else:
        all_pixel['incorrect'] = all_pixel['incorrect'] + 1
  return getPercent(all_pixel['yellow'], all_pixel['incorrect'])

def getPetArea(dialog):
  pixels = dialog.load()
  width, height = dialog.size

  all_pixel = {'correct': 0, 'incorrect': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      if cpixel[0] > 220 and cpixel[1] > 147 and cpixel[2] > 55:
        all_pixel['correct'] = all_pixel['correct'] + 1
      else:
        all_pixel['incorrect'] = all_pixel['incorrect'] + 1
  return getPercent(all_pixel['correct'], all_pixel['incorrect'])


thisframeMp = pa.screenshot(region=(763, 25, 37, 342))
print(getPetArea(thisframeMp))

#763 25
#800 367

#F0A747 => 240 167 75