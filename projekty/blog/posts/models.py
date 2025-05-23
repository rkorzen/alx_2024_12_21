from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=10)
    posted_at = models.DateTimeField(blank=True, null=True)

    image = models.ImageField(upload_to="posts/%Y/%m/%d/", null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    production_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if self.status == "published" and not self.posted_at:
            self.posted_at = timezone.now()
        super().save(*args, **kwargs)


    def get_short_content(self):
        return self.content[:50] + "..." if len(self.content) > 50 else self.content