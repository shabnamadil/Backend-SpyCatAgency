from apps.spy.models import Mission, SpyCat, Target
from rest_framework import serializers, status


class CatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        fields = ["id", "name", "experience", "breed", "salary"]


class CatPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        fields = ["name", "experience", "breed", "salary"]


class TargetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "is_completed"]


class MissionListSerializer(serializers.ModelSerializer):
    targets = TargetListSerializer(many=True, read_only=True)

    class Meta:
        model = Mission
        fields = ["id", "is_completed", "cat", "targets"]


class MissionPostSerializer(serializers.ModelSerializer):
    targets = TargetListSerializer(many=True, write_only=True)
    cat = serializers.PrimaryKeyRelatedField(
        queryset=SpyCat.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Mission
        fields = ["id", "is_completed", "cat", "targets"]

    def validate_cat(self, value):
        if value is None:
            return value
        if value.missions.exists():
            raise serializers.ValidationError(
                "This SpyCat is already assigned to a mission."
            )
        return value

    def validate_targets(self, value):
        if not value:
            raise serializers.ValidationError("At least one target is required.")
        if len(value) > 3:
            raise serializers.ValidationError("A maximum of three targets is allowed.")
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission


class MissionUpdateSerializer(serializers.ModelSerializer):
    cat = serializers.PrimaryKeyRelatedField(
        queryset=SpyCat.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Mission
        fields = ["is_completed", "cat"]

    def validate_cat(self, value):
        if value is None:
            return value
        mission = self.instance
        try:
            if mission and value.missions.exclude(id=mission.id).exists():
                raise serializers.ValidationError(
                    "This SpyCat is already assigned to another mission."
                )
        except SpyCat.DoesNotExist:
            raise serializers.ValidationError(
                {"error": "Invalid SpyCat ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return value
