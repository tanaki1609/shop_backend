from django.urls import path
from users.views import authorization_api_view, registration_api_view


urlpatterns = [
    path('authorization/', authorization_api_view),
    path('registration/', registration_api_view)
]
