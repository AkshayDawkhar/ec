from django.urls import path
from .views import PlaceDetails, PlaceView, index

urlpatterns = [
    # URL pattern for individual Place details API endpoints
    # Example: /api/places/1/
    path('api/places/<int:pk>/', PlaceDetails.as_view(), name='place-get-update-delete'),

    # URL pattern for listing and creating Places API endpoint
    # Example: /api/places/
    path('api/places/', PlaceView.as_view(), name='place-filter-list-create'),

    # URL pattern for rendering the 'index.html' template
    # This is the default URL, and it will be used when the root URL is accessed
    # Example: /
    path('', index, name='place'),
]
