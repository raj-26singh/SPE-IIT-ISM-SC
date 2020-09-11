from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    reg_date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='event_poster')

    def __str__(self):
        return self.title