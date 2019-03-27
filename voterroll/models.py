from django.db import models


class VoterRoll(models.Model):
    state = models.CharField(max_length=2)
    source = models.CharField(max_length=30)


class VoterRecord(models.Model):
    roll = models.ForeignKey(VoterRoll, related_name="records", on_delete=models.PROTECT)
    source_id = models.CharField(max_length=40)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)   # for zip+4
    precinct_id = models.CharField(max_length=20)
    precinct_name = models.CharField(max_length=100)
