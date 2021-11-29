from django.db import models

# Create your models here.
class modelName(models.Model):
    productId = models.IntegerField()
    productName = models.CharField(max_length=20)
    payment = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.productName


class libraryModel(models.Model):
    studentUsn = models.CharField(max_length=20)
    studentName = models.CharField(max_length=20)
    loginTime = models.IntegerField()

    def __str__(self):
        return self.studentName
