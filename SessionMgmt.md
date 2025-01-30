# Session Management Report

## Overview
This document provides a detailed overview of the session management functionality within the Discord bot that monitors game sessions. It covers the data structure used for tracking sessions, the processes for adding, updating, and ending sessions, as well as error handling and logging.

## 1. Data Structure for Session Tracking

- **Active Sessions Dictionary**: 
  - The bot maintains a dictionary (e.g., `self.active_sessions`) where each key is a unique session ID, and the value is an object or dictionary containing details about that session.
  
  Example structure:
  ```python
  self.active_sessions = {
      "session_id_1": {
          "game_name": "Game Title",
          "player_count": 5,
          "max_players": 10,
          "status": "InGame",
          "mod": {
              "name": "Mod Name",
              "url": "http://example.com"
          },
          "players": ["Player1", "Player2", "Player3"]
      },
      "session_id_2": {
          # ... other session details ...
      }
  }
  ```

## 2. Fetching and Updating Sessions

- **Periodic Data Fetching**:
  - The bot regularly calls an API endpoint to fetch the latest game session data. This could be done using an asynchronous function that runs on a timer or in response to specific events.
  
- **Session Comparison Logic**:
  - After fetching the current session data, the bot compares the session IDs from the API response with those in its `active_sessions`.
  - This comparison helps determine:
    - **New Sessions**: If a session ID from the API is not in `active_sessions`, it indicates a new session that needs to be added.
    - **Existing Sessions**: If a session ID is found, the bot updates the session details based on the latest data.
    - **Ended Sessions**: If a session ID in `active_sessions` is not found in the API response, it indicates that the session has ended.

## 3. Handling New Sessions

- **Adding New Sessions**:
  - When a new session is detected, the bot:
    - Adds the session to `self.active_sessions`.
    - Sends a notification to a designated Discord channel, including details like the game name, player count, and any relevant links (e.g., to the mod).
    
    Example code snippet:
    ```python
    if session_id not in self.active_sessions:
        self.active_sessions[session_id] = session_data
        await self.send_discord_notification(session_data, is_new=True)
    ```

## 4. Updating Existing Sessions

- **Updating Session Details**:
  - For existing sessions, the bot updates the relevant fields based on the latest data from the API. This may include:
    - Updating the player count as players join or leave.
    - Changing the game state (e.g., from "Pregame" to "InGame").
    - Updating mod information if it has changed.
    
    Example code snippet:
    ```python
    if session_id in self.active_sessions:
        self.active_sessions[session_id].update(session_data)
        await self.send_discord_notification(session_data, is_new=False)
    ```

## 5. Ending Sessions

- **Marking Sessions as Ended**:
  - When a session is no longer present in the API response, the bot needs to handle this appropriately.
  - The bot calls a function (e.g., `mark_session_ended()`) to:
    - Update the corresponding Discord embed to indicate that the session has ended (e.g., changing the title to "Session Ended" and updating the color).
    - Remove the session from `self.active_sessions` to clean up resources.
    - Optionally, log this event for monitoring purposes.
    
    Example code snippet:
    ```python
    async def mark_session_ended(self, session_id, session_data):
        # Update embed to show session ended
        embed = await self.format_session_embed(session_data)
        embed['title'] = "❌  Session Ended"
        embed['color'] = 0xED4245  # Red color
        # Send updated embed to Discord
        await self.update_discord_message(session_id, embed)
        # Clean up session tracking
        self.active_sessions.pop(session_id, None)
    ```