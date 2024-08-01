from django.db import models


class Task(models.Model):
    to_do = 'to_do'
    in_process = 'in_process'
    finished = 'finished'

    STATUS_CHOICES = [
        (to_do, 'to do'), 
        (in_process, 'in process'), 
        (finished, 'finished'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES, 
        default=to_do
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title