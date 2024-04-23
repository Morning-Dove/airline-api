A simple REST API to track airlines and flights

# Airline API

## Pydantic

**Flight**

Attributes:

* flight_num (string)
* capacity (integer)
* estimated_flight_duration (integer)

**AirlineName**

Attributes:

* DELTA (Enum)
* SOUTHWEST (Enum)
* Alaska (Enum)


## REST Endpoints

Name                            | Method | Path
--------------------------------|--------|------------------
Retrieve airline_name collection| GET    | /
Retrieve flight_num collection  | GET    | /:airline_name
Retrieve flight member          | GET    | /:airline_name/:flight_num
Create flight member            | POST   | /:airline_name
Update flight member            | PUT    | /:airline_name/:flight_num
Delete flight member            | DELETE | /:airline_name/:flight_num