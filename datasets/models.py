from utils.baseModel import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
  
      
class Dataset(BaseModel):
    title = models.CharField(max_length=9000)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    downloads=models.IntegerField(default=0)
    viewers=models.IntegerField(default=0)
    total_files=models.IntegerField(default=14)

    def __str__(self):
        return self.title


class Tag(BaseModel):
    name = models.CharField(max_length=9000, unique=True)
    dataset = models.ForeignKey(Dataset , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class DatasetFolder(BaseModel):
    title = models.CharField(max_length=9000)

    def __str__(self):
        return self.title