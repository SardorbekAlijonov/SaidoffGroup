from django.db import models


class WhyUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()



class Partners(models.Model):
    image = models.ImageField(upload_to='partners', null=False, blank=False)


class Teams(models.Model):
    name = models.CharField(max_length=50, null=False)
    profession = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='teams')


class Subscriber(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Certificates(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates', null=False, blank=False)

class Feedback(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=50, null=False)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='feedback')
    created_at = models.DateTimeField(auto_now_add=True)


class FAQ_Category(models.Model):
    title = models.CharField(max_length=50, null=False)


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    faq_category = models.ForeignKey(FAQ_Category, on_delete=models.CASCADE)

