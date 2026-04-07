from django.db import models

from utils.models import CommonModel

class BlogCategory(CommonModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "blog_categories"
    
    def __str__(self):
        return self.name

class BlogTag(CommonModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "blog_tags"

    def __str__(self):
        return self.name

class Blog(CommonModel):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(BlogTag, related_name='blogs')

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/')
    short_description = models.CharField(max_length=500)

    description = models.TextField()

    class Meta:
        db_table = "blogs"

class BlogComments(CommonModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments')
   
    comment = models.TextField()

    class Meta:
        db_table = "blog_comments"