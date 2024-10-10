Question 1: Django signals executed synchronously or asynchronously?

Django signals are executed synchronously. 
ans:
This means when the signal is sent, the connected signal handler will be executed immediately in the same process
and the flow of code will wait for the signal handler to complete its task.
signal handler must be executed sequentially. So if there are multiple handlers, each handler will block the execution of the next handler until it completes
Example:
When a pre_save signal is triggered when saving a model, the signal handler runs and blocks further execution until it's completed.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Question 2: Do Django signals run in the same thread as the caller?

ans:
Yes,Django signals run in the same thread as the caller, when the signal is triggered, the handler is executed in the same thread as the action that triggered it.
Example :
Suppose you have a post_save signal that is triggered when a model instance is saved.
The code saving the instance and the signal handler that responds to this save event run in the same thread.
-------------------------------------------------------------------------------------------------------------------------------------------
Question 3: Do Django signals run in the same database transaction as the caller?

ans:
Yes, Django signals run in the same database transaction as the code that triggers them. If a signal handler raises an exception, 
it can cause the entire database transaction to be rolled back, including the changes made before the signal was triggered.
example:
If a signal is triggered during the saving of a model and an exception is raised in the signal handler, the changes in the database can be rolled back as part of the same transaction.
---------------------------------------------------------------------------------------------------------------------


related code is avalibale in "signals.py" file within "signal_app" app 
