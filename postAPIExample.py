from requests.auth import HTTPBasicAuth
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests

# create a BDD for this, given an url & endpoint when payload is provided then it should add a book in db

# this is roughly a testing thing as we are hitting the url only
# how it works behind the scene is called designing an API
# *** if you can create an API after seeing this, this will be called Test driven development ***

def check_book_addition():
    url = getConfig()['API']['endpoint'] + ApiResources.addBook
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer YOUR_JWT_TOKEN",
               "User-Agent": "Mozilla/5.0" }
    payload = addBookPayload("fefrewe")
    # only one auth is to be used
    user_auth = HTTPBasicAuth('rahulshettyacademy', getPassword())

    # make a post request to add book in DB with payload keys as columns
    add_book_response = requests.post(url, json=payload, headers=headers,
                                     verify=False, auth=user_auth)

    # as we are not familiar with the response API will be returning, we need to first check the content-type
    content_type = add_book_response.headers.get('Content-Type')

    # as we are not sure API requires auth, we can confirm the same through testing
    # though the most common way is to go through the API documentation
    auth_header = add_book_response.headers.get("WWW-Authenticate")
    if auth_header:
        print("Authentication is required. Method:", auth_header)

    if 'application/json' in content_type:
        # request library return a raw string and it is stored in a request object
        json_response = add_book_response.json()
        return add_book_response.status_code, "\t" + json_response['ID']
    else:
        return add_book_response.status_code, "\t Response type is not json"


# Delete Book -
bookId = check_book_addition()[1]
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                    json={"ID": bookId},
                                    headers={"Content-Type": "application/json"},
                                    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

#Authentication
url = "https://api.github.com/user"
github_response = requests.get(url, verify=False, auth=('rahulshettcademy', getPassword()))

print(github_response.status_code)
