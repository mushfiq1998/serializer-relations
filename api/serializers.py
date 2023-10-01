from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    '''Add song filed that has been defined in models.py in ForeignKey
    relationship. It will show songs (title) assosiated with the singers'''
    # Show title of songs using StringRelatedField
    # song = serializers.StringRelatedField(many=True, read_only=True)

    # Show id of songs using PrimaryKeyRelatedField
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # Create clickable links for songs using HyperlinkedRelatedField
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, 
    #                                            view_name='song-detail')
    
    # SlugRelatedField is like StringRelatedField
    song = serializers.SlugRelatedField(many=True, read_only=True, 
                                        slug_field='title')
    # When slug_field='duration', it will show duration of song  
    # song = serializers.SlugRelatedField(many=True, read_only=True, 
    #                                     slug_field='duration')

    # Specify for every singer a single song as identity field
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        '''Add song filed that has been defined in models.py in ForeignKey
        relationship. It will show songs (id) assosiated with the singers'''
        fields = ['id', 'name', 'gender', 'song']