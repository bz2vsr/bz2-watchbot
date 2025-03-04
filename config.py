import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
API_URL = "https://multiplayersessionlist.iondriver.com/api/1.0/sessions?game=bigboat:battlezone_combat_commander" 
NOTIFICATION_TAG = "<@&1137622254621032500>"  # ID-based role ping for @BZ2Player
# NOTIFICATION_TAG = "NO_PING"  # Don't ping at all

# one of these players must be the game host, for a game to be posted
MONITORED_STEAM_IDS = [
    "76561198006115793",  # Domakus
    "76561198846500539",  # Xohm
    "76561198824607769",  # Cyber
    "76561197962996353",  # Herp
    "76561198076339639",  # Sly
    "76561198820311491",  # m.s 
    # "76561198043392032",  # blue_banana
    # "76561197974548434",  # VTrider
    # "76561198068133931",  # Econchump
    # "76561198825004088",  # Lamper
    # "76561198026325621",  # F9Bomber
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