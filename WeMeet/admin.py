from django.contrib import admin
from .models import *


admin.site.register(school)
admin.site.register(batch)
admin.site.register(student)
admin.site.register(ChatBatch)



# @admin.register(student)
# class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
#     ...
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "category":
#             kwargs["queryset"] = Category.objects.filter(name__in=['God', 'Demi God'])
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)