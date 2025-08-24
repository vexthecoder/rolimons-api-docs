# Rolimons API Documentation

> ⚠️ **Unofficial Documentation**: This is an unofficial documentation for Rolimons APIs. This project is not affiliated with or endorsed by Rolimons. Use at your own risk.

## Table of Contents
- [Overview](#overview)
- [Demo](#demo)
- [Base URL](#base-url)
- [Authentication](#authentication)
- [Rate Limits](#rate-limits)
- [Endpoints](#endpoints)
  - [Items](#items)
  - [Games](#games)
  - [Players](#players)
  - [Groups](#groups)
  - [Market Data](#market-data)
  - [Trade Ads](#trade-ads)
- [Example Usage](#example-usage)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Notes](#notes)
- [Contributing](#contributing)

## Overview

This documentation covers the unofficial APIs used by Rolimons for accessing game data, item information, player searches, and more. All endpoints return JSON data.

## Demo

Check out the interactive Python demo: [demo.py](https://github.com/vexthecoder/rolimons-api-docs/blob/main/demo.py)

```bash
# Run the demo
python demo.py
```

## Base URL
```plaintext
https://api.rolimons.com/
```

## Authentication
Most endpoints do not require authentication. Some endpoints may require session cookies or specific headers.

## Rate Limits
Unknown - use responsibly and implement appropriate caching. Avoid making rapid successive requests.

## Endpoints

### Items

#### Get All Item Details
```http
GET /items/v2/itemdetails
```

Returns comprehensive details about all items in the Rolimons database.

**Response Format:**
```json
{
  "items": {
    "12345": ["Dominus Frigidus", "DF", 45000, 50000, 1, 0, 1, 0, 0, 0],
    "67890": ["Valkyrie Helm", "VH", 12000, 15000, 0, 1, 0, 0, 0, 0]
  }
}
```

**Field Definitions:**
- Index 0: Item Name (string)
- Index 1: Acronym (string) 
- Index 2: RAP (Recent Average Price) (int)
- Index 3: Value (int)
- Index 4: Projected status (0 or 1)
- Index 5: Rare status (0 or 1)
- Index 6: Hyped status (0 or 1)
- Index 7-9: Unknown/Reserved fields

#### Get Item Thumbnails
```http
GET /itemthumbs/v1/thumbssm
```

Returns small thumbnail URLs for items.

### Games

#### Get Game List
```http
GET /games/v1/gamelist
```

Returns information about Roblox games tracked by Rolimons.

**Response Format:**
```json
{
  "games": {
    "15532962292": ["Sol's RNG [BOSS RAID BETA 1]", 15423, "https://tr.rbxcdn.com/abc123"],
    "8737899170": ["Pet Simulator 99!", 89234, "https://tr.rbxcdn.com/def456"]
  }
}
```

**Field Definitions:**
- Index 0: Game Name (string)
- Index 1: Player Count (int)
- Index 2: Icon URL (string)

### Players

#### Search Players
```http
GET /players/v1/playersearch?searchstring={query}
```

Searches for players by username.

**Parameters:**
- `searchstring` (required): Partial or full username to search for

**Response Format:**
```json
{
  "success": true,
  "result_count": 5,
  "players": [
    [682980257, "JohnDoe"],
    [123456789, "JaneSmith"]
  ]
}
```

**Field Definitions:**
- Index 0: Player ID (int)
- Index 1: Username (string)

#### Get Player Assets
```http
GET /players/v1/playerassets/{player_id}
```

Returns a player's inventory/assets. May return empty if player has privacy enabled.

### Groups

#### Search Groups
```http
GET /groups/v1/groupsearch?searchstring={query}
```

Searches for Roblox groups.

**Parameters:**
- `searchstring` (required): Group name to search for

**Response Format:**
```json
{
  "success": true,
  "result_count": 3,
  "groups": [
    [1234567, "Awesome Group", 1, 2, 3, 15423, "https://tr.rbxcdn.com/groupicon1"],
    [8910111, "Cool Clan", 4, 5, 6, 8923, "https://tr.rbxcdn.com/groupicon2"]
  ]
}
```

**Field Definitions:**
- Index 0: Group ID (int)
- Index 1: Group Name (string)
- Index 2: Unknown (int)
- Index 3: Unknown (int) 
- Index 4: Unknown (int)
- Index 5: Member Count (int)
- Index 6: Icon URL (string)

### Market Data

#### Get Sale Activity
```http
GET /market/v1/saleactivity
```

Returns recent market sale activity.

#### Get Deal Activity
```http
GET /market/v1/dealactivity
```

Returns recent market deal activity.

### Trade Ads

#### Get Recent Trade Ads
```http
GET /tradeads/v1/getrecentads
```

Returns recent trade advertisements.

#### Create Trade Ad
```http
POST /tradeads/v1/createad
```

Creates a new trade advertisement (may require authentication).

**Parameters:**
- Requires JSON payload with trade ad data

#### Remove Trade Ad
```http
GET /tradeads/v1/removead/{ad_id}
```

Removes a trade advertisement (may require authentication).

## Example Usage

### Python

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://www.rolimons.com/'
}

# Get game list
response = requests.get("https://api.rolimons.com/games/v1/gamelist", headers=headers)
games = response.json()

# Search for players
response = requests.get(
    "https://api.rolimons.com/players/v1/playersearch", 
    params={"searchstring": "john"},
    headers=headers
)
players = response.json()

# Get market activity
response = requests.get("https://api.rolimons.com/market/v1/saleactivity", headers=headers)
sales = response.json()
```

### JavaScript

```javascript
// Get item details
fetch('https://api.rolimons.com/items/v2/itemdetails', {
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.rolimons.com/'
    }
})
.then(response => response.json())
.then(data => console.log(data));

// Get market activity
fetch('https://api.rolimons.com/market/v1/dealactivity', {
    headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.rolimons.com/'
    }
})
.then(response => response.json())
.then(data => console.log(data));
```

## Notes

- All endpoints return JSON data
- Some endpoints may have additional undocumented parameters
- The API structure may change without notice
- Always handle errors and rate limiting appropriately
- Market and trade endpoints may require authentication
- Use proper headers (User-Agent, Referer) to avoid 403 errors
- Player assets may be hidden due to privacy settings

## Contributing

Found an issue or have improvements? Contribute to the GitHub repository:

[vexthecoder/rolimons-api-docs](https://github.com/vexthecoder/rolimons-api-docs)

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

*Last Updated: August 24th, 2025 | Unofficial Documentation*
