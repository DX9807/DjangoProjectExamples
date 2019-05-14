from django.shortcuts import render
from pages.forms import UsersForm,StudentForm
# Create your views here.
def index(request):
    string='What is csrf_token????'

    return render(request,'index.html',{'string':string})


def user_login(request):
    form1=UsersForm()
    form2=StudentForm()
    if request.method=="POST":
        form1=UsersForm(request.POST)
        form2=StudentForm(request.POST)


    if form1.is_valid() and form2.is_valid():

        form1.save(commit=True)
        form2.save(commit=True)

        return index(request)

    else:
        print('Error Invalid form data...')


    return render(request,'user_login.html',{'form1':form1,'form2':form2})
