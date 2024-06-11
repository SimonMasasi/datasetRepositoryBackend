from django.urls import include, path
from authentication.views import UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', UserViewSet.as_view()),
    path("users/<int:pk>/" , UserViewSet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)