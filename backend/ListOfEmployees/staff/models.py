from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(
        'имя',
        max_length=50
    )
    surname = models.CharField(
        'фамилия',
        max_length=50
    )
    patronymic = models.CharField(
        'отчество',
        max_length=50
    )
    phonenumber = PhoneNumberField(
        'номер телефона',
        db_index=True,
    )
    image = models.ImageField(
        'картинка'
    )
    date_of_birth = models.DateField(
        'дата рождения',
        max_length=8
    )
    ACTIVATED = 'AV'
    NOT_ACTIVATED = 'NA'
    DELETED = 'DL'
    STATUS_CHOICES = [
        (NOT_ACTIVATED, 'не активирован'),
        (ACTIVATED, 'активирован'),
        (DELETED, 'удалён'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_ACTIVATED,
    )

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.patronymic} | {self.get_status_display()}'