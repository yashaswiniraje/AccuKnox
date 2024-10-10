from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import time

# Pre-save Signal handler for User model
@receiver(pre_save, sender=User)
def pre_save_user_signal(sender, instance, **kwargs):
    print(f"Pre_Save Signal started for user: {instance.username}")
    start_time = time.time()  
    time.sleep(10)  
    end_time = time.time()  
    req_time = end_time - start_time  
    
    print(f"Time taken during Pre_Save: {req_time:.2f} seconds")
    print("Pre_Save signal processing finished.")

# Post-save Signal handler for User model
@receiver(post_save, sender=User)
def post_save_user_signal(sender, instance, **kwargs):
    print(f"Post_Save Signal started for user: {instance.username}")
    print("Post_Save signal processing finished.")


"""
#yashaswini is user created in database
Pre_Save Signal started for user: yashaswini
Time taken during Pre_Save: 10.00 seconds
Pre_Save signal processing finished.
Post_Save Signal started for user: yashaswini
Post_Save signal processing finished.
Time taken during Pre_Save: 10.00 seconds
Pre_Save signal processing finished.

"""
