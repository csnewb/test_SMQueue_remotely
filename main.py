import requests

import input_data
import screened_proverbs_list
from api_new_post import submit_post_to_api
from config import LOCAL_URL

##########

def run_main_submit_new_posts(num_posts):
    queue_name = 'general_review'
    twitter_account_handle = 'shortmoneysite'
    category_name = 'quotes'
    api_url = LOCAL_URL
    queue_name = 'general_active'
    twitter_account_handle = 'tester'
    category_name = 'quotes'


    for i in range(num_posts):
        content = input_data.unique_shuffled_list[i]



        submit_post_to_api(queue_name=queue_name,
                           content=content,
                           twitter_account_handle=twitter_account_handle,
                           category_name=category_name,
                           api_url=api_url
                           )
    return

def run_api_call_to_main_delivery():
    # Send a POST request with the JSON payload
    # api_url = 'http://127.0.0.1:5000/delivery/api/activate_delivery'
    api_url = 'http://137.184.180.201/delivery/api/activate_delivery'
    response = requests.post(api_url)
    if response.status_code == 201:
        print("Post successfully submitted.")
        return True
    else:
        print("Failed to submit the post:", response.json().get("error"))
        return False


if __name__ == '__main__':
    run_main_submit_new_posts(num_posts=30)
    # run_api_call_to_main_delivery()


