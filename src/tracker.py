import requests
import json


def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url).json()
    response2 = print(json.dumps(response, indent=4))
    
    print(response2,"\n")

    


def main():
    handle= input("Enter codeforce handle: ")
    get_user_info(handle)

main()