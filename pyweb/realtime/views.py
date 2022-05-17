from django.shortcuts import render
from django.views import View
from random import randint

class Index(View):
    def get(self, request):
        context = {'variable': str(randint(0,100))}
        return render(request, 'realtime/index.html', context)
