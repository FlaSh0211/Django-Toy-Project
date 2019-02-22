from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, null=False) # 값이 없음 허용하지 않음
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]