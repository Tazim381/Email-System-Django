# Django Mailing System

## Introduction
This is a Django-based mailing system project that allows users to send emails directly from the website, rather than using an email application. Django provides a built-in emailing system that supports the SMTP protocol for handling email.

## How to Configure the Email System

1. **Import the send_mail function**:
   Make sure to import the `send_mail` function from Django's core email module:
   ```python
   from django.core.mail import send_mail


2. **Update settings.py**:  
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_USE_TLS = True  
EMAIL_PORT = 587  
EMAIL_HOST_USER ='your host email'  
EMAIL_HOST_PASSWORD = 'your password'  

## make a form in frondtend

## collect data and send the mail using send_mail function

## send mail function have those attribute  
send_mail(  
    "Subject here",  
    "Here is the message.",  
    "from@example.com",//come from host email that you configure into settings.py file  
    ["to@example.com"],//come from form  
    fail_silently=False,  
)  


