from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import discovery

def initSonos():
  global vol, sonos_list
  lcd.fill(0x000000)
  lcd.print('Connecting', 0, 75, 0xffffff)
  wifiCfg.screenShow()
  wifiCfg.autoConnect(lcdShow = True)
  while not (wifiCfg.wlan_sta.isconnected()):
    wait_ms(500)
  wait_ms(1000)
  lcd.fill(0x000000)
  lcd.print('Init SONOS', 3, 75, 0xffffff)
  sonos_list = sum([sum([[s], s.other_players],[]) for s in discovery.discover()], [])

def renderVolume():
  global vol, sonos_list, updating
  lcd.fill(0x000000)
  color = 0x000022 if updating else 0xaaaaaa
  lcd.print('Volume', 13, 14, color)
  if vol >= 10:
    lcd.rect(10, 126, 60, 29, color, color)
  if vol >= 20:
    lcd.rect(10, 96, 60, 29, color, color)
  if vol >= 30:
    lcd.rect(10, 66, 60, 29, color, color)
  if vol >= 40:
    lcd.rect(10, 36, 60, 29, color, color)

def setVolume():
  global vol, sonos_list, updating
  updating = True
  renderVolume()
  [ s.volume(vol) for s in sonos_list ]
  [ s.mute(False) for s in sonos_list ]
  updating = False
  renderVolume()

def buttonA_wasPressed():
  global vol, sonos_list, updating, btnAPressing
  if not btnAPressing:
    btnAPressing = True
    vol = vol + 10
    if vol > 40:
      vol = 40
    setVolume()
    btnAPressing = False
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global vol, sonos_list, updating, btnBPressing
  if not btnBPressing:
    btnBPressing = True
    vol = vol - 10
    if vol <= 0:
      vol = 0
    setVolume()
    btnBPressing = False
  pass
btnB.wasPressed(buttonB_wasPressed)

btnAPressing = False
btnBPressing = False
updating = False
vol = 10
sonos_list = []
initSonos()
setVolume()
