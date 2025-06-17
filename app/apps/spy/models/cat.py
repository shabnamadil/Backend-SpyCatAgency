from django.core.exceptions import ValidationError
from django.db import models

from utils.base_model import Base


class SpyCat(Base):
    """Model representing a cat in the SpyCat agency."""

    BREED_CHOICES = [
        ("abyssinian", "Abyssinian"),
        ("american_bobtail", "American Bobtail"),
        ("american_curl", "American Curl"),
        ("american_shorthair", "American Shorthair"),
        ("balinese", "Balinese"),
        ("bengal", "Bengal"),
        ("birman", "Birman"),
        ("bombay", "Bombay"),
        ("british_shorthair", "British Shorthair"),
        ("burmese", "Burmese"),
        ("chartreux", "Chartreux"),
        ("colorpoint_shorthair", "Colorpoint Shorthair"),
        ("cornish_rex", "Cornish Rex"),
        ("devon_rex", "Devon Rex"),
        ("domestic_long_hair", "Domestic Long Hair"),
        ("egyptian_mau", "Egyptian Mau"),
        ("exotic_shorthair", "Exotic Shorthair"),
        ("havana_brown", "Havana Brown"),
        ("himalayan", "Himalayan"),
        ("japanese_bobtail", "Japanese Bobtail"),
        ("javanese", "Javanese"),
        ("korat", "Korat"),
        ("laperm", "LaPerm"),
        ("maine_coon", "Maine Coon"),
        ("manx", "Manx"),
        ("norwegian_forest_cat", "Norwegian Forest Cat"),
        ("ocicat", "Ocicat"),
        ("oriental", "Oriental"),
        ("persian", "Persian"),
        ("ragamuffin", "RagaMuffin"),
        ("ragdoll", "Ragdoll"),
        ("russian_blue", "Russian Blue"),
        ("scottish_fold", "Scottish Fold"),
        ("selkirk_rex", "Selkirk Rex"),
        ("siamese", "Siamese"),
        ("siberian", "Siberian"),
        ("singapura", "Singapura"),
        ("somali", "Somali"),
        ("sphynx", "Sphynx"),
        ("tonkinese", "Tonkinese"),
        ("turkish_angora", "Turkish Angora"),
        ("turkish_van", "Turkish Van"),
    ]

    name = models.CharField(max_length=100, unique=True, verbose_name="SpyCat Name")
    experience = models.PositiveIntegerField(
        default=0, verbose_name="Experience (in years)"
    )
    breed = models.CharField(choices=BREED_CHOICES, max_length=40, verbose_name="Breed")
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "SpyCat"
        verbose_name_plural = "SpyCats"

    def clean(self):
        if self.breed not in dict(self.BREED_CHOICES):
            raise ValidationError("It is not a valid breed choice.")

    def __str__(self):
        return self.name
