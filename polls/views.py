from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from random import randint
from .models import Choice, Question
from django.utils import timezone
from .forms import UserForm

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

def create(request):
    submitbutton=request.POST.get("submit")
    
    newQuestion=''
    newCandidate1=''
    newCandidate2=''
    newCandidate3=''
    newCandidate4=''
    newCandidate5=''
    if request.method == 'POST':
        form= UserForm(request.POST or None)
        
        if form.is_valid():
            newQuestion= form.cleaned_data.get("Назва_категорії")
            newCandidate1= form.cleaned_data.get("Новий_кандидат_1")
            newCandidate2= form.cleaned_data.get("Новий_кандидат_2")
            newCandidate3= form.cleaned_data.get("Новий_кандидат_3")
            newCandidate4= form.cleaned_data.get("Новий_кандидат_4")
            newCandidate5= form.cleaned_data.get("Новий_кандидат_5")
        if submitbutton != None:        
            newQ=Question(question_text=newQuestion, pub_date=timezone.now())
            newQ.save()
            newC1=newQ.choice_set.create(choice_text=newCandidate1)
            newC2=newQ.choice_set.create(choice_text=newCandidate2)
            newC3=newQ.choice_set.create(choice_text=newCandidate3)
            newC4=newQ.choice_set.create(choice_text=newCandidate4)
            newC5=newQ.choice_set.create(choice_text=newCandidate5)
            newC1.save()
            newC2.save()
            newC3.save()
            newC4.save()
            newC5.save()
        return redirect(request.path)
    else:   
        form= UserForm(request.POST or None)
        
        context= {'form': form, 'Назва_категорії': newQuestion,
                'Новий_кандидат_1':newCandidate1, 'Новий_кандидат_2':newCandidate2, 
                'Новий_кандидат_3':newCandidate3, 'Новий_кандидат_4':newCandidate4, 
                'Новий_кандидат_5':newCandidate5, 
                'submitbutton': submitbutton,
                }
        return render(request, 'polls/new.html', context)