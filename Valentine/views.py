from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Happy valentine")

def name(request):
    return HttpResponse("my name is nuno")

def Bibek(request):
    return HttpResponse("<html> <style> table, th, td { border:1px solid black; } </style> <body> <h2>TD elements define table cells</h2> <table> <tr> <td>Emil</td> <td>Tobias</td> <td>Linus</td> </tr> </table> <p>To understand the example better, we have added borders to the table.</p> </body> </html>")