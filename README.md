# Ships and Positions

docker-compose up -d --build to build the project using docker-compose which will bring up the PostgreSQL and django services.

Once these are up and running, its time for us to run the migrations. The following command can be issued to run the initial set of migrations:

> docker-compose run web python3 manage.py migrate

**Issues?**

Make sure the database service is up and running and that there are no errors apart from the migrate warning within web. This can be inspected via

>  docker logs <container_id>

Now, lets import the positions csv data to pull in somewhat meaningful data into our database.

> docker-compose run web python3 manage.py import_data

This will output a green success message if all goes to plan.

Some quicklinks:

[Display the map](127.0.0.1:8000/map) Does not load correctly due to mapbox API upgrades.
[Display Ships](127.0.0.1:8000/api/ships/)
[Display Positions for the Maersk](127.0.0.1:8000/api/positions/9632179/)
[Display Positions for the Austrailian](127.0.0.1:8000/api/positions/9247455/)
[Display Positions for the MSC](127.0.0.1:8000/api/positions/9595321/)