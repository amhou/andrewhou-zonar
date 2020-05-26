# Zonar Dev Candidate Homework (cf1.0)

This is my solution for a "unique languages by region" API. This service contains one `GET` endpoint that accepts a region as input, and returns a list of unique official languages used in the countries of the selected region. It uses https://restcountries.eu as the data source.

This application is written in Python, using FastAPI and Docker. I chose FastAPI as an opportunity to try out a new lightweight Python webservice. I chose Docker for its ease of development and similarity to a real-world situation.

## Instructions

To run this project, make sure you have Docker installed.
- [Mac](https://www.docker.com/docker-mac)
- [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

I'm running `Docker version 19.03.8`, with `docker-compose version 1.25.0`.

Then, execute the following:

```
$ make && make start
```

This will build the image and start the app. In all, you will have one service running:

```
             Name                    Command        State         Ports
------------------------------------------------------------------------------
andrewhou-zonar_language_app_1   /start-reload.sh   Up      0.0.0.0:80->80/tcp

```

From here you can execute commands against the service.

```
$ curl localhost:80/region/europe
{
   "languages": [
       {
           "iso639_1": "ar",
           "iso639_2": "ara",
           "name": "Arabic",
           "nativeName": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
       },
       {
           "iso639_1": "az",
           "iso639_2": "aze",
           "name": "Azerbaijani",
           "nativeName": "az\u0259rbaycan dili"
       },
       ...
   ],
   "region": "asia"
}
```

## Tests

To run tests, execute the following:

```
$ make test
```
