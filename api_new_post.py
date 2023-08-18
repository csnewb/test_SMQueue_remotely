import requests
import json
from config import VALID_QUEUE_NAMES, LOCAL_URL




def submit_post_to_api(queue_name, content, twitter_account_handle, category_name, api_url=LOCAL_URL):
    # Construct the payload
    payload = {
        "queue_name": queue_name,
        "content": content,
        "twitter_account_handle": twitter_account_handle,
        "category_name": category_name
    }


    # Send a POST request with the JSON payload
    response = requests.post(api_url, json=payload)

    # Check for successful response
    if response.status_code == 201:
        print("Post successfully submitted.")
        print(payload)
        return True
    else:
        print("Failed to submit the post:", response.json().get("error"))
        return False



