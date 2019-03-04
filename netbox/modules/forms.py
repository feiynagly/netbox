from django import forms
from django.forms import MultipleChoiceField, ModelChoiceField

from extras.forms import CustomFieldFilterForm
from modules.constant import MODULE_RATE_CHOICES, MODULE_TYPE_CHOICE, MODULE_STATUS_CHOICE, MODULE_REACH_CHOICE
from modules.models import Manufacturer, Module
from utilities.forms import SlugField, FilterChoiceField, CSVChoiceField, BootstrapMixin


# Manufacrurer Form
class ManufacturerForm(BootstrapMixin, forms.ModelForm):
    slug = SlugField(
        slug_source="name"
    )

    class Meta:
        model = Manufacturer
        fields = ['name', 'description', 'slug']


class ManufacturerCSVForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = Manufacturer.csv_headers
        help_texts = {
            'name': '厂商名称',
            'slug': 'URL-friendly slug',
        }


# Module Form
class ModuleForm(BootstrapMixin, forms.ModelForm):
    slug = SlugField(
        # 设置slug默认值
        slug_source="serial"
    )

    class Meta:
        model = Module
        fields = ['serial', 'manufacturer', 'rate', 'type', 'reach', 'status', 'usage', 'slug']


class ModuleCSVForm(forms.ModelForm):
    manufacturer = ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=True,
        to_field_name='name',
        help_text='厂商',
        error_messages={
            'invalid_choice': '该厂商不存在',
        }
    )
    rate = CSVChoiceField(
        choices=MODULE_RATE_CHOICES,
        required=True,
        help_text='速率',
    )
    type = CSVChoiceField(
        choices=MODULE_TYPE_CHOICE,
        required=True,
        help_text='模块封装类型',
    )
    reach = CSVChoiceField(
        choices=MODULE_REACH_CHOICE,
        required=True,
        help_text='模块传输距离类型'
    )
    status = CSVChoiceField(
        choices=MODULE_STATUS_CHOICE,
        required=True,
        help_text='当前模块使用状态'
    )

    class Meta:
        model = Module
        fields = Module.csv_headers

        help_texts = {
            'Serial': '模块序列号',
            'Manufacturer': '模块厂商',
            'slug': 'URL-friendly slug',
        }


class ModuleFilterForm(BootstrapMixin, CustomFieldFilterForm):
    model = Module
    q = forms.CharField(required=False, label='查找')
    manufacturer = FilterChoiceField(
        queryset=Manufacturer.objects.all(),
        # 定义检索字段对应Manufacturer对象的哪个字段
        to_field_name='name',
        null_label='-- None --',
        label='厂商'
    )
    rate = MultipleChoiceField(
        choices=MODULE_RATE_CHOICES,
        required=False,
        label='速率'
    )
    type = MultipleChoiceField(
        choices=MODULE_TYPE_CHOICE,
        required=False,
        label='封装'
    )
    reach = MultipleChoiceField(
        choices=MODULE_REACH_CHOICE,
        required=False,
        label='类型'
    )
    status = MultipleChoiceField(
        choices=MODULE_STATUS_CHOICE,
        required=False,
        label='状态'
    )
    # TODO: Change time_0 and time_1 to time_after and time_before for django-filter==2.0
    last_updated_0 = forms.DateField(
        label='起始日期',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'YYYY-MM-DD'}
        )
    )
    last_updated_1 = forms.DateField(
        label='截止日期',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'YYYY-MM-DD'}
        )
    )
