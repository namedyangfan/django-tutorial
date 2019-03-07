from polls.views    import ListSongsView
from polls.views    import ListMarketsView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('songs', ListSongsView)
router.register('markets', ListMarketsView)