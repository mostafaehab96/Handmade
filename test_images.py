import requests

if __name__ == "__main__":
    url = "https://api.unsplash.com/photos/random"
    headers = {
        "Authorization": "Client-ID 2pNFjo8YYnAJTdhP0mhIBeR0zb3vn1US7pOJ1hzRG0A"
    }
    params = {
        "query": "handmade",
        "count": 30
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        with open("test_images.txt", "a") as file:
            for res in response.json():
                url = res["urls"]["small"]
                file.write(f"{url}\n")
    else:
        print(response.status_code)






