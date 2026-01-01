import requests
import json


def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url).json()

    #print(json.dumps(response, indent=4))
    
    user_info=response["result"][0]

    print(f"Handle: {user_info['handle']}")
    print(f"Avatar: {user_info['titlePhoto']}")
    print(f"Rank: {user_info.get('rank', 'N/A')}")                           ## (print if ,else print)
    print(f"Rating: {user_info.get('rating', 'Unrated')}")
    print(f"Max Rating: {user_info.get("maxRating", "Unrated")}")  
    print(f"Contribution: {user_info["contribution"]}")  
    print('\n')                
    

    
def header():
    print(f'\n######################## Codeforces Tracker ########################\n')

def main():
    handle= input("Enter codeforce handle: ")
    header()
    get_user_info(handle)



main()