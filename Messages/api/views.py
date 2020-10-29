from .serializers import *
from rest_framework import generics
from Messages.models import *
from rest_framework import mixins
from rest_framework.response import Response
from .services import *
from rest_framework import status
from rest_framework.views import APIView
import requests
import json
from Messages.models import *
from django.shortcuts import get_object_or_404

mathdroidAPI = "https://covid19.mathdro.id/api/countries/"


class createNewView(generics.CreateAPIView):
    # lookup_field = 'country'
    queryset = MessagesFromAPI.objects.all()
    serializer_class = apiMessagesSerializer

    def post(self, request, *args, **kwargs):
        countryCode = self.request.data.get('country_code')
        api = self.request.data.get('api')
        restricted_countries = self.request.data.get('restricted_countries')
        test_required = self.request.data.get('test_required')
        content = self.request.data.get('content')
        url = mathdroidAPI+countryCode+"/"

        try:
            r = requests.get(url)
            data = r.json()
            print(data)
            serializer = apiMessagesSerializer(data={
                "confirmed": data['confirmed']['value'],
                "recovered": data['recovered']['value'],
                'deaths': data['deaths']['value'],
                # 'api': ['MathDroid', 'CDC'],
                'api': api,

                'country': countryCode,
                # 'restricted_countries': ['US', 'AF', 'GE', 'KE', 'LB', 'LT'],
                'restricted_countries': restricted_countries,
                'test_required': test_required,
                'content': content
                # 'test_required': "Yes"
            })
            if serializer.is_valid():
                # return Response("Data is saved for {}".format(countryCode))
                return Response("Data is saved successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Url doesn't work", status=r.status_code)


class viewMessages(generics.ListAPIView):
    queryset = MessagesFromAPI.objects.distinct(
        'country_id').order_by('country_id', '-timestamp')
    serializer_class = messagesSerializer


class detailsOfCountry(generics.RetrieveAPIView):
    lookup_field = 'country_code'
    queryset = MessagesFromAPI.objects.all()
    serializer_class = messagesSerializer

    def get_object(self, *args, **kwargs):
        country = self.kwargs.get('country_code')
        queries = self.queryset.filter(
            country__country_code=country)
        if queries:
            '''
            see here the usage of latest keyword. 
            '''
            return queries.latest('timestamp')


'''
Link to post: https://stackoverflow.com/questions/38869894/get-latest-object-with-filter-in-django-rest-framework

If you want to receive a detail list for a particular value
use this view. I am switching to Retrieve APIView to get only
one instance of the data.

***
Note: Here order_by is used instead of latest. As latest returns a single instance.

class detailsOfCountry(generics.ListAPIView):
    # lookup_field = 'country_code'
    # queryset = MessagesFromAPI.objects.all()
    serializer_class = messagesSerializer

    def get_queryset(self):
        country = self.kwargs['country_code']
        m = MessagesFromAPI.objects.filter(
            country__country_code__contains=country).order_by('-last_updated')
        return m


In the urls.py file, I am passing the argument using
    path('messages/<str:country_code>/', detailsOfCountry.as_view()),
'''

# Calling another view from a view
# Link: https://stackoverflow.com/questions/26790981/how-to-programmatically-call-a-django-rest-framework-view-within-another-view
