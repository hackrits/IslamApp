from django.contrib import admin
from .models import *

admin.site.register(DGroups)
admin.site.register(GroupRules)
admin.site.register(GroupMembers)
admin.site.register(Members)
admin.site.register(Required)
