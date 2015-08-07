from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from translation.views import LanguageViewSet

router = DefaultRouter()
router.register(r'language', LanguageViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls))
]
