import requests

def fetch_data(api_key):
    # Construct the URL with the provided API key
    url = f"https://api.example.com/data?api_key={api_key}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and return it
        return response.json()
    else:
        # Return a message or handle errors as needed
        return {"error": "Failed to fetch data", "status_code": response.status_code}
