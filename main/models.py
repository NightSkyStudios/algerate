from django.db import models
import uuid


# Create your models here.
class PostedImage(models.Model):
    image = models.ImageField("Image", upload_to='img')
    unique_link = models.UUIDField(default=uuid.uuid4, editable=False)
    isVerified = models.BooleanField('Verified', default=False)
    sex = models.CharField(max_length=225, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField(max_length=2)
    email = models.CharField(max_length=64)

    def __str__(self):
        return self.unique_link.__str__()


class Rating(models.Model):
    ratedImage = models.ForeignKey(PostedImage, on_delete=models.CASCADE)
    rating = models.IntegerField()
