from datetime import datetime

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.contrib.auth.models import User

from acm_soda.api.models import *
from acm_soda.settings import SODA_FIFO_IN, SODA_FIFO_OUT

def external(request):
    inventories = Inventory.getEntireInventory()
    return render_to_response('external.html', {'request': request,
                                'inventories': inventories})
        
@login_required
def profile(request, username=''):
    # If no username was present in URL, load current user's profile
    if username == '':
        username = request.user.username
        real_user = request.user
    # Otherwise, load the profile of whichever user was listed
    else:
        real_user = User.objects.get(username=username)
        
    # If the currently logged in user is viewing his own page, show personal data
    if real_user == request.user:
        current_user = True
    else:
        current_user = False
    
    soda_user = MachineUser.objects.get(user=real_user)
    printable_balance = soda_user.balance/100.0
    
    # Grab all soda transactions
    try:
        transactions = SodaTransaction.objects.filter(user=real_user)
    except:
        transactions = None
        
    # Grab all admin transactions
    #TODO
    
    # Grab all available sodas
    #TODO: There is probably a way to do this w/ a Django model query
    available_inv = Inventory.objects.filter(amount__gte=1)
    available_sodas = []
    for inventory in available_inv:
        available_sodas.append(inventory.soda)
    
    return render_to_response('profile.html', {'request': request, 'user': soda_user, 
        'current_user': current_user, 'printable_balance': printable_balance,
        'transactions': transactions, 'available_sodas': available_sodas})

@login_required
def purchase(request): #TODO: Add exception handling!
    soda = None
    success = False
    
    if request.method == 'GET':
        pass #TODO: print out error message
    elif request.method == 'POST':
        #TODO: generate a purchase hash prior to submitting the form and check
        #that it matches w/ the GET request (send hash w/ form).  This will
        #give a unique purchase URL for each purchase to avoid accidental
        #or spamming purchases
        soda_name = request.POST['soda']
        soda = Soda.objects.get(short_name=soda_name)
    
        # Check that the user has enough money for the purchase
        machine_user = MachineUser.objects.get(user=request.user)
        if machine_user.balance >= soda.cost:
            avail_soda = Inventory.objects.filter(soda=soda, amount__gte=1)[0]
            vend_soda(avail_soda.slot)
            #TODO: figure out a better way to bail out
            
            # Don't record the transaction and deduct the account until everything else works
            purchase_trans = SodaTransaction(user=machine_user, amount=soda.cost,
                date_time=datetime.now(), description="Purchased a %s" % (soda.description),
                soda=soda)
            purchase_trans.save()
            avail_soda.amount -= 1
            avail_soda.save()
            machine_user.balance -= soda.cost
            machine_user.save()
            success = True
    return render_to_response('purchase.html', {'request': request,
        'soda': soda, 'success': success})

def vend_soda(slot_number):
    #Tell controller to vend
    if slot_number >= 0 and slot_number <= 7:
        fifo = open(SODA_FIFO_IN, 'w')
        fifo.write('%s' % slot_number)
        fifo.close()
    else:
        raise Exception('Invalid Soda Slot Number!')

    # Check w/ the controller that there was success
    fifo = open(SODA_FIFO_OUT, 'r')
    output = fifo.read(1)
    if int(output) == 1:
        fifo.close()
    else:
        fifo.close()
        raise Exception('Controller failed to vend!')

def profile_logout(request):
    return logout(request, '/web')
