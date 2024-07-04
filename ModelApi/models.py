from django.db import models
# Create your models here.

class Company (models.Model):
    compney_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(("IT",'IT'),
                                                  ('Non IT','Non IT'),
                                                  ('Mobile Phones','Mobile Phones')))
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ReqModel (models.Model):
    name=models.AutoField(primary_key=True)
    continu=models.CharField(max_length=50)
    loca=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(("Mone",'Mone'),
                                                  ('Light','Light'),
                                                  ('Black','Black')))
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FeedbackForm (models.Model):
    Patientname=models.TextField(default='')
    Mobileno=models.TextField(default='')
    Disease=models.TextField(default='')

    def __str__(self):
        return self.name

class Blog (models.Model):
    BlogTitle=models.TextField(default='')
    BlogDiscription=models.TextField(default='')
    Photo=models.TextField(default='')
    Video=models.TextField(default='')

    def __str__(self):
        return self.name
    
    

class Video (models.Model):
    Video=models.TextField(default='')

    def __str__(self):
        return self.name

class Products (models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.TextField(default='')
    Price=models.IntegerField()
    Mrp=models.TextField(default='')
    Rating=models.TextField(default='')
    Img=models.TextField(default='')
    Description=models.TextField(default='')
