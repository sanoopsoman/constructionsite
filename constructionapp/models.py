from django.db import models

from django.contrib.auth.models import AbstractUser


class Login(AbstractUser):
    usertype=models.CharField(max_length=40)
    ViewPassword=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.username

    
class Contractor(models.Model):
    constructor=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    idprof=models.ImageField(upload_to="gallery")
    address=models.CharField(max_length=100)
    # status=models.CharField(max_length=10,default="0")
    img=models.ImageField(upload_to="gallery")
    
    def __str__(self):
        return self.name
    
class Worker(models.Model):
    worker=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    wages=models.IntegerField(default=0)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    idprof=models.ImageField(upload_to="gallery")
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    wtype=models.CharField(max_length=100)
    img=models.ImageField(upload_to="gallery")
    def __str__(self):
        return self.name
    
class User1(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,null=True)
    wages=models.IntegerField()
    phone=models.CharField(max_length=100)
    age=models.IntegerField()
    img=models.ImageField(upload_to="gallery")
    address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Userworkrequest (models.Model):
    user=models.ForeignKey(User1,on_delete=models.CASCADE,null=True)
    cid=models.ForeignKey(Contractor,on_delete=models.CASCADE, null=True)
    worktype=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100)
    days=models.IntegerField(default=0)
    date=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    request=models.CharField(max_length=100)
    status=models.CharField(max_length=100,null=True,default='pending')
    payment=models.CharField(max_length=100,null=True,default='pending')
    
    
   

class AllotedWorks(models.Model):
    wid=models.ForeignKey(Worker,on_delete=models.CASCADE)
    uid=models.ForeignKey(User1,on_delete=models.CASCADE)
    cid=models.ForeignKey(Contractor,on_delete=models.CASCADE)
    rid=models.ForeignKey(Userworkrequest,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,default="process")
    payments=models.CharField(max_length=10,default="pending")
   
    
class Customerfeedback(models.Model):
    msg=models.TextField()
    uid=models.ForeignKey(User1,on_delete=models.CASCADE)
    cid=models.ForeignKey(Contractor,on_delete=models.CASCADE)
    wid=models.ForeignKey(Worker,on_delete=models.CASCADE)

class Workerfeedback(models.Model):
    msg=models.TextField()
    uid=models.ForeignKey(User1,on_delete=models.CASCADE)
    cid=models.ForeignKey(Contractor,on_delete=models.CASCADE)
    wid=models.ForeignKey(Worker,on_delete=models.CASCADE)
   
class Customerpayment(models.Model):
    uid=models.ForeignKey(User1,on_delete=models.CASCADE)
    wid=models.ForeignKey(Worker, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    cid=models.ForeignKey(Contractor,on_delete=models.CASCADE)
    amount=models.IntegerField()
    status=models.CharField(max_length=15,default="paid")
    
class Contractorpayment(models.Model):
    uid=models.ForeignKey(User1,on_delete=models.CASCADE)
    wid=models.ForeignKey(Worker, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    cid=models.ForeignKey(Contractor,on_delete=models.CASCADE)
    amount=models.IntegerField()
    status=models.CharField(max_length=15,default="paid")

    

