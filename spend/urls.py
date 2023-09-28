from django.urls import path

from spend.views import spend_statistics

app_name = "spend"


urlpatterns = [
    path("spend/", spend_statistics)
]
