from ticktick.oauth2 import OAuth2

# Replace with your details from the developer portal
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "http://127.0.0.1:8080"  # e.g., http://127.0.0.1:8080

auth_client = OAuth2(client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri=redirect_uri)

# This will open a web browser for authorization
# Follow the instructions in the terminal to authorize
print(auth_client.access_token_info)
