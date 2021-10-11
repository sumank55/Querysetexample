from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("----------------------------------")
    print("Loged In signal...........Intro")
    print("sender",sender)
    print("request",request)
    print("User",user)
    
    print(f'kwargs:{kwargs}')

# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("----------------------------------")
    print("Loged Out signal...........Intro")
    print("sender",sender)
    print("Request",request)
    print("User",user)
    
    print(f'kwargs:{kwargs}')

# user_logged_out.connect(log_out, sender=User)


@receiver(user_logged_failed)
def login_failed(sender,request,user,**kwargs):
    print("----------------------------------")
    print("signal login failed...........Intro")
    print("sender",sender)
    print("credentials",credentials)
    print(f'kwargs:{kwargs}')

# user_logged_failed.connect(login_failed, sender=User)
