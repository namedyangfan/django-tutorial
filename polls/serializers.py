from rest_framework import serializers
from .models.Song   import Song
from .models.Market import Market


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "artist")

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ("internal_name", "display_name", "slug")