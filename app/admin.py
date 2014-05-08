from django.contrib import admin
from app.models import * 
from app.forms import *
# Register your models here.

admin.site.register(Critic)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Review)
admin.site.register(Score)