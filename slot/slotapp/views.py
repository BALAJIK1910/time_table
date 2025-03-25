from django.shortcuts import render


def time_table(request):
    return render(request, "time_table.html")
