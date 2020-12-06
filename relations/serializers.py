from rest_framework import serializers
from relations.models import Album, Track, LocationExpire

class LocationExpireSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationExpire
        fields = ['order', 'location']

class TrackSerializer(serializers.ModelSerializer):
    locations = LocationExpireSerializer(many=True, read_only=True)
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration', 'locations']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']