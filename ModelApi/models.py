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


