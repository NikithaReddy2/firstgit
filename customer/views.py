from django.shortcuts import render,get_list_or_404,get_object_or_404
from customer.models import modelName
from customer.forms import formName
from customer.forms import libraryForm
from customer.forms import libraryModel
from django.urls import reverse_lazy

# Create your views here.
def thankyou(request):
    return render(request,'thankyou.html')


def user(request):
    form = formName

    if request.method == "POST":
        form = formName(request.POST)

        if form.is_valid():
            form.save()
            return thankyou(request)
        else:
            print("error form invalid")
    return render(request,'formpage.html',{'form':form})

def payment(request):
    test = get_list_or_404(modelName)
    print(test)
    return render(request,'display.html',{'display':test})

def update(request,num):
    test = get_object_or_404(modelName,id=num)
    if request.method == "POST":
        a = request.POST
        # print(a['ID'])
        test.productId = a['ID']
        test.productName = a['NAME']
        test.payment = a['Payment']
        test.address = a['ADDRESS']
        test.save()
        return render(request,'thankyou.html')

    return render(request,'update.html',{'display':test})



def student(request):
    form = libraryForm

    if request.method == "POST":
        form = libraryForm(request.POST)

        if form.is_valid:
            form.save()
            return thankyou(request)

    return render(request,'studentform.html',{'form':form})




def lib_rary(request):
    lib = get_list_or_404(libraryModel)
    return render(request,'displaylib.html',{'lib':lib})

def updatelib(request,num):

    lib = get_object_or_404(libraryModel,id=num)

    if request.method == "POST":
        a = request.POST
        lib.studentUsn = a['USN']
        lib.studentName = a['Name']
        lib.loginTime = a['LOG IN Time']
        lib.save()

        return lib_rary(request)

    return render(request,'updatelib.html',{'lib':lib})


def deletelib(request,num):

    libr = get_object_or_404(libraryModel,id=num)
    # print(libr)
    if request.method == "POST":
        libr.delete()
        # print("sucess")
        return lib_rary(request)
    return render(request,'delete.html')
