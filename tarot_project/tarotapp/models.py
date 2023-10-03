from django.db import models

class TarotCard(models.Model):
    number=models.IntegerField()
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)  # Store the image file name
    meaning = models.TextField()


    def __str__(self):
        return self.name
    