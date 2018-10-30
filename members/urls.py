from django.urls import path, include
from .views import MembersView

app_name = 'members'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', MembersView.as_view(), name='signup')
]