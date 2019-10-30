from django.shortcuts import render, get_object_or_404, get_list_or_404,HttpResponseRedirect, HttpResponse
from .models import *
from django.views import generic
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')
#
#     return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/detail.html', {'question': question})
#
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice_value = question.choice_set.get(pk=request.POST['choice'])

    choice_value.votes += 1
    choice_value.save()

    return HttpResponseRedirect('result')

class ApiQuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ApiQuestionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer