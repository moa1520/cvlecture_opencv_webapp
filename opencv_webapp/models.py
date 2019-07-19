from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# Receive the pre_delete signal and delete the file associated with the model instance.


@receiver(pre_delete, sender=ImageUploadModel)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.document.delete(False)
