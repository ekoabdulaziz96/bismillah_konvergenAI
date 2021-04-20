from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from django.contrib.auth import get_user_model
from .dataset import Dataset as ModelDataset
UserModel = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,null=True)
    dataset = models.ForeignKey(ModelDataset, on_delete=models.CASCADE,null=True)
           
    name = models.CharField(max_length=255,default='')
    slugName = models.SlugField(blank=True, editable=False)
    description = models.TextField(default='')
    isBooking = models.BooleanField(default=False)
    
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ['user', 'dataset']

    @property
    def isSoftDelete(self):
        return self.deleted_at != None

    #soft_deleted
    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(Task, self).delete()

    def save(self, **kwargs):
        self.slugName = slugify(self.name)
        super(Task, self).save()


    def __str__(self):
        return "[{}] Task {}".format(self.id,self.name)