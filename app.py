import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

KEY_WORDS	=['hi', 'hello', 'yo']

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  #helper function
  used_any = lambda word_list: any(map(lambda x: x in text, words_list))

  # We don't want to reply to ourselves!
  #if data['name'] != 'demobot56':
    ##msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    #msg = 'what'
    #send_message(msg)

#THIS CODE WORKS
  #if 'texas' in data['text'].lower():
    #msg = 'Happy saxeT Week! -- Tuck Fexas'
    #send_message(msg)
  #elif 'ou' in data['text'].lower():
    #msg = 'NoNoNo Boomer Sooner'
    #send_message(msg)

  KEY_WORDS = ['hi', 'hello', 'yo']

  for i in range(len(words_list)):
    if KEY_WORDS[i] in data['text'].lower():
      msg = 'word detected: "{}"' .format(KEY_WORDS[i].lower())
      send_message(msg)
    else:
      msg = 'you sent "{}".' .format(data['text'])
      send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
