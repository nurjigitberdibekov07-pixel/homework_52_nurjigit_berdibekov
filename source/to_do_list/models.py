from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]

    content = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Описание")

    status = models.CharField(max_length=100, null=False, blank=False,
                              choices=STATUS_CHOICES, default='new',verbose_name="Статус")

    due_date = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return self.content

    class Meta:
        db_table = "Задача"
        verbose_name = "Задача"