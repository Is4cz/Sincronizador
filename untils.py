import schedule
import time
from pynput.keyboard import Controller

keyboard = Controller()
stop = False

def pressKey(secondsToPlay):
          time.sleep(secondsToPlay)
          keyboard.tap('k')
          global stop
          stop = True
          print('Pressionado...')

def autoPlay(hoursToPlay: str, secondsToPlay: int):
          """Start the process of waiting for play to begin"""
          print('Aguardando horário {} e {} segundos...'.format(hoursToPlay, secondsToPlay))
          schedule.every().day.at(hoursToPlay).do(pressKey, secondsToPlay)
          while True:
                    if stop:
                              break
                    schedule.run_pending()
                    time.sleep(0.1)