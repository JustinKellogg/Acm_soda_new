from acm_soda.views import dispatch_method
from django.http import HttpResponse

@dispatch_method
def test(request):
    return HttpResponse("test")

test = dispatch_method(test)