from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.contrib.auth.models import User
import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_like_count(self):
        cache_key = f'post_like_count_{self.pk}'
        count = cache.get(cache_key)
        if count is None:
            count = self.likes.count()
            cache.set(cache_key, count)
        return count

    def __str__(self):
        return self.title

    def html(self):
        return markdown.markdown(self.text)


class Like(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache_key = f'post_like_count_{self.post.pk}'
        cache.incr(cache_key)

    def delete(self, *args, **kwargs):
        cache_key = f'post_like_count_{self.post.pk}'
        cache.decr(cache_key)
        super().delete(*args, **kwargs)
