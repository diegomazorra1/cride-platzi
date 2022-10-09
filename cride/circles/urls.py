"""Circles URLs."""

from django.urls import include, path

# Views
from .views import circles as circle_views
from .views import membership as membership_views
# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
    membership_views.MembershipViewSet,
    basename='membership'
)
urlpatterns = [
    path('', include(router.urls))

]

