import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

def send_like(uid):
    url = f"https://likes.api.freefireofficial.com/api/sg/{uid}?key={API_KEY}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if "message" in data and "maximum" in data["message"].lower():
            print("┌  MAX LIKES\n└─ This uid has already received the maximum likes today.")
        elif "data" in data:
            added = data["data"].get("addLike", "N/A")
            before = data["data"].get("before", "N/A")
            after = data["data"].get("after", "N/A")
            nickname = data["data"].get("nickname", "UNKNOWN")

            print(f"""┌  ACCOUNT
├─ NICKNAME:{nickname}
├─ UID:{uid}
└─ RESULT:
    ├─ ADDED:+{added}
    ├─ BEFORE:{before}
    └─ AFTER:{after}""")
        else:
            print("Something went wrong:", data)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    uid = input("Enter Free Fire UID: ")
    send_like(uid)
