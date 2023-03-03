from django.urls import path
from users.views import AuthorizationAPIView, registration_api_view


urlpatterns = [
    path('authorization/', AuthorizationAPIView.as_view()),
    path('registration/', registration_api_view)
]
