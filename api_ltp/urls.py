
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from linktopay.views import LinkToPayViewSet

router = DefaultRouter()
router.register(r'linktopay', LinkToPayViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
