from django.shortcuts import render
from django.views.generic import ListView
from .models import News

index = ListView.as_view(model=News)