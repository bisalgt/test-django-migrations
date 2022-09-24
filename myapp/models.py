from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__gte=1),
                name="Age should not be less than one"
            )
        ]