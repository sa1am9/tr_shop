from django.shortcuts import render
from .models import Board

def index(request):
    bbs = Board.objects.order_by('-published')
    return render(request,"shop/index.html",{"bbs":bbs})