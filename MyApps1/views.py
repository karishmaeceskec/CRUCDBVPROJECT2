from django.shortcuts import render
from MyApps1.models import Employee
#from django.core.urlresolvers import reverse_Jazy #old-lib
from django.urls import reverse_lazy	#new-lib
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.
class EmployeeListView(ListView):
    model = Employee

class EmployeeDetailView(DetailView):
    model = Employee

class EmployeeCreateView(CreateView):
    model = Employee
    #fields=('empno', 'ename','job', 'sal')
    fields = '__all__'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ('ename', 'job', 'sal')

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('home')

from django.shortcuts import render, redirect
from MyApps1.forms import EmployeeForm
from MyApps1.models import Employee

# Create your views here.
def show_view(request):
    employees = Employee.objects.all()
    return render(request, 'MyApps1/index.html', {'employees': employees})

def insert_view(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request, "MyApps1/insert.html", {"form":form})


def delete_view(request,pk):        #use pk only here (same as url)
    employee=Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/index')

def update_view(request,pk):    #use pk only here(same as url)
    employee=Employee.objects.get(id=pk)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'MyApps1/update.html',{'employee':employee})



