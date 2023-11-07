from django.contrib import admin

# Register your models here.
from .models import Golfer
from .models import Scores
from .models import FiveScores
admin.site.register(Golfer)
admin.site.register(FiveScores)
admin.site.register(Scores)
