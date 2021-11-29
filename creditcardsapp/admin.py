from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import *
from .forms import CreditCardsForm, HistoryCardForm
from import_export.admin import ImportExportModelAdmin
from datetime import datetime, timezone
import math


class CreditCardsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'seria', 'number', 'data_vipusk', 'data_okonchania', 'data_ispolzovania', 'summa', 'statuscard')
    form = CreditCardsForm



class HistoryCardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'id_card', 'who_buy', 'what_buy', 'price_tovar')
    form = HistoryCardForm



admin.site.register(CreditCards, CreditCardsAdmin)
admin.site.register(HistoryCard, HistoryCardAdmin)


admin.site.site_title = 'Админ панель CreditCards'
admin.site.site_header = 'Админ панель CreditCards'