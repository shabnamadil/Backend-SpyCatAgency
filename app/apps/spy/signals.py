from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.spy.models import Target


@receiver(post_save, sender=Target)
def mark_mission_completed_if_all_targets_completed(sender, instance, **kwargs):
    all_targets_completed = all(
        target.is_completed for target in instance.mission.targets.all()
    )
    if all_targets_completed:
        instance.mission.is_completed = True
        instance.mission.save()
