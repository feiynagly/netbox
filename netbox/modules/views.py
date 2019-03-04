# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin

from modules import filters
from modules.models import Manufacturer, Module
from utilities.views import ObjectListView, ObjectEditView, BulkImportView, BulkDeleteView
from . import tables, forms


# Manufacturer
class ManufacturerListView(ObjectListView):
    queryset = Manufacturer.objects.all()
    table = tables.ManufacturerTable
    template_name = 'modules/manufacturer_list.html'


class ManufacturerCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'modules.add_manufacturer'
    model = Manufacturer
    model_form = forms.ManufacturerForm
    default_return_url = 'modules:manufacturer_list'


class ManufacturerEditView(ManufacturerCreateView):
    permission_required = 'modules.change_manufacturer'


class ManufacturerBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'modules.add_manufacturer'
    model_form = forms.ManufacturerCSVForm
    table = tables.ManufacturerTable
    default_return_url = 'modules:manufacturer_list'


class ManufacturerBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'modules.delete_manufacturer'
    queryset = Manufacturer.objects.all()
    table = tables.ManufacturerTable
    default_return_url = 'modules:manufacturer_list'


# Module
class ModuleListView(ObjectListView):
    queryset = Module.objects.all()
    filter = filters.ModuleFilter
    filter_form = forms.ModuleFilterForm
    table = tables.ModuleTable
    template_name = 'modules/module_list.html'


class ModuleCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'modules.add_module'
    model = Module
    model_form = forms.ModuleForm
    default_return_url = 'modules:module_list'


class ModuleEditView(ModuleCreateView):
    permission_required = 'modules.change_module'


class ModuleBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'modules.add_module'
    model_form = forms.ModuleCSVForm
    table = tables.ModuleTable
    default_return_url = 'modules:module_list'


class ModuleBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'modules.delete_module'
    queryset = Module.objects.all()
    table = tables.ModuleTable
    default_return_url = 'modules:module_list'
