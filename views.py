from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import login,logout
from .models import test,saved_test
# Create your views here.
def home(request):
    return render(request,'servey/homepage.html')

def signup(request):
    if request.method=='GET':
        return render(request,'servey/signup.html')
    else:
        username1=request.POST.get('username')
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        user=User.objects.create_user(username=username1,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        auth.login(request,user)
        return render(request,'servey/homepage.html')

def give_test(request):
    if request.method=='GET':
        questions=test.objects.all()
        return render(request,'servey/give_test.html',{'questions':questions})
    else:
        questions=test.objects.all()
        for question in questions:
            print('ids:',question.id)
            answer=request.POST.get(question.question)
            print(answer)
            if answer =='1':
                saveit=saved_test(question=question.question,answer=answer,user=request.user,optionA=question.optionA,optionB=question.optionB,optionC=question.optionC,optionD=question.optionD)
                saveit.save()
                answer=None
            elif answer == '2':
                saveit=saved_test(question=question.question,answer=answer,user=request.user,optionA=question.optionA,optionB=question.optionB,optionC=question.optionC,optionD=question.optionD)
                saveit.save()
                answer=None
            elif answer =='3':
                saveit=saved_test(question=question.question,answer=answer,user=request.user,optionA=question.optionA,optionB=question.optionB,optionC=question.optionC,optionD=question.optionD)
                saveit.save()
                answer=None
            elif answer == '4':
                saveit=saved_test(question=question.question,answer=answer,user=request.user,optionA=question.optionA,optionB=question.optionB,optionC=question.optionC,optionD=question.optionD)
                saveit.save()
                answerD=None
            
        return render(request,'servey/homepage.html',{'msg':'test completed'}) 

def result(request):
    count=0
    answers=test.objects.all()
    given_answers=saved_test.objects.filter(user=request.user)
    for answer in answers:
        for given_answer in given_answers:
            if answer.question==given_answer.question:
                if answer.answer==given_answer.answer:
                    count=count+1
    return render(request,'servey/result.html',{'count':count})

def view_test(request):
    questions=saved_test.objects.filter(user=request.user)
    questions1=test.objects.all()
    return render(request,'servey/view_test.html',{'questions':questions,'questions1':questions1})

def update_test(request):
    saved_questions=saved_test.objects.filter(user=request.user)
    questions=test.objects.all()
    for question1 in questions:
        for question in saved_questions:
            if question1.question==question.question:
                answer=request.POST.get(question.question)
                print(answer)
                if answer =='1':
                    question.answer=answer
                    question.save()
                    answer=None
                elif answer == '2':
                    question.answer=answer
                    question.save()
                    answer=None
                elif answer =='3':
                    question.answer=answer
                    question.save()
                    answer=None
                elif answer == '4':
                    question.answer=answer
                    question.save()
                    answer=None   
    return render(request,'servey/homepage.html',{'msg':'test completed'}) 

def login(request):
    if request.method=='GET':
        return render(request,'servey/login.html')
    else:
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            return render(request,'servey/login.html',{'error':'invalid'})

def logout(request):
    auth.logout(request)
    return redirect('home')














                


        

        