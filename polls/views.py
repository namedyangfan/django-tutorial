from rest_framework import generics
from rest_framework import viewsets
from .models.Song   import Song
from .models.Market import Market
from .serializers   import SongsSerializer
from .serializers   import MarketSerializer


class ListSongsView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer

class ListMarketsView(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer