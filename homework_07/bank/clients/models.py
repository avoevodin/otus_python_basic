from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.middle_name if self.middle_name else '-'} {self.last_name}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(first_name={self.first_name}"
            f", middle_name={self.middle_name}"
            f", last_name={self.last_name})"
        )
