from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class userAdmin(admin.ModelAdmin):
    list_display=('name','f_name','l_name','email','password' ,'profile')

@admin.register(Country)
class conutryAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(State)
class stateAdmin(admin.ModelAdmin):
    list_display=('country','name')

@admin.register(City)
class cityAdmin(admin.ModelAdmin):
    list_display=('state','name')

@admin.register(Workout_category)
class workout_categoryAdmin(admin.ModelAdmin):
    list_display=('name','description','image')

@admin.register(Workout_exercise)
class workout_exerciseAdmin(admin.ModelAdmin):
    list_display=('title','description','category','video_url','difficulty','duration_in_min','image','created_at')

@admin.register(Subscription)
class subscriptionAdmin(admin.ModelAdmin):
    list_display=('name','description','price_per_month','is_active')

@admin.register(User_subscription)
class user_subscriptionAdmin(admin.ModelAdmin):
    list_display=('user','plan','start_date','end_date','is_active','created_at')

@admin.register(Payment)
class paymentAdmin(admin.ModelAdmin):
    list_display=('user','amount','payment_date','payment_method','status')

@admin.register(User_feedback)
class user_feedbackAdmin(admin.ModelAdmin):
    list_display=('user','subject','message' ,'created_at')

@admin.register(Contactus)
class contactusAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_no','message' ,'created_at')

