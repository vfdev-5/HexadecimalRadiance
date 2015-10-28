from django.shortcuts import render


# Create your views here.
def main(request, template_name='main.html'):
    context={}
    return render(request, template_name, context)




def verification(request, template_name='verification.html'):
    context={}
    return render(request, template_name, context)

