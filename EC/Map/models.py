from django.db import models
from django.contrib.gis.db import models


class Place(models.Model):
    """
    Model representing a place.

    This model defines the attributes and behavior of a Place.

    Attributes:
    - name (CharField): The name of the place. Maximum length is 200 characters.
    - description (TextField): A detailed description of the place.
    - latitude (FloatField): The latitude coordinate of the place.
    - longitude (FloatField): The longitude coordinate of the place.
    - created_at (DateTimeField): The date and time when the place was created (auto-generated).

    Methods:
    - __str__: Returns a string representation of the Place object (the name of the place).

    Example usage:
    ```python
    # Create a new Place object
    place = Place(name='Example Place', description='This is an example place', latitude=40.7128, longitude=-74.0060)
    place.save()

    # Retrieve name of the place
    print(place.name)  # Output: 'Example Place'
    ```
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the Place object.

        Returns:
        - str: The name of the place.
        """
        return self.name


# class PlacePicker(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.PointField()
#
#     def __str__(self):
#         return self.name
