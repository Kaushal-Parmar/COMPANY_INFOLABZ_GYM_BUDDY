from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
payment_method=[
     ('credit_card', 'Credit_Card'),
     ('debit_card', 'Debit_Card'), 
     ('paypal', 'PayPal'),
     ('other', 'Other')
]

status=[
    ('pending', 'Pending'),
    ('completed','Completed'),
    ('failed','Failed')
]

class User(models.Model):
    name=models.CharField( max_length=50)
    f_name=models.CharField( max_length=50)
    l_name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    profile=models.ImageField( upload_to='profile')
    def profile_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.profile.url))

    profile_photo.allow_tags = True

class Country(models.Model):
    name=models.CharField( max_length=50)

class State(models.Model):
    country=models.ForeignKey("Country", on_delete=models.CASCADE)
    name=models.CharField( max_length=50)

class City(models.Model):
    state=models.ForeignKey("State", on_delete=models.CASCADE)
    name=models.CharField( max_length=50)

class Workout_category(models.Model):
    name=models.CharField( max_length=50)
    description=models.TextField()
    image=models.ImageField( upload_to='Workout_category')

    def workout_category(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    
    workout_category.allow_tags = True

class Workout_exercise(models.Model):
    title=models.CharField( max_length=50)
    description=models.TextField()
    category=models.ForeignKey("Workout_category", on_delete=models.CASCADE)
    video_url=models.URLField( max_length=200)
    difficulty=models.TextField()
    duration_in_min=models.DurationField()
    image=models.ImageField( upload_to='Workout_exercise')
    created_at=models.CharField( max_length=50)

    def workout_exercise(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    
    workout_exercise.allow_tags = True

class Subscription(models.Model):
    name=models.CharField( max_length=50)
    description=models.TextField()
    price_per_month=models.FloatField()
    is_active=models.BooleanField(verbose_name="Active Status")

class User_subscription(models.Model):
    user=models.ForeignKey("User", on_delete=models.CASCADE)
    plan=models.ForeignKey("Subscription", on_delete=models.CASCADE)
    start_date=models.DateField( auto_now=False)
    end_date=models.DateField( auto_now=False)
    is_active=models.BooleanField(verbose_name="Active Status")
    created_at=models.CharField( max_length=50)

class Payment(models.Model):
    user=models.ForeignKey("User", on_delete=models.CASCADE)
    amount=models.FloatField()
    payment_date=models.DateField( auto_now=False)
    payment_method=models.CharField(max_length=50, choices=payment_method)
    status=models.CharField( max_length=50,choices=status, default='pending')

class User_feedback(models.Model):
    user=models.ForeignKey("User", on_delete=models.CASCADE)
    subject=models.ForeignKey("Subscription", on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.CharField( max_length=50)

class Contactus(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    phone_no=models.CharField( max_length=10)
    message=models.TextField()
    created_at=models.CharField( max_length=50)

    



