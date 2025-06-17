from rest_framework import serializers

from apps.spy.models import SpyCat, Target, Mission


class CatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'experience', 'breed', 'salary']


class CatPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        fields = ['name', 'experience', 'breed', 'salary']


class TargetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_completed']


class MissionListSerializer(serializers.ModelSerializer):
    targets = TargetListSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = ['id', 'is_completed', 'cat', 'targets']


class MissionPostSerializer(serializers.ModelSerializer):
    targets = TargetListSerializer(many=True, write_only=True)
    cat = serializers.PrimaryKeyRelatedField(
        queryset=SpyCat.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Mission
        fields = ['id','is_completed', 'cat', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission