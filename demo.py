import requests
import json
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to return to the main menu...")

def make_api_request(url, params=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.rolimons.com/',
        'Origin': 'https://www.rolimons.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            return {"error": f"403 Forbidden - Headers used: {dict(response.request.headers)}"}
        elif response.status_code == 404:
            return {"error": "404 Not Found - Endpoint may not exist"}
        else:
            return {"error": f"HTTP Error {response.status_code}: {str(e)}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_game_list():
    url = "https://api.rolimons.com/games/v1/gamelist"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return {}
    
    games = data.get("games", {})
    print(f"Found {len(games)} games")
    
    if games:
        count = 0
        for game_id, game_data in games.items():
            if count < 5:
                print(f"  {game_id}: {game_data[0]} ({game_data[1]} players)")
                count += 1
        if len(games) > 5:
            print(f"  ... and {len(games) - 5} more games")
    
    return games

def get_game_by_id(game_id):
    games = get_game_list()
    game_data = games.get(str(game_id))
    
    if game_data:
        print(f"\nGame ID: {game_id}")
        print(f"Name: {game_data[0]}")
        print(f"Players: {game_data[1]}")
        print(f"Icon URL: {game_data[2]}")
    else:
        print(f"\nGame ID {game_id} not found in the game list.")

def get_item_details():
    url = "https://api.rolimons.com/items/v2/itemdetails"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return {}
    
    items = data.get("items", {})
    print(f"Found {len(items)} items")
    
    if items:
        count = 0
        for item_id, item_data in items.items():
            if count < 5:
                rap = item_data[2] if len(item_data) > 2 else "N/A"
                value = item_data[3] if len(item_data) > 3 else "N/A"
                print(f"  {item_id}: {item_data[0]} (RAP: {rap}, Value: {value})")
                count += 1
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more items")
    
    return items

def get_item_by_id(item_id):
    items = get_item_details()
    item_data = items.get(str(item_id))
    
    if item_data:
        print(f"\nItem ID: {item_id}")
        print(f"Name: {item_data[0]}")
        if len(item_data) > 1:
            print(f"Acronym: {item_data[1]}")
        if len(item_data) > 2:
            print(f"RAP: {item_data[2]}")
        if len(item_data) > 3:
            print(f"Value: {item_data[3]}")
    else:
        print(f"\nItem ID {item_id} not found in the item list.")

def search_players(query):
    url = "https://api.rolimons.com/players/v1/playersearch"
    params = {"searchstring": query}
    data = make_api_request(url, params)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    if data.get("success"):
        players = data.get("players", [])
        print(f"\nFound {len(players)} players:")
        for player in players:
            if len(player) >= 2:
                print(f"  {player[0]}: {player[1]}")
    else:
        print("Player search failed or returned no results.")

def search_groups(query):
    url = "https://api.rolimons.com/groups/v1/groupsearch"
    params = {"searchstring": query}
    data = make_api_request(url, params)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    if data.get("success"):
        groups = data.get("groups", [])
        print(f"\nFound {len(groups)} groups:")
        for group in groups:
            if len(group) >= 6:
                print(f"  {group[0]}: {group[1]} ({group[5]} members)")
    else:
        print("Group search failed or returned no results.")

def get_item_thumbnails():
    url = "https://api.rolimons.com/itemthumbs/v1/thumbssm"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    thumbs = data.get("items", {})
    print(f"Found {len(thumbs)} item thumbnails")
    
    if thumbs:
        count = 0
        for item_id, thumb_url in thumbs.items():
            if count < 3:
                print(f"  {item_id}: {thumb_url}")
                count += 1
        if len(thumbs) > 3:
            print(f"  ... and {len(thumbs) - 3} more thumbnails")

def get_recent_trade_ads():
    url = "https://api.rolimons.com/tradeads/v1/getrecentads"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    print("Recent Trade Ads Response:")
    print(json.dumps(data, indent=2)[:500] + "..." if len(json.dumps(data)) > 500 else json.dumps(data, indent=2))

def get_sale_activity():
    url = "https://api.rolimons.com/market/v1/saleactivity"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    print("Sale Activity Response:")
    print(json.dumps(data, indent=2)[:500] + "..." if len(json.dumps(data)) > 500 else json.dumps(data, indent=2))

def get_deal_activity():
    url = "https://api.rolimons.com/market/v1/dealactivity"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    print("Deal Activity Response:")
    print(json.dumps(data, indent=2)[:500] + "..." if len(json.dumps(data)) > 500 else json.dumps(data, indent=2))

def get_player_assets(player_id):
    url = f"https://api.rolimons.com/players/v1/playerassets/{player_id}"
    data = make_api_request(url)
    
    if "error" in data:
        print(f"Error: {data['error']}")
        return
    
    print("Player Assets Response:")
    print(json.dumps(data, indent=2)[:500] + "..." if len(json.dumps(data)) > 500 else json.dumps(data, indent=2))
    
    if data.get("playerPrivacyEnabled"):
        print("\nNote: Player has privacy settings enabled, assets may be hidden.")

def main():
    while True:
        clear_console()
        print("=== Rolimon's API Explorer ===")
        print("1. Get Game List")
        print("2. Lookup Game by ID")
        print("3. Get Item Details")
        print("4. Lookup Item by ID")
        print("5. Search Players")
        print("6. Search Groups")
        print("7. Get Item Thumbnails")
        print("8. Get Recent Trade Ads")
        print("9. Get Sale Activity")
        print("10. Get Deal Activity")
        print("11. Get Player Assets")
        print("12. Exit")
        
        try:
            choice = input("\nEnter choice: ").strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
            
        clear_console()
        
        if choice == "1":
            print("=== Rolimon's Game List ===\n")
            get_game_list()
            pause()
        elif choice == "2":
            print("=== Rolimon's Game Lookup ===\n")
            try:
                gid = input("Enter Game ID: ").strip()
                get_game_by_id(gid)
            except ValueError:
                print("Invalid Game ID. Please enter a numeric value.")
            pause()
        elif choice == "3":
            print("=== Rolimon's Item Details ===\n")
            get_item_details()
            pause()
        elif choice == "4":
            print("=== Rolimon's Item Lookup ===\n")
            try:
                iid = input("Enter Item ID: ").strip()
                get_item_by_id(iid)
            except ValueError:
                print("Invalid Item ID. Please enter a numeric value.")
            pause()
        elif choice == "5":
            print("=== Rolimon's Player Search ===\n")
            name = input("Enter Player Name: ").strip()
            if name:
                search_players(name)
            else:
                print("Please enter a valid player name.")
            pause()
        elif choice == "6":
            print("=== Rolimon's Group Search ===\n")
            name = input("Enter Group Name: ").strip()
            if name:
                search_groups(name)
            else:
                print("Please enter a valid group name.")
            pause()
        elif choice == "7":
            print("=== Rolimon's Item Thumbnails ===\n")
            get_item_thumbnails()
            pause()
        elif choice == "8":
            print("=== Recent Trade Ads ===\n")
            get_recent_trade_ads()
            pause()
        elif choice == "9":
            print("=== Sale Activity ===\n")
            get_sale_activity()
            pause()
        elif choice == "10":
            print("=== Deal Activity ===\n")
            get_deal_activity()
            pause()
        elif choice == "11":
            print("=== Player Assets ===\n")
            try:
                pid = input("Enter Player ID: ").strip()
                get_player_assets(pid)
            except ValueError:
                print("Invalid Player ID. Please enter a numeric value.")
            pause()
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-12.")
            pause()

if __name__ == "__main__":
    main()
