import json
import urllib.request
import time
import traceback

#VARIABLES TO EDIT
logDirectory = "C:\\Users\\Matt\\Downloads\\" #CHANGE THIS TO THE FOLDER YOU WANT LOGS IN
gameid = 48265 #ROOM NUMBER HERE

#DO NOT EDIT
logged=[] 
ABILITIES = {
        10:"Tactical Nuke",
        11:"Cluster Bomb",
        12:"Napalm",
        15:"Cripple Monster",
        20:"Throw Money",
        26:"WORMHOLE"
    }
while True:
  try:
    r=urllib.request.urlopen("http://steamapi-a.akamaihd.net/ITowerAttackMiniGameService/GetGameData/v0001/?gameid="+ str(gameid) +"&include_stats=1&format=json").read()
    jsonobj=json.loads(r.decode('utf-8'))
    lvl = jsonobj["response"]["game_data"]["level"]+1
    lanes = jsonobj["response"]["game_data"]["lanes"]     
    with open(logDirectory+str(gameid)+"_super_offenders.log", "a") as myfile:
      for lane in lanes:
        active_abilities = lane["active_player_abilities"]
        for active in active_abilities:
          if active["timestamp_done"] > jsonobj["response"]["game_data"]["timestamp_level_start"]:
            if active["ability"] in ABILITIES: #nuking abilities
              if lvl%100==0: #boss level
                message = ['Boss level',str(lvl),time.strftime('%x %X', time.gmtime(active["timestamp_done"])), ABILITIES[active["ability"]], str(76561197960265728+active["accountid_caster"]),"\n"]
              else:
                message = ['Normal lvl',str(lvl),time.strftime('%x %X', time.gmtime(active["timestamp_done"])), ABILITIES[active["ability"]], str(76561197960265728+active["accountid_caster"]),"\n"]
              if message not in logged:
                myfile.write('\t'.join(message))
                logged.append(message)
  except Exception as e:
    pass #No abilities active in lane
  time.sleep(1)
