from django.shortcuts import render

# Create your views here.
def review(request):
    context = {}
    return render(request , 'review.html' , context)
