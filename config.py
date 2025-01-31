import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
API_URL = "https://multiplayersessionlist.iondriver.com/api/1.0/sessions?game=bigboat:battlezone_combat_commander" 
NOTIFICATION_TAG = "@BZ2Player"  # can be @BZ2Player, @everyone, or empty for no tags in message payloads

MONITORED_STEAM_IDS = [
    "76561198006115793",  # Domakus
    "76561198846500539",  # Xohm
    "76561197974548434",  # VTrider
    "bz2Cyber",           # Cyber
    "76561198825004088",  # Lamper
    "herpmcderperson",    # Herp
    "76561198820311491",  # m.s 
    "running-roxas",      # Sly
    "76561198068133931",  # Econchump
    "76561198026325621",  # F9Bomber
    # "bzlolol",            # blue_banana
    # "76561198088036138",  # dd
    # "76561198058690608",  # JudgeGuns
    # "76561199732480793",  # XPi
    # "76561198088149233",  # Muffin
    # "76561198064801924",  # HappyOtter
    # "76561198045619216",  # Zack
    # "76561197970538803",  # Graves
    # "76561198345909972",  # Vivify
    # "76561199653748651",  # Sev
]

CHECK_INTERVAL = 5