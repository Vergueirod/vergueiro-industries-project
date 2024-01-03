from django.db import models


class Revenue(models.Model):
    REVENUE_TYPES_CHOICES = [
        ('SAL', 'Salary'),
        ('BEN', 'Benefits'),
        ('OUT', 'Others'),
    ]

    revenue_types = models.CharField(
        max_length=3,
        choices=REVENUE_TYPES_CHOICES,
        default='OUT',
        verbose_name='Revenue Type'
    )

    MONTHS_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]

    month = models.PositiveIntegerField(
        verbose_name='Month',
        choices=MONTHS_CHOICES
    )

    year = models.PositiveIntegerField(verbose_name='Year')

    value_revenue = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        verbose_name='Value Revenue'
    )

    def __str__(self):
        return f'{self.get_revenue_types_display()} - {self.month}/{self.year}'

    class Meta:
        verbose_name = 'Revenue'
        verbose_name_plural = 'Revenues'
        ordering = ['year', 'month']


from django.db import models