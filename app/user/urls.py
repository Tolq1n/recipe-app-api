"""
URL mappings for the user API
"""
from django.urls import path
from .views import CreateUserAPIView, CreateTokenView, ManageUserView

app_name = 'user'

urlpatterns = [
    path('create', CreateUserAPIView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
]
