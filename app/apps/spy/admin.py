from django.contrib import admin

from apps.spy.models import Mission, SpyCat, Target

admin.site.register(SpyCat)
admin.site.register(Mission)
admin.site.register(Target)
