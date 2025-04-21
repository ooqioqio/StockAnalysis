# !/usr/bin/env python
# coding=utf-8
from django.db import models   

class stockInfo(models.Model):
    date = models.CharField('date', max_length=10)
    open = models.FloatField('open')
    close = models.FloatField('close')
    high = models.FloatField('high')
    low = models.FloatField('low')
    vol = models.IntegerField('vol')
    stockCode = models.CharField('stockCode', max_length=10)
    class Meta:
        db_table = 'stockInfo'
    