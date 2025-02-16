from django.urls import path
from .views import predicted_job

urlpatterns = [
    # path('', predicted_job, name='home'),
    path('prediction/', predicted_job, name='form'),
]
