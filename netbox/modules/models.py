from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

from modules.constant import MODULE_RATE_CHOICES, MODULE_TYPE_CHOICE, TYPE_SFP, MODULE_STATUS_CHOICE, STATUS_IN_USE, \
    STATUS_CLASSES, MODULE_REACH_CHOICE, REACH_LR
from utilities.models import ChangeLoggedModel


@python_2_unicode_compatible
class Manufacturer(ChangeLoggedModel):
    """
    A Manufacturer represents a company which produces modules hardware; for example, Juniper or Cisco.
    """
    name = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        unique=True
    )
    description = models.CharField(
        max_length=200,
        unique=False,
        blank=True
    )

    csv_headers = ['name', 'slug', 'description']

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "{}?manufacturer={}".format(reverse('modules:manufacturer_list'), self.slug)

    def to_csv(self):
        return (
            self.name,
            self.slug,
            self.description
        )


@python_2_unicode_compatible
class Module(ChangeLoggedModel):
    """
    Module description
    """
    serial = models.CharField(
        max_length=30,
        unique=True
    )
    manufacturer = models.ForeignKey(
        to='modules.Manufacturer',
        on_delete=models.CASCADE,
        related_name='modules'
    )
    rate = models.IntegerField(
        choices=MODULE_RATE_CHOICES,
        default=10000
    )
    type = models.PositiveSmallIntegerField(
        choices=MODULE_TYPE_CHOICE,
        default=TYPE_SFP
    )
    reach = models.PositiveSmallIntegerField(
        help_text="SR/LR/ER/ZR",
        choices=MODULE_REACH_CHOICE,
        default=REACH_LR
    )
    status = models.PositiveSmallIntegerField(
        choices=MODULE_STATUS_CHOICE,
        default=STATUS_IN_USE
    )
    usage = models.CharField(
        max_length=266,
        unique=False,
        blank=True
    )
    slug = models.SlugField(
        unique=True
    )

    csv_headers = ['serial', 'manufacturer', 'rate', 'type', 'reach', 'status', 'usage', 'slug']

    class Meta:
        ordering = ['rate']

    def __str__(self):
        return self.serial

    def get_absolute_url(self):
        return "{}?module={}".format(reverse('modules:module_list'), self.slug)

    def to_csv(self):
        return (
            self.serial,
            self.manufacturer.name,
            self.rate,
            self.type,
            self.reach,
            self.status,
            self.usage,
            self.last_updated,
            self.slug
        )

    def get_status_class(self):
        return STATUS_CLASSES[self.status]

