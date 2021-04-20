from django.db import models
from django.utils.text import slugify
from django.utils import timezone

import os
from django.core.exceptions import ValidationError

def validate_file_dataset(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'FILE UPLOAD : Sorry, only available for extension .zip' )

class Dataset(models.Model):           
    name = models.CharField(max_length=255,default='')
    slugName = models.SlugField(blank=True, editable=False)
    description = models.TextField(default='')
    fileDataset = models.FileField(upload_to='dataset/zip', validators=[validate_file_dataset], null=True)

    #delete file from storege, if request UPDATE appear
    def deleteFileDataset(self, *args, **kwargs):
        self.fileDataset.delete()
        return JsonResponse('warning', safe=False)

    #delete file from storege, if request DELETE appear
    def delete(self, *args, **kwargs):
        self.fileDataset.delete()
        super().delete(*args, **kwargs)

    def save(self, **kwargs):
        self.slugName = slugify(self.name)
        super(Dataset, self).save()

    def __str__(self):
        return "[{}] Dataset {}".format(self.id,self.name)