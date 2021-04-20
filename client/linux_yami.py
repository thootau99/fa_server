import pyautogui as pa
import keyboard
import threading
import time
import client
import atexit
from random import shuffle
id = None
previousHpMp = []
baseHPy = 32
baseMPy = 44
baseX = 21
p = True
DIALOG_LOCK = False
    # 130 420
    # 203 367
    # 262 312
    # 351 249
    # 425 191
    # 72 353
    # 138 311
    # 220 249
    # 290 187
    # 359 139
locate = [(130, 420), (203,367), (262,312), (351,249), (425,191), (72,353),(138,311), (220, 249), (290,187), (359,139)]

def checkmp(mp):
  pixels = mp.load()
  width, height = mp.size

  all_pixel = {'blue': 0, 'white': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      avg = (cpixel[0] + cpixel[1] + cpixel[2]) / 3
      if cpixel[2] > 200 and cpixel[0] < 80:
        all_pixel['blue'] = all_pixel['blue'] + 1
      elif avg > 200:
        all_pixel['white'] = all_pixel['white'] + 1
      elif avg < 60:
        return 200
  
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

def checkBattleFrame(battle):
  pixels = battle.load()
  width, height = battle.size

  all_pixel = {'correct': 0, 'incorrect': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      if cpixel[0] < 20 and cpixel[2] > 200:
        all_pixel['correct'] = all_pixel['correct'] + 1
      else:
        all_pixel['incorrect'] = all_pixel['incorrect'] + 1
  
  sum = all_pixel['correct'] + all_pixel['incorrect']
  return int((all_pixel['correct'] / sum) * 100)

def getDialogArea(dialog):
  pixels = dialog.load()
  width, height = dialog.size

  all_pixel = {'yellow': 0, 'incorrect': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      if cpixel[0] > 200 and cpixel[1] > 100 and cpixel[2] > 75:
        if cpixel[1] > 200 and cpixel[2] > 200:
          all_pixel['incorrect'] = all_pixel['incorrect'] + 1
        else:
          all_pixel['yellow'] = all_pixel['yellow'] + 1
      else:
        all_pixel['incorrect'] = all_pixel['incorrect'] + 1
  return getPercent(all_pixel['yellow'], all_pixel['incorrect'])


def getPercent(numa, numb):
  if numa == 0 or numb == 0:
    return 200
  sum = numa + numb
  return int((numa / sum) * 100)

def checkBattle():
  battle = pa.screenshot(region=(551, 25, 29, 1))
  battleCondition = checkBattleFrame(battle)
  if battleCondition > 80:
    return False
  else:
    return True

def main():
  global p
  global id
  id = client.create("暗")
  print(id)
  while True:
    key_stroke = keyboard.read_key()
    if key_stroke == 'f2':
      p = True
      client.play(id)
    if key_stroke == 'f3':
      p = False
      client.pause(id)

    if key_stroke == 'esc':
      exit()
    time.sleep(0.2)

t = threading.Thread(target=main)

t.start()


def whenexit():
  global id
  client.quit(id)

atexit.register(whenexit)


while True:
  if DIALOG_LOCK:
    if client.getDialog() != False:
      action = client.getAction()
      if action:
        if not action['perform']:
          num = action['action']
          if num == 1:
            pa.moveTo(384, 310)
            pa.moveTo(384, 310)
            pa.mouseDown()
            pa.mouseUp()
            time.sleep(0.5)
            pa.moveTo(384, 310)
            pa.moveTo(384, 310)
            pa.mouseDown()
            pa.mouseUp()
          elif num == 2:
            pa.moveTo(384, 341)
            pa.moveTo(384, 341)
            pa.mouseDown()
            pa.mouseUp()
            time.sleep(0.5)
            pa.moveTo(384, 310)
            pa.moveTo(384, 310)
            pa.mouseDown()
            pa.mouseUp()
          elif num == 3:
            pa.moveTo(384, 367)
            pa.moveTo(384, 367)
            pa.mouseDown()
            pa.mouseUp()
            time.sleep(0.5)
            pa.moveTo(384, 310)
            pa.moveTo(384, 310)
            pa.mouseDown()
            pa.mouseUp()
          elif num == 4:
            pa.moveTo(384, 400)
            pa.moveTo(384, 400)
            pa.mouseDown()
            pa.mouseUp()
            time.sleep(0.5)
            pa.moveTo(384, 310)
            pa.moveTo(384, 310)
            pa.mouseDown()
            pa.mouseUp()
          
          dialog = pa.screenshot(region=(241, 122, 302, 292))
          dialogsim = getDialogArea(dialog)
          if dialogsim > 50:
            dialog.save('dialog.png')
            client.dialoging('dialog.png')
            continue
          else:
            client.offDialog()
            client.offAction()
      #384 310 1
      #384 341 2
      #384 367 3
      #384 400 4
      continue
    elif client.getDialog == False:
      DIALOG_LOCK = False

  battle = checkBattle()

  mpNotEnough = []

  shuffle(locate)
  if battle:
    thisframeMp = pa.screenshot(region=(baseX+6, baseMPy+19, 92, 1))
    thisframeHp = pa.screenshot(region=(baseX+6, baseHPy+19, 92, 1)) # +19

    if id != None:
      client.setStatus(id, checkhp(thisframeHp), checkmp(thisframeMp))
    for L in locate:
      if p:
        innerBattleCheck = checkBattle()
        if not innerBattleCheck:
          break
        # pa.moveTo(L[0], L[1])
        pa.keyDown('f6')
        pa.keyUp('f6')
        pa.keyDown('f6')
        pa.keyUp('f6')
  elif not battle:
    dialog = pa.screenshot(region=(241, 122, 302, 292))
    dialogsim = getDialogArea(dialog)
    if dialogsim > 50:
      DIALOG_LOCK = True
      dialog.save('dialog.png')
      client.dialoging('dialog.png')
    
    
    thisframeMp = pa.screenshot(region=(baseX, baseMPy, 92, 1))
    thisframeHp = pa.screenshot(region=(baseX, baseHPy, 92, 1)) # +19
    otherInterfaces = client.all()
    print(otherInterfaces)
    for interface in otherInterfaces:
      try:
        thismp = int(interface['mp'])
        if thismp <= 20:
          if interface['id'] != id:
            mpNotEnough.append(interface)
            print(thismp)
        if interface['stop']:
          mpNotEnough.append(interface)
      except:
        pass
    if len(mpNotEnough) >= 1:
      print('stopping.')
      p = False
    else:
      p = True

    if id != None:
      client.setStatus(id, checkhp(thisframeHp), checkmp(thisframeMp))
    if p:
      pa.keyDown('f5')
      pa.keyUp('f5')
      pa.keyDown('f5')
      pa.keyUp('f5')

  time.sleep(0.2)