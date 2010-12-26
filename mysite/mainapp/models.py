from django.db import models

class Tag(models.Model):
    machine_name = models.CharField(max_length=30)
    human_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.human_name

class Thing(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    mini_desc = models.CharField(max_length=3000)
    widget = models.CharField(max_length=10000)
    big_image = models.CharField(max_length=10000)
    tags = models.ManyToManyField(Tag, verbose_name="list of tags")
    karma = models.IntegerField()
    def __unicode__(self):
        return self.title

