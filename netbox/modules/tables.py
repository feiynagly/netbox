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
{{ value|date:"Y-m-d" }}
"""

STATUS_LABEL = """
<span class="label label-{{ record.get_status_class }}">{{ record.get_status_display}}</span>
"""


def get_table_cell_style(width_percentage=10):
    width_percentage = str(width_percentage)
    return {'th': {'style': 'text-align:center;width:' + width_percentage + '%'},
            'td': {'style': 'text-align:center;width:' + width_percentage + '%'}
            }


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
    serial = tables.Column(verbose_name='序列号', attrs=get_table_cell_style(12))
    manufacturer = tables.Column(verbose_name='厂商', attrs=get_table_cell_style(8))
    rate = tables.Column(verbose_name='速率', attrs=get_table_cell_style(8))
    type = tables.Column(verbose_name='类型', attrs=get_table_cell_style(6))
    reach = tables.Column(verbose_name='距离', attrs=get_table_cell_style(6))
    status = tables.TemplateColumn(template_code=STATUS_LABEL, verbose_name='状态',
                                   attrs=get_table_cell_style(8))
    usage = tables.Column(verbose_name="备注", attrs=get_table_cell_style(34))
    last_updated = tables.TemplateColumn(
        template_code=LAST_UPDATED_TIME,
        verbose_name='入库日期',
        attrs=get_table_cell_style(8)
    )
    actions = tables.TemplateColumn(template_code=MODULE_ACTIONS, attrs=get_table_cell_style(10),
                                    verbose_name='')

    class Meta(BaseTable.Meta):
        model = Module
        fields = ('pk', 'serial', 'manufacturer', 'rate', 'type', 'reach', 'status', 'usage', 'last_updated', 'actions')
