from django.http import HttpResponse
from .models import Question, Answer, Punkty
from django.shortcuts import render, redirect
from .forms import NameForm


def index(request):
    punkty = Punkty.objects.get(pk=1)
    punkty.pkt=0
    punkty.save()
    return render(request, 'polls/index.html')

def question(request, pk):
    
    question2 = Question.objects.get(pk=pk)
    last = False
    if question2 == Question.objects.order_by('-id')[0]:
        last = True
        print("last")
    answers_list = Answer.objects.filter(question = question2)
    context = {'question': question2,
               'answers_list': answers_list,
               'last': last}
    return render(request, 'polls/question.html', context)

def check(request, pk):
    question = Question.objects.get(pk=pk)
    punkty = Punkty.objects.get(pk=1)
    if request.method == 'POST':
        if request.POST['odp'] == 'True':
            print("Pkt")
            punkty.pkt+=1
            punkty.save()
        else: print("Nie dostajesz pkt")
    else:
        print("NIE")
    
    if question == Question.objects.order_by('-id')[0]:
        context = {'punkty':punkty}
        return render(request,'polls/podsumowanie.html', context)
        
    else:
        return redirect('polls:question',question.get_next())

    
