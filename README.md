# Mobile Fuel Delivery
a Web Application for:
* Requesting Fuel so that Mobile Delivery Agents come to your location and fill your car fuel tank.
* Drivers with Fuel Tankers can register there and be hired.
* Monitoring this Logistic procces by always-ready-to-work Supervisors.

newest feature that has been added to the project is the ability to monitor users view map and geograpfic location. this features can be accessed through /map api.

# Requirements

* Install [Docker](https://docs.docker.com/engine/install/debian/) and [docker-compose](https://docs.docker.com/compose/install/) on your system


# Setup

```
cd FuelApp
sudo docker-compose up
```

if you changed requirements or dockerfile.base use `--build` flag


# Creating migrations
when your app is up with docker

```
sudo docker-compose exec webapp python manage.py makemigrations
```
