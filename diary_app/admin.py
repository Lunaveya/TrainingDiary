from django.contrib import admin

from .models import Exercise, Day, Done

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Day)
admin.site.register(Done)
