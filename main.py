# Pixela Habit Tracking - API Exercise


import requests
from pixela_data import TOKEN, USERNAME, GRAPH_ID
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#CREATING USER ON PIXELA
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN

}
# Creating the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"), #formatting data with strftime( string format time)
    "quantity": input("How many pages did you read today?"),

}


response = requests.post(url=pixel_endpoint, json=pixel_config, headers= headers)
print(response.text)
