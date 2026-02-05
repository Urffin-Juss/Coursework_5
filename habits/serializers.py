from rest_framework import serializers, permissions

from habits.models import RelatedHabits




class RelatedHabitsSerializer(serializers.ModelSerializer):


    class Meta:
        model = RelatedHabits
        fields = '__all__'


    @staticmethod
    def validate_fields(data):
        is_pleasant = data.get('is_pleasant')
        reward= data.get('reward')

        if is_pleasant  is None and reward is None:
            raise serializers.ValidationError('You must select a reward or is_pleasant')

        elif is_pleasant and reward:
            raise serializers.ValidationError('You must select a reward or is_pleasant')





