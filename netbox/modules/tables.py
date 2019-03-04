#
# Manufacturers
#
import django_tables2 as tables

from modules.models import Manufacturer, Module
from utilities.tables import BaseTable, ToggleColumn

MODULEMANUFACTURER_ACTIONS = """
<a href="{% url 'modules:manufacturer_changelog' slug=record.slug %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.modules.change_manufacturer %}
    <a href="{% url 'modules:manufacturer_edit' slug=record.slug %}" class="btn btn-xs btn-warning"><i class="glyphicon 
    glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

MODULE_ACTIONS = """
<a href="{% url 'modules:module_changelog' slug=record.slug %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.modules.change_module %}
    <a href="{% url 'modules:module_edit' slug=record.slug %}" class="btn btn-xs btn-warning"><i class="glyphicon 
    glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

LAST_UPDATED_TIME = """
{{ value|date:"SHORT_DATETIME_FORMAT" }}
"""

STATUS_LABEL = """
<span class="label label-{{ record.get_status_class }}">{{ record.get_status_display}}</span>
"""


class ManufacturerTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name='Manafacture Name')
    description = tables.Column(verbose_name='Description')
    slug = tables.Column(verbose_name='Slug')
    actions = tables.TemplateColumn(template_code=MODULEMANUFACTURER_ACTIONS, attrs={'td': {'class': 'text-right'}},
                                    verbose_name='')

    class Meta(BaseTable.Meta):
        model = Manufacturer
        fields = ('pk', 'name', 'description', 'slug', 'actions')


class ModuleTable(BaseTable):
    pk = ToggleColumn()
    serial = tables.Column(verbose_name='序列号')
    manufacturer = tables.Column(verbose_name='厂商')
    rate = tables.Column(verbose_name='速率')
    type = tables.Column(verbose_name='类型')
    reach = tables.Column(verbose_name='距离')
    status = tables.TemplateColumn(template_code=STATUS_LABEL, verbose_name='状态')
    usage = tables.Column(verbose_name="备注")
    last_updated = tables.TemplateColumn(
        template_code=LAST_UPDATED_TIME,
        verbose_name='使用时间'
    )
    actions = tables.TemplateColumn(template_code=MODULE_ACTIONS, attrs={'td': {'class': 'text-right'}},
                                    verbose_name='')

    class Meta(BaseTable.Meta):
        model = Module
        fields = ('pk', 'serial', 'manufacturer', 'rate', 'type', 'reach', 'status', 'usage', 'last_updated', 'actions')
