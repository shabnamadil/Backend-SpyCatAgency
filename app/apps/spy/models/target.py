from django.db import models
from django.forms import ValidationError
from utils.models.base_model import Base
from apps.spy.models import Mission

class Target(Base):
    """Model representing a target in the SpyCat agency."""

    name = models.CharField(max_length=100, verbose_name="Target Name")
    country = models.CharField(max_length=255, verbose_name="Target Country")
    notes = models.TextField(verbose_name="Notes", blank=True, null=True)
    is_completed = models.BooleanField(default=False, verbose_name="Target Completed")
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name="targets"
    )

    class Meta:
        verbose_name = "Target"
        verbose_name_plural = "Targets"
        unique_together = ('name', 'id', 'mission')

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.is_completed and self.mission.is_completed:
            raise ValidationError("Notes cannot be updated if the target and mission is completed.")