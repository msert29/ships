from django.urls import include, path
from . import views

urlpatterns = [
    path("map", views.index, name="map"),
    path("api/ships/", views.ShipView.as_view(), name="ships"),
    path("api/positions/<int:imo_number>/", views.PositionView.as_view(), name="positions"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]