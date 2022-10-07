"""Users URLs."""

# Django
from django.urls import include, path

#Django rest framework
from rest_framework.routers import DefaultRouter


from .views import user as user_views

router = DefaultRouter()
router.register(r'user', user_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]
