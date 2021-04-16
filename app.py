import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers ={
    "Authorization": "Bearer "+ config.api_key
} 


def get_biz(offset):
    """
    the function gets the names of business from Yelp API
    """
    params={
        "term": "restaurants",
        "location": "Cologne",
        "limit": 50,
        "offset": offset
    } 

    try:
        response = requests.get(url, headers=headers, params=params)
        result = response.json()['businesses']
        names = [business["name"] for business in result]  
        print(names)
        print(len(names))
    except:
        print("Reached the limit")
        names=[]  
    
    return names

if __name__ == '__main__':
    biz=[] 

    for i in range(1, 1001, 50):
        biz.append(get_biz(i))

    print(biz)

