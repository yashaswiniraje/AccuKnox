from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import time
import threading
from django.db import transaction

#Question-1

@receiver(pre_save, sender=User)
def pre_save_user_signal(sender, instance, **kwargs):
    print(f"Pre_Save Signal started for user: {instance.username}")
    start_time = time.time()  
    time.sleep(10)  
    end_time = time.time()  
    req_time = end_time - start_time  
    
    print(f"Time taken during Pre_Save: {req_time:.2f} seconds")
    print("Pre_Save signal processing finished.")

@receiver(post_save, sender=User)
def post_save_user_signal(sender, instance, **kwargs):
    print(f"Post_Save Signal started for user: {instance.username}")
    print("Post_Save signal processing finished.")



#Question-2

import threading


@receiver(post_save, sender=User)
def user_post_save_handler(sender, instance, **kwargs):
    print(f"Signal Handler: Started for user: {instance.username}")
    time.sleep(5)
    print(f"Signal Handler Thread: {threading.current_thread().name}")
    print(f"Signal Handler: Completed for user: {instance.username}")

#Question -3


@receiver(post_save, sender=User)
def error_in_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal triggered for new user: {instance.username}")
        passlen = len(instance.username)

        with transaction.atomic():
            if passlen < 6:
                raise Exception("username is too small")

            print("User Successfully created")


"""
Output:

Pre_Save Signal started for user: yashaswini
Time taken during Pre_Save: 10.00 seconds
Pre_Save signal processing finished.
Post_Save Signal started for user: yashaswini
Post_Save signal processing finished.
Signal Handler: Started for user: yashaswini
Signal Handler Thread: Thread-11 (process_request_thread)
Signal Handler: Completed for user: yashaswini
Signal triggered for new user: yashaswini
User Successfully created
"""

#Task 4-  Topic: Custom Classes in Python

class Rectangle:
    def __init__(self, length: int, width: int):
        self.values = [{'length': length}, {'width': width}]
    
    def __iter__(self):
        return iter(self.values)
rect = Rectangle(10, 5)

for item in rect:
    print(item)


