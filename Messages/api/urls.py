from django.urls import path

from .views import *

urlpatterns = [
    path("messages/new/", createNewView.as_view(), name="polls_list"),
    path('messages/<country_code>/', detailsOfCountry.as_view()),

    path('messages/', viewMessages.as_view()),

]
