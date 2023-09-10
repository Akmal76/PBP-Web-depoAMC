from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Batu Bata',
        'amount': '69',
        'description': 'Salah satu bahan material sebagai bahan konstruksi'
    }

    return render(request, "main.html", context)