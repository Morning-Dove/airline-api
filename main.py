from fastapi import FastAPI

import json
from models import Flight, AirlineName


app = FastAPI()

with open("airlines.json", "r") as f:
    airlines: dict = json.load(f)

flights: dict[AirlineName, list[Flight]] = {}

for airline_name, flight_list in airlines.items():
    f_list: list[Flight] = []
    for flight in flight_list:
        f_list.append(Flight(**flight))
    flights[AirlineName(airline_name)] = f_list


# GET / -> list[airline_name]
@app.get("/")
async def get_airline_list() -> list[AirlineName]:
    return flights.keys()


# GET /:airline_name -> list[flight_num]
@app.get("/{airline_name}")
async def get_airline_flight(airline_name: AirlineName) -> list[str]:
    airline_flights = flights.get(airline_name, [])
    return [flight.flight_num for flight in airline_flights]


# GET /:airline_name/:flight_num -> Flight 
@app.get("/{airline_name}/{flight_num}")
async def get_flight(airline_name: AirlineName, flight_num: str) -> Flight:
    for flight in flights[AirlineName(airline_name)]:
        if flight.flight_num == flight_num:
            return flight


# POST /:airline 
@app.post("/{airline}")
async def create_flight(airline_name: AirlineName, flight: Flight) -> str:
    flights[airline_name].append(flight)
    return "Flight created."


# PUT /:airline/:flight_num
@app.put("/{airline}/{flight_num}")
async def update_flight(airline_name: AirlineName, flight_num: str, updated_flight: Flight) -> str:
    for flight in flights[AirlineName(airline_name)]:
        if flight.flight_num == flight_num:
            flight.capacity = updated_flight.capacity
            flight.estimated_flight_duration = updated_flight.estimated_flight_duration
            return "Flight updated."
    
    flights[airline_name].append(updated_flight)
    return "Flight created."

# DELETE /:airline/:flight_num
@app.delete("/{airline}/{flight_num}")
async def delete_flight(airline_name: AirlineName, flight_num: str) -> str:
    airline_flights = flights.get(airline_name, [])
    for i, flight in enumerate(airline_flights):
        if flight.flight_num == flight_num:
            airline_flights.pop(i)
            return "Flight deleted"

