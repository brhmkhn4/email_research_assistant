import json
import requests
from random import choice
from string import ascii_uppercase
import os

# it will get web results using serper
def search_serper(search_query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q" : search_query,
        "gl" : "gb",
        "num" : 4,
        "tbs" : "qdr:d"
    })
    headers = {
        'X-API-KEY': os.getenv('ZENSCRAPE_API_KEY'), # ZENSCRAPE_API_KEY = "52227bb4ce11d45935ad38a980f15b234de6cf6d"
        'Content-Type': 'application/json'
    }
    # calling serper api
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(f'result of Serper Search {response.text}')  
    # extracting text data out of the serper response converting it to json format
    result = json.loads(response.text)
    # extracting further cleaned data with key named organic which contain list of dictionary with keys organic[{'title':"", 'link':"", 'snippet':"", 'date':"", 'position':""}]
    results_list = result['organic']# organic[{'title':"", 'link':"", 'snippet':"", 'date':"", 'position':""}]

    all_results = []
    
    for result in results_list:
        id = (''.join(choice(ascii_uppercase) for i in range(12)))         
        result_dict = {
            'title': result['title'],
            'link' : result['link'],
            'snippet' : result['snippet'],
            'search_term' : search_query,
            'id' : id 
        }
        all_results.append(result_dict)
        
    # print(f"serper result {all_results}")
    return all_results