# Text-Me-Where-to-Ski
 
This program traverses a CSV file that includes a couple of resorts and figures out the resort with the highest snowfall and texts a user the resort with the highest snowfall because the more snow a resort has, the better place it is to ski.

This program was made from a couple REST APIs:
* Dark Sky API
* Twilio API
* MapQuest API

### Dark Sky API

This API tracks the weather data given a geocode. The only data that is relevant to this API is the current snowfall accumulation of the resorts.

### MapQuest API

This API allows the program to get the geocode for each resort in the CSV file and the geocode will be used to get the data for finding the weather data.

### Twilio API

This API texts the number given by the user and informs the user of the resort with the largest snowfall.