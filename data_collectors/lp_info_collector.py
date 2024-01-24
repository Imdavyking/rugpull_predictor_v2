import requests
import json

def get_top_token_holders(token_id, limit=1000):
    # Replace 'YOUR_API_KEY' with your actual Ethplorer API key
    api_key = 'EK-fewp2-ycMSQm7-3Qj3b'
    url = f"https://api.ethplorer.io/getTopTokenHolders/{token_id}?apiKey={api_key}&limit={limit}"

    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

# Example token ID (replace with the token ID you are interested in)
token_id = "0x60f99e81d7e9634d1de93af5301e3321c960a575"

# Get top 10 token holders
top_holders = get_top_token_holders(token_id)

if top_holders:
    print("Top Token Holders:")
    for holder in top_holders.get('holders', []):
        print(f"Address: {holder['address']}, Share: {holder['share']}%")
else:
    print("Failed to retrieve token holders.")
