# Module 3 Part B: Multi-Model Design

Extended Models
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'Comment by {self.author_name} on "{self.post.title}"'


Schema Diagram
+----------------------+
|       Post           |
+----------------------+
| id (PK)              |
| title : Char(200)    |
| body  : Text         |
+----------------------+
           ▲
           │ 1
           │
           │
           │ Many-to-One
           │
           ▼
+------------------------------+
|          Comment             |
+------------------------------+
| id (PK)                      |
| post_id (FK → Post.id)       |
| author_name : Char(100)      |
| body        : Text           |
+------------------------------+


Migration Notes
•	Add comment model with foreign key to post
•	Two related tables
o	Post holds blog posts (title and content)
o	Comment holds comments that belong to the posts
•	Created Comment model with fields: author_name, body, and post (foreign key to Post)
•	Established a one-to-many relationship: one post can have many comments


Assumptions and Business/Analytics Use
Adding comments allows readers to engage with blog content by leaving feedback or questions.
This feature supports analytics to track user interaction such as counting comments per post to measure traffic or engagement.
