from django.db import models

class Tag(models.Model):
    machine_name = models.CharField(max_length=30)
    human_name = models.CharField(max_length=30)

class Thing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    widget = models.CharField(max_length=10000)
    big_image = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag, verbose_name="list of tags")
    karma = models.IntegerField()
    def __unicode__(self):
        return self.title

