from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json
from .models import *

def apis(request):
    groups = serializers.serialize('json',DGroups.objects.all())
    grouprules = serializers.serialize('json',GroupRules.objects.all())
    member = serializers.serialize('json',Members.objects.all())
    groupmembers = serializers.serialize('json',GroupMembers.objects.all())
    required = serializers.serialize('json',Required.objects.all())
    dtapis = {'groups': groups,
            'grouprules': grouprules,
            'member': member,
            'groupmembers': groupmembers,
            'required': required,
            }
    return JsonResponse(dtapis,safe=False, status=201)
