from django.urls import path
from location import views as location_view

urlpatterns = [
    path("places/", 
        location_view.PlaceViewList.as_view(),
        name="place-list"
    ),
    path("place/<int:pk>", 
        location_view.DeleteLocationId().as_view(),
        name="delete-location-id"
    ),
    path("places/search/", 
        location_view.SearchPlacesView.as_view(),
        name="search-places"
    ),
]