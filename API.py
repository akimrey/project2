import requests

# Your API URL with the key and parameters included
api_url = "https://api.giphy.com/v1/gifs/trending?api_key=fwmPVjyOZsVvHGKarGwKb81LeaQOFqga&limit=25&offset=0&rating=g"

def fetch_trending_gifs():
    response = requests.get(api_url)
    if response.status_code == 200:
        # Convert the JSON response to a Python dictionary
        data = response.json()
        return data
    else:
        return "Error: Unable to fetch the data."

# Fetch trending GIFs
trending_gifs = fetch_trending_gifs()
print(trending_gifs)
