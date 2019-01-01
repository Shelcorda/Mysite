from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify

# Create your models here.
#文章栏目
class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=True)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


#文章
class ArticlePost(models.Model):
    author = models.ForeignKey(User, related_name="article", on_delete=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, related_name='article_column', on_delete=True)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated", )
        index_together = (('id', 'slug'),) #对数据库这两个字段建立索引

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) #有插件插入：pip install awesome-slugify
        super(ArticlePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])