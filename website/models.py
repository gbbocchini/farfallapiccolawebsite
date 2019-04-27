import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, SmartResize
from PIL import ImageFont, ImageDraw


# Create your models here.
class Watermark0(object):
    def process(self, img):
        draw = ImageDraw.Draw(img)
        draw.text((200, 200), "Farfalla Piccola", fill='white')
        return img


class Watermark1(object):
    def process(self, img):
        draw = ImageDraw.Draw(img)
        draw.text((500, 480), "Farfalla Piccola", fill='white')
        return img


# Album fotos Model
class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(500, 480), Watermark0()], format='PNG',
                                options={'quality': 100})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    # def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


# Model fotos de cada album
class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280, 960), Watermark1()], format='PNG',
                                options={'quality': 100})
    thumb = ProcessedImageField(upload_to='albums', processors=[SmartResize(500, 480), Watermark0()], format='PNG',
                                options={'quality': 80})
    descritivo_foto = models.CharField(max_length=70)
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.descritivo_foto


