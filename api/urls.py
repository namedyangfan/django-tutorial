from django.contrib import admin
from django.urls import path, re_path, include
from .router import router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include(router.urls))
]