from django.contrib import admin
from .models import Fundraiser, Pledge

@admin.register(Fundraiser)
class FundraiserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'goal', 'is_open', 'owner', 'date_created')
    list_filter = ('is_open', 'date_created')
    search_fields = ('title', 'description', 'owner__username')

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'anonymous', 'fundraiser', 'supporter')
    list_filter = ('anonymous',)
    search_fields = ('comment', 'supporter__username')

# Register your models here.
