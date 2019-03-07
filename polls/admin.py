from django.contrib import admin
from .models.Song import Song
from .models.Market import Market

myModels = [Market, Song]
admin.site.register(myModels)
