from rest_framework import serializers
from movies.models import Movie, RatingTypes


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, blanck=True, null=True)
    rating = serializers.ChoiceField(choices=RatingTypes.choices, default=RatingTypes.G)
    synopsis = serializers.CharField(blank=True, null=True)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        ...
