from django.contrib import admin

# Register your models here.
from activities.models import Activity, Session

admin.site.register(Activity)
admin.site.register(Session)