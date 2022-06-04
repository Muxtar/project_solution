from django.db import models

# Create your models here.
class ABS(models.Model):
    create_data = models.DateTimeField(auto_now=True)
    update_data = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Problems(ABS):
    title = models.CharField(max_length=40)
    difficulty = models.SmallIntegerField(choices=((1, 'Hard'), (2, 'Medium'), (3, 'Easy')))

    def __str__(self) -> str:
        return self.title

class ProblemDetail(ABS):
    problem = models.OneToOneField(Problems, related_name='problemdetail', on_delete=models.CASCADE)
    desc = models.TextField()

class Example(ABS):
    problem = models.ForeignKey(Problems, related_name='example', on_delete=models.CASCADE)
    inputData = models.CharField(max_length=30)
    outputData = models.CharField(max_length=30)

class BackTestExample(ABS):
    problem = models.ForeignKey(Problems, related_name='backtest', on_delete=models.CASCADE)
    inputData = models.CharField(max_length=30)
    outputData = models.CharField(max_length=30)

