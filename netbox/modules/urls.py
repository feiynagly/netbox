from django.conf.urls import url

from extras.views import ObjectChangeLogView
from modules.models import Manufacturer, Module
from . import views

app_name = 'modules'
urlpatterns = [
    # Manufacturer

    url(r'^manufacturer/$', views.ManufacturerListView.as_view(), name='manufacturer_list'),
    url(r'^manufacturer/add/$', views.ManufacturerCreateView.as_view(), name='manufacturer_add'),
    url(r'^manufacturer/import/$', views.ManufacturerBulkImportView.as_view(), name='manufacturer_import'),
    url(r'^manufacturer/delete/$', views.ManufacturerBulkDeleteView.as_view(), name='manufacturer_bulk_delete'),
    url(r'^manufacturer/(?P<slug>[\w-]+)/edit/$', views.ManufacturerEditView.as_view(), name='manufacturer_edit'),
    url(r'^manufacturer/(?P<slug>[\w-]+)/changelog/$', ObjectChangeLogView.as_view(), name='manufacturer_changelog',
        kwargs={'model': Manufacturer}),

    # Module
    url(r'^module/$', views.ModuleListView.as_view(), name='module_list'),
    url(r'^module/add/$', views.ModuleCreateView.as_view(), name='module_add'),
    url(r'^module/import/$', views.ModuleBulkImportView.as_view(), name='module_import'),
    url(r'^module/delete/$', views.ModuleBulkDeleteView.as_view(), name='module_bulk_delete'),
    url(r'^module/(?P<slug>[\w-]+)/edit/$', views.ModuleEditView.as_view(), name='module_edit'),
    url(r'^module/(?P<slug>[\w-]+)/changelog/$', ObjectChangeLogView.as_view(), name='module_changelog',
        kwargs={'model': Module}),
]
