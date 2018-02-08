import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin

from .models import Genres, Films, Survey, Personality

def exportToCSV(modeladmin, request, queryset):
  opts = modeladmin.model._meta
  response = HttpResponse(content_type = 'text/csv')
  response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
  writer = csv.writer(response)

  fields = [field for field in opts.get_fields()
               if not field.many_to_many and not field.one_to_many]

  writer.writerow([field.verbose_name for field in fields])

  for obj in queryset:
    dataRow = []
    for field in fields:
      value = getattr(obj, field.name)
      if isinstance(value, datetime.datetime):
        value = value.strftime('%d/%m/%Y')
      dataRow.append(value)
    writer.writerow(dataRow)
  return response

exportToCSV.short_description = 'Export to CSV'

class SurveyAdmin(admin.ModelAdmin):
  actions = [exportToCSV]

class PersonalityAdmin(admin.ModelAdmin):
  actions = [exportToCSV]

# Register your models here.
admin.site.register(Genres)
admin.site.register(Films)
# admin.site.register(Survey)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Personality, PersonalityAdmin)
