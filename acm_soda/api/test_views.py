from acm_soda.views import dispatch_method


@dispatch_method
def test(request):
    return HttpReponse("test")

test = dispatch_method(test)