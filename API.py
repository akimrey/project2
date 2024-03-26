import requests

def fetch_trending_gifs():
    response = requests.get(api_url)
    if response.status_code == 200:
        # Convert the JSON response to a Python dictionary
        data = response.json()
        return data
    else:
        return "Error: Unable to fetch the data."

trending_gifs = fetch_trending_gifs()
print(trending_gifs)
