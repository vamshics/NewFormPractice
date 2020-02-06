from django.shortcuts import render

# Create your views here.
def saveemp(request):
    empname = request.POST.get('empname1')
    empemail = request.POST.get('empemail')
    empcontact = request.POST.get('empcontact')
    empimg = request.POST.get('empimage')
    ss = (empname,empemail,empcontact,empimg)
    ss.save()
    return redirect()