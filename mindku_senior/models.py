from django.db import models



class CompanyUser(models.Model):
    email = models.EmailField(max_length=128, unique=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    phone = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=256)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.email, self.name)

class CompanyAdmin(models.Model):
    company_user = models.ForeignKey(CompanyUser, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return '{}'.format(self.company_user)
    

class Customer(models.Model):
    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=128, null=False, blank=False)
    company = models.ForeignKey(CompanyUser, on_delete=models.SET_NULL, null=True)
    
    name = models.CharField(max_length=128, null=False, blank=False)
    birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE)
    phone = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=256)
    tutorial = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.email, self.name)
    

class Question_depression(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.content)
    
class Question_anxiety(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.content)
    
class Question_vitality(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.content)
    
class Question_suicide(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.content)
    
class Report(models.Model):
    CATEGORY_CHOICE = [
        ('DEP', 'Depression'),
        ('ANX', 'Anxiety'),
        ('VIT', 'Vitality'),
        ('SUI', 'Suicide')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    category = models.CharField( max_length=3 ,choices=CATEGORY_CHOICE)
    score = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} {} {}'.format(self.customer, self.category, self.score)

