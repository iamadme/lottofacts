# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Lotto(models.Model): 
  lotto_name = models.CharField(max_length=200)
  lotto_country = models.CharField(max_length=200)
  
class Draw(models.Model):
  lotto = models.ForeignKey(Lotto, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
  draw_number = models.DecimalField(max_digits=12, decimal_places=0)
  draw_result = models.TextField()
  message = models.TextField()
  top_prize = models.DecimalField(max_digits=12, decimal_places=0)
  
class Prizes(models.Model):
  lotto = models.ForeignKey(Lotto, on_delete=models.CASCADE)
  draw = models.ForeignKey(Draw, on_delete=models.CASCADE)
  winners = models.DecimalField(max_digits=9, decimal_places=0)
  match = models.TextField()
  prize_type = models.TextField()
  prize = models.DecimalField(max_digits=12, decimal_places=0)
