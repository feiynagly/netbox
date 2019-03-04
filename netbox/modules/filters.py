import django_filters
from django.db.models import Q

from extras.filters import CustomFieldFilterSet
from modules.constant import MODULE_RATE_CHOICES, MODULE_TYPE_CHOICE, MODULE_STATUS_CHOICE, MODULE_REACH_CHOICE
from modules.models import Manufacturer, Module
from utilities.filters import TagFilter


class ModuleFilter(CustomFieldFilterSet, django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search'
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='manufacturer__name',
        queryset=Manufacturer.objects.all(),
        label='Manufacturer',
        to_field_name='name'
    )
    rate = django_filters.MultipleChoiceFilter(
        choices=MODULE_RATE_CHOICES,
        null_value=None,
        label='Rate'
    )
    type = django_filters.MultipleChoiceFilter(
        choices=MODULE_TYPE_CHOICE,
        null_value=None,
        label='type'
    )
    reach = django_filters.MultipleChoiceFilter(
        choices=MODULE_REACH_CHOICE,
        null_value=None,
        label='reach'
    )
    status = django_filters.MultipleChoiceFilter(
        choices=MODULE_STATUS_CHOICE,
        null_value=None,
        label='status'
    )
    last_updated = django_filters.DateFromToRangeFilter()
    tag = TagFilter()

    class Meta:
        model = Module
        fields = ['q', 'serial', 'manufacturer', 'rate', 'type', 'reach', 'status', 'usage', 'last_updated']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(serial__icontains=value) |
            Q(usage__icontains=value)
        )
