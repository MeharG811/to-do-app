from django.db import models

# Create your models here.

status_={
    "pending":"Pending",
    "inProgress":"In Progress",
    "compeleted":"Compeleted",    
    "Waitingfor_support":"Waiting For Support"
}


def status_Return():    
    return status_


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20, 
        choices=[(key, value) for key, value in status_.items()],
        default='pending'
    )
    
    def __self__(self):
        return self.title