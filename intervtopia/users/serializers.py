from rest_framework import serializers
from .models import CustomUser

class PreferenceSerializer(serializers.HyperlinkedModelSerializer):
    target_companys = serializers.StringRelatedField(many=True)
    target_positions = serializers.StringRelatedField(many=True)
    preferred_languages = serializers.StringRelatedField(many=True)
    availability = serializers.StringRelatedField(many = True)

    class Meta:
        model = CustomUser
        # fields = []
        fields = [
            'url', 
            'username', 
            'email', 
            'target_companys', 
            'target_positions', 
            'matchingStrategy', 
            'preferred_languages', 
            'preferred_difficulty',
            'availability', 
            'preferred_role',
            'rating'
        ]

