from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from translation.views import LanguageViewSet
from translation.views import SentenceViewSet

router = DefaultRouter()
router.register(r'language', LanguageViewSet)
router.register(r'sentence', SentenceViewSet)

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
