from django.db import models
from django.utils import timezone

class Comments(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField()
    likes = models.IntegerField(default=0)  # ✅ Fixed default value
    img = models.ImageField(upload_to='img/', null=True, blank=True)
    post = models.ForeignKey('home.Post', on_delete=models.CASCADE, related_name="comments", null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)  # ✅ Default to current time

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"
