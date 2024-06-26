from django.db import models
import uuid

# Create your models here.

# Create BaseModel
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True

# Create category field
class Category(BaseModel):
    category_name = models.CharField(max_length=100)

class Question(BaseModel):
    category = models.ForeignKey('Category', related_name='question')
    question = models.CharField(max_length=1000)
    marks = models.IntegerField(default=5)

class Answer(BaseModel):
    question = models.ForeignKey('Question', related_name='answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
