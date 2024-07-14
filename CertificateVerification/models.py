from django.db import models
from datetime import datetime

# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length=127)
    cert_id = models.CharField(max_length=50, unique=True)
    event = models.CharField(max_length=50)
    year = models.IntegerField(default=datetime.today().year)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Certificate, self).save(*args, **kwargs)

    def __str__(self):
        return self.cert_id

class Member(models.Model):
    name = models.CharField(max_length=127)
    father_name = models.CharField(max_length=127,null=True, blank=True)
    membership_num = models.CharField(max_length=63)
    email = models.EmailField()
    contributions = models.TextField()
    year = models.CharField(max_length=10)
    certificate_num = models.CharField(max_length=63, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.father_name = self.father_name.title()
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.membership_num