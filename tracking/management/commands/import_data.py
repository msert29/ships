import csv
from enum import Enum
from django.core.management.base import BaseCommand, CommandError
from tracking.models import Ship, Position


def get_ship_name(imo_number):
    imo_number = str(imo_number)
    if imo_number == "9632179":
        return "Mathilde Maersk"
    if imo_number == "9247455":
        return "Australian Spirit"
    if imo_number == "9595321":
        return "MSC Preziosa"

class Command(BaseCommand):
    help = 'Imports initial CSV data into SQLite database'

    def handle(self, *args, **options):
        with open("positions.csv") as positions:
            try :
                reader = csv.reader(positions)
                # First get unique ships
                ships_list = []
                ship_dicts = []

                for line in reader:
                    ship = list(filter(lambda x: x["imo_number"] == line[0], ship_dicts))
                    if len(ship) > 0:
                        ship[0]["positions"].append({
                            "timestamp": line[1],
                            "latitude": line[2],
                            "longitude": line[3]
                        })
                    else:
                        ship_dicts.append({
                            "imo_number": line[0],
                            "name": get_ship_name(line[0]),
                            "positions": [{
                                    "timestamp": line[1],
                                    "latitude": line[2],
                                    "longitude": line[3]
                                }]
                        })
                
                for ship in ship_dicts:
                    new_ship = Ship.objects.create(imo_number=ship["imo_number"], name=ship["name"])
                    for position in ship["positions"]:
                        Position.objects.create(
                                    timestamp=position["timestamp"], 
                                    latitude=position["latitude"],
                                    longitude=position["longitude"], 
                                    ship=new_ship
                                )
                self.stdout.write(self.style.SUCCESS("Successfully imported initial data"))
            
            except Exception as e:
                raise CommandError(f"Failed to import initial data, error: {e}")

