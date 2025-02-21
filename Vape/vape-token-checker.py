import requests

def check_own_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": f"Bearer {token}"  
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            
            user_data = response.json()
            print(f"Token is valid!")
            print(f"Username: {user_data['username']}#{user_data['discriminator']}")
            print(f"User ID: {user_data['id']}")
        elif response.status_code == 401:
            print("Invalid token. Unauthorized access.")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    token = input("Enter your Discord token to check: ")
    check_own_token(token)
