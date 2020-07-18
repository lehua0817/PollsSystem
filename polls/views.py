from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from polls.models import Question


def index(request):
    # 获取最新的5个问题
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # 下面两种写法是等价的

    # 写法一
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    # 写法二
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)

    choice_list = question.choice_set.all()
    # 获取
    template = loader.get_template('polls/question_detail.html')
    context = {
        'question': question,
        'choice_list': choice_list,
    }
    return HttpResponse(template.render(context, request))


def result(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
