import requests
import json

def send_to_webhook(webhook_url, message):
    data = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        if response.status_code == 204:
            print("Information successfully sent to the webhook!")
        else:
            print(f"Failed to send to webhook. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending to webhook: {e}")

def check_token_info(token, webhook_url):
   
    if token.startswith("Bot "):
        url = "https://discord.com/api/v9/users/@me"
        headers = {
            "Authorization": f"{token}"  
        }
    else:
        url = "https://discord.com/api/v9/users/@me"
        headers = {
            "Authorization": f"Bearer {token}" 
        }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            message = f"Token Information:\n"
            message += f"Username: {user_data['username']}#{user_data['discriminator']}\n"
            message += f"User ID: {user_data['id']}\n"
            message += f"Email: {user_data.get('email', 'Not available')}\n"
            message += f"Avatar URL: https://cdn.discordapp.com/avatars/{user_data['id']}/{user_data['avatar']}.png\n"
            message += f"Bot Token: {'Yes' if 'bot' in user_data and user_data['bot'] else 'No'}"

            send_to_webhook(webhook_url, message)

        elif response.status_code == 401:
            print("Invalid token. Unauthorized access.")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    token = input("Enter the Discord token to check: ")
    webhook_url = input("Enter your Discord webhook URL: ")
    check_token_info(token, webhook_url)
