from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return '{"id": ' + str(self.id) + ', "name": "' + self.name + '"}'


class MagicWord(models.Model):
    index = models.IntegerField(unique=True)
    word = models.CharField(max_length=200, unique=True)
    message = models.CharField(max_length=200)
    recipient = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{"id": ' + str(self.id) + ',"word": "' + self.word + '"}'
