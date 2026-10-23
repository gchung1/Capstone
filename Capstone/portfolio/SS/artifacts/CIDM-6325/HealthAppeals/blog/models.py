from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db import models


class PostQuerySet(models.QuerySet):
    """Custom queryset for Post with convenience filters."""

    def published(self):
        """Return posts with publish_date <= now (i.e., published)."""
        return self.filter(publish_date__lte=timezone.now())


class Category(models.Model):
    """Category for grouping blog posts (e.g., Tech, Lifestyle, Tutorials)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField(help_text="Markdown content")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    tags = TaggableManager(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # <--- Added field

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ["-publish_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        permissions = [("can_publish", "Can publish posts")]

    def save(self, *args, **kwargs):
        """Auto-generate slug if not set."""
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})