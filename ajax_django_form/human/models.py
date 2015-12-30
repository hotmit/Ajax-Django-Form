from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _


class PunyHuman(models.Model):
    SEX_CHOICES = (
        ('male', _('Male')),
        ('female', _('Female')),
        ('other', _('Other')),
        ('yes_please', _('Yes please :D')),
    )

    name = models.CharField(max_length=70, verbose_name=_('name'))
    weight = models.DecimalField(null=True, blank=True, verbose_name=_('weight'), help_text=_('Weight in pounds.'),
                                 validators=[MinValueValidator(Decimal('0.01'))])
    birthday = models.DateField(verbose_name=_('birthday'))
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)

    level_of_hotness = models.PositiveSmallIntegerField(verbose_name=('level of hotness'),
                                                        help_text=_('Higher is hotter'),
                                                        validators=[MinValueValidator(1),
                                                                    MaxValueValidator(10),])
