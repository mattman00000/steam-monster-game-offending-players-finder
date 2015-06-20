import json
import urllib.request
import time
import traceback

#VARIABLES TO EDIT
logDirectory = r".\\"
gameid = 46100

#DO NOT EDIT
logged=[] 
ABILITIES = {
		26:"Wormhole"
	}
while True:
  try:
    r=urllib.request.urlopen("http://steamapi-a.akamaihd.net/ITowerAttackMiniGameService/GetGameData/v0001/?gameid="+ str(gameid) +"&include_stats=1&format=json").read()
    jsonobj=json.loads(r.decode('utf-8'))
    lvl = jsonobj["response"]["game_data"]["level"]+1
    lanes = jsonobj["response"]["game_data"]["lanes"]     
    with open(logDirectory+str(gameid)+"_wormholes.log", "a") as myfile:
      for lane in lanes:
        active_abilities = lane["active_player_abilities"]
        for active in active_abilities:
          if active["timestamp_done"] > jsonobj["response"]["game_data"]["timestamp_level_start"]:
            #if lvl%100==0: #boss level commented out to log all levels
              if active["ability"] in ABILITIES: #nuking abilities
                message = ['Boss level',str(lvl),time.strftime('%x %X', time.gmtime(active["timestamp_done"])), ABILITIES[active["ability"]], str(76561197960265728+active["accountid_caster"]),"\n"]
                if message not in logged:
                  myfile.write('\t'.join(message))
                  logged.append(message)
  except Exception as e:
    pass #No abilities active in lane
  time.sleep(1)
