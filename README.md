# BZ2VSR GameWatch Service

A Web Service that monitors multiplayer game data from [Battlezone II: Combat Commander](https://store.steampowered.com/app/624970/Battlezone_Combat_Commander/), curated specifically for VSR games hosted by the [BZ2 Vet Strat](https://discord.gg/FQnXFhnp) Discord community. Inspired by the [bz2vsr.com](https://github.com/bz2vsr/bz2vsr.github.io).

Relies on the MultiplayerSessionList API by Nielk1 ([Github](https://github.com/Nielk1) | [Twitter](https://x.com/nielk1)).

## Technical Details

- Uses Discord webhooks for communication
- Polls the BZ2 multiplayer API at configurable intervals
- Maintains session history for accurate status tracking
- Handles both Steam and GOG player identifiers
- Includes enhanced VSR map data

## Requirements

- Python 3.7+
- python-dotenv
- aiohttp
- watchdog