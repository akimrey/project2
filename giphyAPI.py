import os
import requests

class GiphyAPI:

    def __init__(self):
        # Safely get the API key or set to None if it's not found
        self.api_key = os.getenv("GIPHY_API_KEY")
        if not self.api_key:
            raise ValueError("GIPHY_API_KEY environment variable not set.")

    def get_TrendingGifs(self):
        result = requests.get(
            f"https://api.giphy.com/v1/gifs/trending?api_key={self.api_key}&limit=25&offset=0&rating=g"
        )
        result.raise_for_status()  # Raises an error for bad responses
        return result.json()

    def get_SearchGifs(self, query):
        result = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key={self.api_key}&q={query}&limit=25&offset=0&rating=g"
        )
        result.raise_for_status()  # Raises an error for bad responses
        return result.json()
