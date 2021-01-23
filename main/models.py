from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60, default="Name")
    surname = models.CharField(max_length=60, default="Surname")
    patronymic = models.CharField(max_length=60, default="Patronymic")

    def __str__(self):
        return self.surname + " " + self.name + " " + self.patronymic


class Student(Person):
    year = models.IntegerField(default=1)


class Teacher(Person):
    pass


class Subject(models.Model):
    name = models.CharField(max_length=60, default="Subject")

    def __str__(self):
        return self.name


class Mark(models.Model):
    value = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)


