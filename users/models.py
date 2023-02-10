from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# from lessons.models import Course


class CustomUser(AbstractUser):
    image = models.ImageField(
        "Изображение",
        upload_to='user_image/%Y/%m/%d',
        null=None,
        blank=True
    )
    # Todo: код взять с сайта метейн, обрати внимание на through = "Enrollment" подстрой под себя этот связующий
    #  класс я его под проэкт не подгонял

    # courses = models.ManyToManyField(
    #     Course,
    #     blank=True,
    #     verbose_name='Курсы на которые подписан пользователь',
    #     through = "Enrollment"
    # )

# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     date = models.DateField()   # дата поступления
#     mark = models.IntegerField(max_value=5)  # полученный балл
