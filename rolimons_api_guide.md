# Rolimons Unofficial API Documentation

## Overview
Rolimons provides several official API endpoints for accessing game data, item information, player searches, and more. All endpoints return JSON data.

## Base URL
`https://api.rolimons.com/`

## Authentication
Most endpoints do not require authentication. Some endpoints may require session cookies.

## Rate Limits
Unknown - use responsibly and implement appropriate caching.

## Endpoints

### Items
#### Get All Item Details
`GET /items/v2/itemdetails`
Returns comprehensive details about all items in the Rolimons database.

```json
{
  "items": {
    "item_id": ["Item Name", "Acronym", RAP, Value, ...],
    ...
  }
}
```

#### Get Item Thumbnails
`GET /itemthumbs/v1/thumbssm`
Returns small thumbnail URLs for items.

### Games
#### Get Game List
`GET /games/v1/gamelist`
Returns information about Roblox games tracked by Rolimons.

```json
{
  "games": {
    "game_id": ["Game Name", player_count, icon_url],
    ...
  }
}
```

### Players
#### Search Players
`GET /players/v1/playersearch?searchstring={query}`
Searches for players by username.

**Parameters:**
- `searchstring` (required): Partial or full username to search for

```json
{
  "success": true,
  "result_count": 5,
  "players": [
    [player_id, "username"],
    ...
  ]
}
```

#### Get Player Assets
`GET /players/v1/playerassets/{player_id}`
Returns a player's inventory/assets.

### Groups
#### Search Groups
`GET /groups/v1/groupsearch?searchstring={query}`
Searches for Roblox groups.

**Parameters:**
- `searchstring` (required): Group name to search for

```json
{
  "success": true,
  "result_count": 3,
  "groups": [
    [group_id, "Group Name", unknown, unknown, unknown, member_count, icon_url],
    ...
  ]
}
```

### Market Data
#### Get Sale Activity
`GET /market/v1/saleactivity`
Returns recent market sale activity.

#### Get Deal Activity
`GET /market/v1/dealactivity`
Returns recent market deal activity.

### Trade Ads
#### Get Recent Trade Ads
`GET /tradeads/v1/getrecentads`
Returns recent trade advertisements.

#### Create Trade Ad
`POST /tradeads/v1/createad`
Creates a new trade advertisement.

**Parameters:**
- Requires JSON payload with trade ad data

#### Remove Trade Ad
`GET /tradeads/v1/removead/{ad_id}`
Removes a trade advertisement.

## Example Usage

### Python Example
```python
import requests

# Get game list
response = requests.get("https://api.rolimons.com/games/v1/gamelist")
games = response.json()

# Search for players
response = requests.get("https://api.rolimons.com/players/v1/playersearch", 
                       params={"searchstring": "john"})
players = response.json()

# Get market activity
response = requests.get("https://api.rolimons.com/market/v1/saleactivity")
sales = response.json()
```

### JavaScript Example
```javascript
fetch('https://api.rolimons.com/items/v2/itemdetails')
  .then(response => response.json())
  .then(data => console.log(data));

fetch('https://api.rolimons.com/market/v1/dealactivity')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Notes
- All endpoints return JSON data
- Some endpoints may have additional undocumented parameters
- The API structure may change without notice
- Always handle errors and rate limiting appropriately
- Market and trade endpoints may require authentication