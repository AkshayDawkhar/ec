from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Place
from .serializers import PlaceSerializer
from django.contrib.postgres.search import SearchQuery, SearchVector


class PlaceDetails(APIView):
    """
    API endpoint to handle individual Place details.

    Methods:
    - get: Retrieve details of a specific Place by its primary key (id).
    - put: Update details of a specific Place by its primary key (id).
    - delete: Delete a specific Place by its primary key (id).
    """

    def get(self, request, pk):
        """
        Retrieve details of a specific Place.

        Parameters:
        - request: The HTTP request object.
        - pk (int): The primary key of the Place to retrieve.

        Returns:
        - Response: HTTP response containing serialized Place data if found, or 404 NOT FOUND if not found.
        """
        try:
            place = Place.objects.get(id=pk)
        except Place.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        placeSerializer = PlaceSerializer(place)
        return Response(placeSerializer.data)

    def put(self, request, pk):
        """
        Update details of a specific Place.

        Parameters:
        - request: The HTTP request object.
        - pk (int): The primary key of the Place to update.

        Returns:
        - Response: HTTP response containing serialized updated Place data if valid, or 404 NOT FOUND if Place not found,
                    or 400 BAD REQUEST if the data provided is invalid.
        """
        try:
            place = Place.objects.get(id=pk)
        except Place.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        placeSerializer = PlaceSerializer(place, data=request.data)
        if placeSerializer.is_valid():
            placeSerializer.save()
            return Response(placeSerializer.data)
        return Response(placeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific Place.

        Parameters:
        - request: The HTTP request object.
        - pk (int): The primary key of the Place to delete.

        Returns:
        - Response: HTTP response with 204 NO CONTENT if Place is deleted successfully, or 404 NOT FOUND if Place not found.
        """
        try:
            place = Place.objects.get(id=pk)
        except Place.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaceView(APIView):
    """
    API endpoint to handle listing and creation of Places.

    Methods:
    - get: Retrieve a list of all Places or filter Places based on search query (q) parameter.
    - post: Create a new Place.
    """

    def get(self, request):
        """
        Retrieve a list of all Places or filter Places based on search query (q) parameter.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: HTTP response containing serialized list of Places data.
        """
        q = request.GET.get('q')
        if q:
            vector = SearchVector('name', 'description')
            query = SearchQuery(q)
            place = Place.objects.annotate(search=vector).filter(search=query)
        else:
            place = Place.objects.all()
        placeSerializer = PlaceSerializer(place, many=True)
        return Response(placeSerializer.data)

    def post(self, request):
        """
        Create a new Place.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: HTTP response containing serialized data of the newly created Place if valid,
                    or 400 BAD REQUEST if the data provided is invalid.
        """
        placeSerializer = PlaceSerializer(data=request.data)
        if placeSerializer.is_valid():
            placeSerializer.save()
            return Response(placeSerializer.data, status=status.HTTP_201_CREATED)
        return Response(placeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    """
    Render the 'index.html' template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Render: HTTP response rendering the 'index.html' template.
    """
    return render(request, 'index.html')
