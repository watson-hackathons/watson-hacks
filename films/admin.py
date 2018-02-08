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

def exportMergedToCSV(modeladmin, request, queryset):
  opts = modeladmin.model._meta
  response = HttpResponse(content_type = 'text/csv')
  response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
  writer = csv.writer(response)

  fields = [field for field in opts.get_fields()
               if not field.many_to_many and not field.one_to_many]

  personalityOpts = Personality._meta
  pFields = [field for field in personalityOpts.get_fields()
               if not field.many_to_many and not field.one_to_many]

  writer.writerow([field.verbose_name for field in fields] +
                        [field.verbose_name for field in pFields])

  for obj in queryset:
    dataRow = []
    p = None
    for field in fields:
      value = getattr(obj, field.name)
      if field.name == 'film':
        p = Personality.objects.get(film=value)
      dataRow.append(value)
    if p:
      for field in pFields:
        value = getattr(p, field.name)
        dataRow.append(value)

    writer.writerow(dataRow)
  return response

exportMergedToCSV.short_description = 'Export Merged with Film Personalities to CSV'

class SurveyAdmin(admin.ModelAdmin):
  actions = [exportToCSV, exportMergedToCSV]

class PersonalityAdmin(admin.ModelAdmin):
  actions = [exportToCSV]

# Register your models here.
admin.site.register(Genres)
admin.site.register(Films)
# admin.site.register(Survey)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Personality, PersonalityAdmin)
