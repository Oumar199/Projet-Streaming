# Importation de la librairie
# Importation of the library
from kafka import KafkaProducer

### for the kafka client initialisation
# client = kafka.KafkaClient(bootstrap_servers=['217.182.68.36:9092'])

producer = KafkaProducer(bootstrap_servers=['217.182.68.36:9092'], api_version = (2, 5, 0))
# producer = KafkaProducer(bootstrap_servers='217.182.68.36:9092')



message ='{"Year": 2007, "Month": 1, "DayofMonth": 26, "DayOfWeek": 5, "DepTime": "2144", "CRSDepTime": 2130, "ArrTime": "2309", "CRSArrTime": 2257, "UniqueCarrier": "US", "FlightNum": 1857, "TailNum": "N917UW", "ActualElapsedTime": "85", "CRSElapsedTime": "87", "AirTime": "67", "ArrDelay": "12", "DepDelay": "14", "Origin": "CLT", "Dest": "MCO", "Distance": 468, "TaxiIn": 6, "TaxiOut": 12, "Cancelled": 0, "Diverted": 0, "CarrierDelay": 0, "WeatherDelay": 0, "NASDelay": 0, "SecurityDelay": 0, "LateAircraftDelay": 0, "iata": "CLT", "airport": "Charlotte/Douglas International", "city": "Charlotte", "state": "NC", "country": "USA", "lat": 35.21401111, "long": -80.94312583, "Code": "US", "Description": "US Airways Inc. (Merged with America West 9/05. Reporting for both starting 10/07.)", "location": "35.21401111,-80.94312583"}'
# A la prochaine étape, envoyons les messages une par une
# To the next step, we send the messages one by one
# with open("data/flights.json", mode = "r") as f:
    # for i, line in enumerate(f):
        # Affichons le numéro de la ligne à chaque itération
        # Print the line number in each iteration
        # print(i)
        
        # Envoie du message avec le temps d'attente qu'il faut pour le message soit
        # complétement envoyé
        # Sending a message with a time out
producer.send("oumar_kane_streaming", value=bytes(message, encoding="utf8"))
producer.flush()

### to get the version of the api
# print(client.check_version())