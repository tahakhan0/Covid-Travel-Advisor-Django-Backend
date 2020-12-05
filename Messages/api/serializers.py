from rest_framework import serializers

from Messages.models import *


class countrySerializer (serializers.):
    class Meta:
        model = Country
        fields = ("name", "country_code")


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = APIs
        fields = ("name", "url")


# class bulkMessagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = bulkMessages
#         fields = "__all__"


class StringListField(serializers.ListField):
    child = serializers.CharField()


class messagesSerializer(serializers.ModelSerializer):
    restricted_countries = serializers.SlugRelatedField(many=True,
                                                        slug_field="name", queryset=Country.objects.all())

    country = countrySerializer(read_only=True)
    get_last_updated_date = serializers.ReadOnlyField()

    # api = serializers.SlugRelatedField(
    #     slug_field='url', many=True, queryset=APIs.objects.all())
    api = APISerializer(many=True, read_only=True)
    # messages = bulkMessagesSerializer(many=True)
    # content = serializers.ReadOnlyField()

    class Meta:
        model = MessagesFromAPI
        fields = ('id', 'country', 'api', 'restricted_countries',
                  'confirmed', 'deaths', 'recovered', 'content', 'test_required', 'get_last_updated_date')


class apiMessagesSerializer(serializers.ModelSerializer):
    # country = CreatableSlugRelatedField(
    #     many=False, slug_field='country_slug', queryset=Country.objects.all()
    # )
    country = serializers.SlugRelatedField(
        slug_field="country_code", queryset=Country.objects.all())

    api = serializers.SlugRelatedField(
        slug_field='name', many=True, queryset=APIs.objects.all())

    restricted_countries = serializers.SlugRelatedField(many=True,
                                                        slug_field="name", queryset=Country.objects.all())

    class Meta:
        model = MessagesFromAPI
        fields = ('test_required', 'confirmed', 'deaths', 'recovered',
                  'country', 'restricted_countries', 'api', 'content')
