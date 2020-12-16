from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Questions

from django.template import loader


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
            }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404('Question does not exists')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("you're looking at the rsult of question %s."% question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on question  %s."% question_id)


