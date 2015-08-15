from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'puzzles/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'puzzles/detail.html', {'question': question})

