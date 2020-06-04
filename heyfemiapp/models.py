from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    def __unicode__(self):
        return (self.Name)



class Post(models.Model):
    Title = models.TextField()
    Author = models.CharField(max_length=255)
    Date = models.DateTimeField()
    Description = models.TextField()
    Content = models.TextField()
    Image = models.ImageField(blank=True, upload_to="gallery")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, )

    class Meta:
        ordering = ('-Date',)



