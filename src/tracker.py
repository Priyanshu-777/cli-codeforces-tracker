import requests
import pyfiglet
#import json


def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url).json()
    #print(json.dumps(response, indent=4))
    
    user_info=response["result"][0]

    print(f"\nHandle: {user_info['handle']}")
    print(f"Avatar: {user_info['titlePhoto']}")
    print(f"Rank: {user_info.get('rank', 'N/A')}")                           ## (print if ,else print)
    print(f"Rating: {user_info.get('rating', 'Unrated')}")
    print(f"Max Rating: {user_info.get("maxRating", "Unrated")}")  
    print(f"Contribution: {user_info["contribution"]}\n")  
                   
    

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

    print(f"Total Problem Solved: {len(solved)}\n")
    problem_by_level(solved)

    

def problem_by_level(solved):
    difficulty_count = {}

    for contest_id, index in solved:
        if index:
            level = index[0]
            difficulty_count[level] = difficulty_count.get(level, 0) + 1

    print("Problems solved by difficulty:")
    for level in sorted(difficulty_count.keys()):
        print(f"    {level}: {difficulty_count[level]}")

    print()
    


def header():
    line()
    print(pyfiglet.figlet_format("Codeforces Tracker"))
    line()

def line():
    print("="*90)   


def main():
    header()
    
    handle= input("\nEnter codeforce handle: ")
    
    get_user_info(handle)
    get_user_submissions(handle)
    line()
    print("\n")




main()