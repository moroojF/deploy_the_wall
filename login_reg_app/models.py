from django.db import models
import re 
from datetime import date, datetime, timedelta 

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        # isString = postData['first_name'].isalpha()

# and isString != True
        #checking first name 
        #empty string
        if len(postData['first_name']) == 0 :
            errors['first_name1'] = 'First name should not be empty'

        #characters less than 2
        if len(postData['first_name']) < 2 :
            errors['first_name2'] = 'First name should be at least 2 characters'

        #all alphabets 
        if ( not str.isalpha(postData['first_name'])) :
            errors['first_name3'] = 'First name should be letters only'

        #checking last name 
        #empty string
        if len(postData['last_name']) == 0 :
            errors['last_name1'] = 'Last name should not be empty'

        #characters less than 2
        if len(postData['last_name']) < 2 :
            errors['last_name2'] = 'Last name should be at least 2 characters'

        #all alphabets 
        if ( not str.isalpha(postData['last_name'])) :
            errors['last_name3'] = 'Last name should be letters only'
        
        #checking email
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        
        #checking password length more than 8
        if len(postData['password']) < 8:
            errors['password1'] = 'Password should be at least 8 characters'

        #password = confirm password
        if(postData['password'] != postData['cpassword']):
            errors['cpassword2'] = 'Passwords do not match'

        #birthday
        if (postData['BD'] == ''):
            errors['BD'] = "Please enter birthday"

        else:
            birthday_check = datetime.strptime(str(postData['BD']), '%Y-%m-%d').date()
            if ( birthday_check > date.today()):
                errors['BD1'] = "You can't register if you're born in the future!"

            elif birthday_check > (date.today() - timedelta(days=4745)):
                errors['BD2'] = "You can't register if you're younger than 13!"
        
        return errors


    def login_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['log_email']):
            errors['login'] = "Invalid email address!"
        
        if (len(postData['log_password']) < 8):
            errors['login'] = "Invalid password!"

        return errors

class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)

    birthday = models.DateField(default = '1900-01-01')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


    def __repr__(self):
        return f"\n<Users object: first name = {self.first_name}, last name = {self.last_name}, email = {self.email}>"

# _-----------------------------------------------------

