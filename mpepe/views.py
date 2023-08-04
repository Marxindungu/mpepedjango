from django.shortcuts import render, redirect



def displaypay(request):
    return render(request, "pay.html")