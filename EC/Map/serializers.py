from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Place model.

    This serializer is used to convert Place model instances to JSON data and vice versa.

    Attributes:
    - model (Place): The Place model to serialize.
    - fields (list): The fields to include in the serialized representation.

    Example usage:
    ```python
    place = Place(name='Example Place', description='This is an example place', latitude=40.7128, longitude=-74.0060)
    serializer = PlaceSerializer(place)
    serialized_data = serializer.data
    ```
    """
    class Meta:
        model = Place
        fields = '__all__'
