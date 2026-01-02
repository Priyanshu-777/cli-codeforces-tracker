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
                   
    

def get_user_submissions(handle):
    url =  f"https://codeforces.com/api/user.status?handle={handle}"
    response = requests.get(url).json()
    #print(json.dumps(response,indent=4))

    submissions_list= response['result']
    solved = set()

    for submission in submissions_list:
        if submission['verdict']== "OK":        # solution accepted by cf
            problem = submission['problem']
            solved_problem_id = (problem.get("contestId"), problem.get("index"))

            solved.add(solved_problem_id)

    print(f"Number of problem solved: {len(solved)}\n")



def header():
    print(f'\n########################## Codeforces Tracker ##########################\n')

def main():
    handle= input("Enter codeforce handle: ")
    header()
    get_user_info(handle)
    get_user_submissions(handle)




main()