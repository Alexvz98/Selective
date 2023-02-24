from django.db import models



class Project(models.Model):
    profession = models.CharField(max_length=200)
    fio = models.TextField(null=True, blank=True)
    foto_image = models.ImageField(null=True, blank=True, upload_to='projects/%Y/%m/%d', default='default.jpg')
    instagram_url = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name