from django.db import models
from django.utils.text import slugify
# from django.http import JsonResponse


class Role(models.Model):
    nama = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.nama)
        super(Role, self).save()

    def __str__(self):
        return "[{}] Role {}".format(self.id,self.nama)