import requests

# This method returns a string which is a random quote generated by le wagon breaking bad quote generator!
def breaking_quote():
    url = "https://breaking-bad.lewagon.com/v1/quotes"
    call = requests.get(url).json()
    response = f"{call['author']} says : {call['quote']}"
    return response
