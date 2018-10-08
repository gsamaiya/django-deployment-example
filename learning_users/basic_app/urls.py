from django.conf.urls import url
from .views import register, user_profile

app_name = 'basic_app'

urlpatterns = [
    url(r'^userform/', register, name='registration'),
    url(r'^profile/', user_profile, name='login'),
]