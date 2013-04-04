from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from acm_soda.api.models import Inventory, MachineUser

def external(request):
    inventories = Inventory.getEntireInventory()
    return render_to_response('external.html', {'inventories': inventories})

@login_required
def profile(request):
    try:
        real_user = User.objects.get(username='request.user')
        soda_user = MachineUser.objects.get(user=real_user)
    except:
        soda_user = None
        real_user = None
    return render_to_response('profile.html', {'user': soda_user, 'request': real_user})

def profile_logout(request):
    return logout(request, '/web')