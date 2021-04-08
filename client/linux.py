import pyautogui as pa
import keyboard
import threading
import time
import client
from random import shuffle
id = 0
previousHpMp = []
p = True

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

# 20-112 44
locate = [(130, 420), (203,367), (262,312), (351,249), (425,191), (72,353),(138,311), (220, 249), (290,187), (359,139)]




def checkmp(mp):
  pixels = mp.load()
  width, height = mp.size

  all_pixel = {'blue': 0, 'white': 0}
  for x in range(width):
    for y in range(height):
      cpixel = pixels[x, y]
      if cpixel[0] > 200:
        all_pixel['white'] = all_pixel['white'] + 1
      else:
        all_pixel['blue'] = all_pixel['blue'] + 1
  return getPercent(all_pixel['blue'], all_pixel['white'])

def getPercent(numa, numb):
  sum = numa + numb
  return (numa / sum) * 100
  

def main():
  global p
  global id
  id = client.create()
  print(id)
  while True:
    key_stroke = keyboard.read_key()
    if key_stroke == 'f2':
      p = True

    if key_stroke == 'f3':
      p = False
    

    if key_stroke == 'esc':
      exit()
    time.sleep(0.2)

t = threading.Thread(target=main)

t.start()

while True:
  shuffle(locate)
  thisframeMp = pa.screenshot(region=(21, 44, 92, 1))
  checkmp(thisframeMp)
  for L in locate:
    if p:
      pa.moveTo(L[0], L[1])
      pa.keyDown('f6')
      pa.keyUp('f6')
      pa.keyDown('f6')
      pa.keyUp('f6')
      pa.keyDown('f6')
      pa.keyUp('f6')
      pa.keyDown('f6')
      pa.keyUp('f6')
      pa.keyDown('f6')
      pa.keyUp('f6')
      pa.mouseDown()
      pa.mouseUp()

  time.sleep(0.2)