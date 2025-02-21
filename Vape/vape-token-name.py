import requests

def check_token_name(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            username = data["username"]
            discriminator = data["discriminator"]
            print(f"Token is valid. Username: {username}#{discriminator}")
        else:
            print(f"Invalid token or error occurred. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error checking token: {e}")


if __name__ == "__main__":
    
    tokens = []
    print("Enter your Discord tokens (enter 'done' when finished):")
    while True:
        token_input = input("Enter Discord Token: ")
        if token_input.lower() == "done":
            break
        tokens.append(token_input)

    
    for token in tokens:
        check_token_name(token)
