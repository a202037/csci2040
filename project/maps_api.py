import gmplot
import requests

#load the data and initialize the values


## Getting data and filtering
## Please register your key and design the correct query
key = "Key"
query = 

# you might want a for loop to send and receive the query
url = "https://maps.googleapis.com/maps/api/distancematrix/json?" + query
res = requests.get(url).json()



#plotting using gmplot
