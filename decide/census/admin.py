from django.contrib import admin

from .models import Census
from .resources import CensusResources
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse


# class CensusAdmin(admin.ModelAdmin):
#     list_display = ('voting_id', 'voter_id')
#     list_filter = ('voting_id', )

#     search_fields = ('voter_id', )


# admin.site.register(Census, CensusAdmin)

#Metodo para exportar
def export_selected(modeladmin, request, queryset):
	census_resource = CensusResources()
	dataset = census_resource.export(queryset)
	response = HttpResponse (dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="census.csv"'
	return response
export_selected.short_description = 'Export selected as xls'

search_fields = ('voter_id', )


class CensusAdmin(ImportExportModelAdmin):
	resource_class = CensusResources
	list_display = ('voting_id', 'voter_id')
	list_filter = ('voting_id', )

	search_fields = ('voter_id', )
	#Se añade el metodo de export a la lista de acciones de django
	actions = [export_selected, ]

admin.site.register(Census, CensusAdmin)
