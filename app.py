import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# load API keys and tokens from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# list of tweet IDs to delete
TWEET_IDS_TO_DELETE = [
    "1772960524864487435",  # example tweet ID 1
    "1772513632347373588",  # example tweet ID 2
]

# authenticate
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# function to delete a tweet
def delete_tweet(tweet_id):
    url = f"https://api.x.com/2/tweets/{tweet_id}"
    response = requests.delete(url, auth=auth)

    if response.status_code in [200, 204]:
        print(f"Successfully deleted tweet {tweet_id}. Response: {response.text}")
    else:
        print(
            f"Failed to delete tweet {tweet_id}: {response.status_code} - {response.text}"
        )


# execute
if __name__ == "__main__":
    for tweet_id in TWEET_IDS_TO_DELETE:
        delete_tweet(tweet_id)
