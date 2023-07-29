from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Place


class PlaceViewTests(TestCase):
    def setUp(self):
        # Create a test client to simulate API requests
        self.client = APIClient()

        # Sample data for creating a test Place
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place',
            'latitude': 40.7128,
            'longitude': -74.0060,
        }

        # Create a test Place object in the database
        self.place = Place.objects.create(**self.place_data)

    def test_get_place_details(self):
        """Test retrieving place details using the 'GET' method."""
        url = reverse('place-get-update-delete', args=[self.place.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.place.name)
        # Add more assertions to check other fields if needed

    def test_get_place_details_not_found(self):
        """Test retrieving details for a non-existing place, which should return a 404 response."""
        url = reverse('place-get-update-delete', args=[999])  # Non-existing place ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_place_details(self):
        """Test updating place details using the 'PUT' method."""
        url = reverse('place-get-update-delete', args=[self.place.id])
        updated_data = {
            'name': 'Updated Place',
            'description': 'This place has been updated',
            'latitude': 35.6895,
            'longitude': 139.6917,
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])
        # Add more assertions to check other fields if needed

    def test_update_place_details_not_found(self):
        """Test updating details for a non-existing place, which should return a 404 response."""
        url = reverse('place-get-update-delete', args=[999])  # Non-existing place ID
        updated_data = {
            'name': 'Updated Place',
            'description': 'This place has been updated',
            'latitude': 35.6895,
            'longitude': 139.6917,
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_place(self):
        """Test deleting a place using the 'DELETE' method."""
        url = reverse('place-get-update-delete', args=[self.place.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Place.objects.filter(id=self.place.id).exists())

    def test_delete_place_not_found(self):
        """Test deleting a non-existing place, which should return a 404 response."""
        url = reverse('place-get-update-delete', args=[999])  # Non-existing place ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_places(self):
        """Test filtering places based on a search query parameter."""
        # Create more places with specific names and descriptions for the filtering test
        place2 = Place.objects.create(name='Place Test 2', description='This is another test place', latitude=0,
                                      longitude=0)
        place3 = Place.objects.create(name='Place Test 3', description='Yet another test place', latitude=0,
                                      longitude=0)

        url = reverse('place-filter-list-create')
        response = self.client.get(url, {'q': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Assuming there are other places in the database

    def test_create_place(self):
        """Test creating a new place using the 'POST' method."""
        url = reverse('place-filter-list-create')
        response = self.client.post(url, self.place_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Place.objects.filter(name=self.place_data['name']).exists())

    def test_create_place_invalid_data(self):
        """Test creating a new place with invalid data, which should return a 400 response."""
        invalid_data = {
            'name': 'Invalid Place',  # Missing 'description', 'latitude', and 'longitude'
        }
        url = reverse('place-filter-list-create')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
