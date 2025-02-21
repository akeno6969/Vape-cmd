import requests

def send_dm(token, user_id, message):
    url = f"https://discord.com/api/v9/users/{user_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "content": message
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Message sent to {user_id} using token {token[:10]}...")
        else:
            print(f"Failed to send message to {user_id} using token {token[:10]} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def token_dmall(tokens, user_ids, message):
    for token in tokens:
        for user_id in user_ids:
            send_dm(token, user_id, message)

if __name__ == "__main__":
    
    tokens = []
    print("Enter your Discord tokens (enter 'done' when finished):")
    while True:
        token_input = input("Enter Discord Token: ")
        if token_input.lower() == "done":
            break
        tokens.append(token_input)

    
    user_ids = []
    print("Enter user IDs (enter 'done' when finished):")
    while True:
        user_id_input = input("Enter User ID: ")
        if user_id_input.lower() == "done":
            break
        user_ids.append(user_id_input)

    
    message = input("Enter the message you want to send: ")

    
    token_dmall(tokens, user_ids, message)
