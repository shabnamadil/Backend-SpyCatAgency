from django.db import models

from apps.spy.models import SpyCat
from utils.base_model import Base


class Mission(Base):
    is_completed = models.BooleanField(default=False, verbose_name="Mission Completed")
    cat = models.ForeignKey(
        SpyCat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="missions",
    )

    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Missions"

    def __str__(self):
        return f'{"Mission by " + self.cat.name if self.cat else "Unknown Cat"}  - {"Completed" if self.is_completed else "In Progress"}'
