from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from tracking.models import Ship, Position
from tracking.views import ShipView, PositionView
import json
import logging

logger = logging.getLogger('my_logger')

class AnimalTestCase(TestCase):
    def setUp(self):

        self.factory = APIRequestFactory()
        client = APIClient()

        ship_1 = Ship.objects.create(name="Evergreen", imo_number=12345678)

        Position.objects.create(
            ship=ship_1, 
            timestamp="2019-01-14T20:10:30Z", 
            latitude="17.7871608734131",
            longitude="69.5053863525391"
        )

        Position.objects.create(
            ship=ship_1, 
            timestamp="2019-01-14T20:11:30Z", 
            latitude="17.7871608734131",
            longitude="69.5053863525391"
        )
    
    def test_ship_endpoint(self):
        response = self.client.get("/api/ships/", format="json")

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(json.dumps(response.json()), [{'imo_number': 12345678, 'name': 'Evergreen'}])
        
    def test_ship_positions(self):
        response = self.client.get("/api/positions/12345678/", format="json")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(json.dumps(response.json()), 
                        {
                            'imo_number': 12345678, 
                            'name': 'Evergreen',
                            'position_set': [
                                {
                                    "timestamp":"2019-01-14T20:11:30Z", 
                                    "latitude": "17.7871608734131",
                                    "longitude": "69.5053863525391"
                                },
                                {
                                    "timestamp": "2019-01-14T20:10:30Z", 
                                    "latitude": "17.7871608734131",
                                    "longitude": "69.5053863525391"
                                },
                            ]    
                        })        
    
    def test_ship_position_timestamp(self):
        response = self.client.get("/api/positions/12345678/", format="json")
        self.assertEqual(response.status_code, 200)

        self.assertGreater(
            response.json()["position_set"][0]["timestamp"], 
            response.json()["position_set"][1]["timestamp"])
    
    def test_map_is_available(self):
        request = self.factory.get('/')
        response = ShipView.as_view()(request)
        self.assertEqual(response.status_code, 200)
