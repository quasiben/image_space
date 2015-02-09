from django.db import models

# # Create your models here.
class Images(models.Model):
    img_file_name = models.CharField(max_length=200)
    EXIF_LensSerialNumber = models.CharField(max_length=200)
    MakerNote_SerialNumberFormat = models.CharField(max_length=200)
    EXIF_BodySerialNumber = models.CharField(max_length=200)
    MakerNote_InternalSerialNumber = models.CharField(max_length=200)
    MakerNote_SerialNumber = models.CharField(max_length=200)
    Image_BodySerialNumber = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.img_file_name
