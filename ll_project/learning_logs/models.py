from django.db import models

# Create your models here.
class Topic(models.Model):
    text=models.CharField(max_length=300)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateField(auto_now_add=True)

    class meta:
        verbose_name_plural='entries'
    
    def __str__(self) -> str:
        return f"{self.text[:50]}..."