from django.db import models
from django.contrib.auth.models import User

class DGroups(models.Model):
    groupname = models.CharField(max_length=255)
    grouptotal = models.FloatField()
    groupmonthly = models.FloatField()
    groupcount = models.IntegerField()
    groupstatus = models.CharField(max_length=50)
    groupvisibilty = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.groupname}'

class GroupRules(models.Model):
    group = models.ForeignKey(DGroups, on_delete=models.CASCADE)
    rulename = models.CharField(max_length=50)
    booked = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.group.groupname} | {self.rulename}'

class Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membername = models.CharField(max_length=255)
    memberphone = models.CharField(max_length=50)
    memberid = models.CharField(max_length=50)
    memberstatus = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.membername}'

class GroupMembers(models.Model):
    grouprule = models.ForeignKey(GroupRules, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.member.membername} | {self.grouprule.rulename}'

class Required(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    requiredrule = models.ForeignKey(GroupRules, on_delete=models.CASCADE)
    requirementstatus = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.member.membername} | {self.requiredrule}'
