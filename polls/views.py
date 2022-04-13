from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from random import randint
from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        allQ=Question.objects.all()
        count = 0
        random = randint(4, 5)
        q1 = Question.objects.get(pk=4)
        for q in allQ:
            q.random=0
            q.save()
            count+=1
        q1.random = random
        q1.count = count
        q1.save()
        return Question.objects.all()

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class CreateView(generic.DetailView):
    model = Question
    template_name = 'polls/create.html'

def create(request):    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/create.html')
    #return HttpResponse("Створи власну голосовалку")

def new(request, text):
    new=Question(question_text=text, pub_date=timezone.now())
    new.save()
    question = get_object_or_404(Question, pk=new.id)
    question.text=text
    return HttpResponseRedirect(reverse('polls:create', args=(new.text,)))


def vote(request, question_id):        
    question = get_object_or_404(Question, pk=question_id)
    allQ=Question.objects.all()
    allC=Choice.objects.all() 
    a = []
    max=-1
    min=10000
    sum=0
    try:
        all_choices = question.choice_set.all()
        selected_choice = question.choice_set.get(pk=request.POST['choice'])                 
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/results.html', {
            'question': question,
            'error_message': "Ви не вибрали кандидата",
        })
    else:  
        selected_choice.max = max
        selected_choice.min = min
        selected_choice.votes += 1
        selected_choice.sum = sum
        selected_choice.save()
       
        for choice in all_choices:
            choice.sum = sum
            choice.max = max
            choice.min = min
            a.append(choice.votes)
            a.append(selected_choice.votes)
            choice.save() 
        for i in a:
            if max<i:
                max=i
        for i in a:
            if min>i:
                min=i
        for choice in all_choices:
            sum+=choice.votes
            if choice.votes==max:
                choice.max = max
            if selected_choice.votes==max:
                selected_choice.max = max
            if choice.votes==min:
                choice.min = min
            if selected_choice.votes==min:
                selected_choice.min = min
            choice.save() 
            selected_choice.save()
        #Усього голосів:        
        selected_choice.sum = sum
        selected_choice.save()
        for choice in all_choices:
            choice.sum=sum
            choice.save()
        for choice in all_choices:
            choice.percent = (choice.votes * 100) / sum
            choice.save()
        sum=0
        for c in allC:
            sum+=c.votes    
        for q in allQ:
            q.sum=sum
            q.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

