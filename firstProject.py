import requests
from json import *
from csv import *
from twilio.rest import Client

# API keys
geocode_API_key = "your_api_key"
dark_sky_API_key = "your_api_key"

account_sid = "your_account_id"
auth_token = 'your_token'
client = Client(account_sid, auth_token)

filename = input("Enter the name of the file that contains the ski resorts: ")
number = input("What is your phone number? (Numbers only)\n")

# Read the list of resorts and create a new file called out.csv that holds the results for the snowfall
with open(filename, 'r', encoding='utf-8') as f:

    with open('out.csv', 'w', encoding='utf-8') as out:
        writefile = writer(out)
        readfile = reader(f)

        writefile.writerow(['resort_name','city','state'])
        f.readline()
        for row in readfile:
            location = row[0]
            print(f"Fetching data for {location}...")

            geocode = {'key': geocode_API_key, 'location': f"{row[0]},{row[1]},{row[2]}"}
            locationURL = "http://www.mapquestapi.com/geocoding/v1/address"
            geocode_request = requests.get(locationURL, params=geocode)
            geocode_data = geocode_request.json()
            latitude = geocode_data['results'][0]['locations'][0]["latLng"]['lat']
            longitude = geocode_data['results'][0]['locations'][0]["latLng"]['lng']

            snowfallURL = f"https://api.darksky.net/forecast/{dark_sky_API_key}/{latitude},{longitude}"
            weather_request = requests.get(snowfallURL)
            weather_data = weather_request.json()
            if weather_data["currently"]['precipIntensity'] != 0 and weather_data['currently']['precipType'] == 'snow':
                amount_of_snow = weather_data['currently']['precipAccumulation']
            else:
                amount_of_snow = 0

            print(amount_of_snow)

            writefile.writerow([row[0], row[1], row[2], amount_of_snow])


place = ''
highest_snowfall = 0

# Search the resorts for the largest amount of snowfall
with open('out.csv', 'r', encoding='utf-8') as file:
    outfile = reader(file)
    file.readline()
    for line in outfile:
        if float(line[3]) > highest_snowfall:
            highest_snowfall = float(line[3])
            place = line[0]
    if place == '':
        print("None of the resorts are snowing right now.")
    else:
        print(f"{place} has the most potential snow with {highest_snowfall} inches.")

# Text the number that was given in the beginning to alert the user of the resort with the highest snowfall
message = client.messages.create(
    to=number,
    from_="+14806464017",
    body=f"{place} has the most potential snow with {highest_snowfall} inches."
)
