from django.urls import path
from location import views as location_view

urlpatterns = [
    path("place/", 
        location_view.UserLocation.as_view(),
        name="user_location"
    ),
    path("place/<int:pk>", 
        location_view.DeleteLocationId().as_view(),
        name="delete_location_id"
    ),
]