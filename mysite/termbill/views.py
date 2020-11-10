from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def bill(request):
    campusFee = 1144.95
    schoolFee = 104.75
    dbc = 119.99
    misc = 75.00
    CompFee = 171
    pirg = 11.2
    credits = 1
    tution = credits * 3950
    fees=campusFee+schoolFee+tution+dbc+misc+CompFee
    paid=0
    balance=fees-paid
    data = [
        {
            'ComputerFee': '$171.00',
            'PIRG': '$11.20',
            'CampusFee': '$1144.95',
            'SchoolFee': '$104.75',
            'TutionFees': str(tution),
            'DigitalBookCharge': '$8629.89',
            'MISC': '$75.00',
            'TotalCharges': str(fees),
            'TotalPayments': str(paid),
            'BalanceDue': str(balance)

         }
    ]
    context={
        'data':data
    }
    return render(request, 'termbill/termbill.html', context)
