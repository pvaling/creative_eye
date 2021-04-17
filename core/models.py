from django.db import models

# Create your models here.


class Creative(models.Model):
    label = models.TextField(blank=False)
    file = models.FileField(blank=False, upload_to='files/creatives')

    def __str__(self):
        return self.label


class CreativeLabeling(models.Model):
    creative = models.ForeignKey(to=Creative, blank=False, on_delete=models.CASCADE)
    labeling_data = models.TextField()  # Strange decision but ok for MVP

    labeling_source = models.CharField(choices=(('aws_rekognition', 'AWS rekognition'),), default='aws_rekognition', blank=False, max_length=128)

    def __str__(self):
        return "{label} ({source})".format(label=self.creative.label, source=self.get_labeling_source_display())
