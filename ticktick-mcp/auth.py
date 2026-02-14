import os
from dotenv import load_dotenv
from ticktick.oauth2 import OAuth2

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

client_id = os.environ["TICKTICK_CLIENT_ID"]
client_secret = os.environ["TICKTICK_CLIENT_SECRET"]
redirect_uri = os.environ["TICKTICK_REDIRECT_URI"]

auth_client = OAuth2(client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri=redirect_uri)

print(auth_client.access_token_info)
