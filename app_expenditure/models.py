from django.db import models


class Expenditure(models.Model):
    CATEGORY_CHOICES = [
        ('HO', 'Housing'),
        ('FO', 'Food'),
        ('TR', 'Transport'),
        ('TRAV','Travel'),
        ('HE', 'Health'),
        ('ED', 'Education'),
        ('SH', 'Shopping'),
        ('CL', 'Clothing'),
        ('TAX', 'Tax'),
        ('LE',  'Leisure'),
        ('GIF', 'Gifts/Donations'),
        ('WO', 'Work'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('CR', 'Credit Card'),
        ('DE', 'Debit'),
    ]

    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        verbose_name='Category'
    )

    payment_method = models.CharField(
        max_length=2,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name='Payment Method'
    )

    credit_card = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Credit Card'
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

    year = models.PositiveIntegerField(
        verbose_name='Year',
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Title',
    )

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Value'
    )

    def __str__(self):
        return f'{self.title} - {self.get_category_display()} - {self.month}/{self.year}'

    class Meta:
        verbose_name = 'Expenditure'
        verbose_name_plural = 'Expenditures'
        ordering = ['-year', '-month', 'category']