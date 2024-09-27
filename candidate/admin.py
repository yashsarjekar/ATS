from django.contrib import admin
from candidate.models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone_number', 'email')
    search_fields = ('email', 'name')
admin.site.register(Candidate, CandidateAdmin)
