from django.shortcuts import render

# Create your views here.
def index(request):

    document = [
        'Work Contract',
        'Work Reference',
        'Payslip 1',
        'Payslip 2',
        'Payslip 3',
        'Landlord Reference',
        'Bank Statement'
    ]

    context = {
        'document': document,
    }
    return render(request, 'tenant/index.html', context)