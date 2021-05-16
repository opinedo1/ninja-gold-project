from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    # sets our inital conditions for our mini game
    if not "gold" in request.session or "activities" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")

def process_gold(request):
    if request.method == 'GET':
        return redirect("/")

def reset(request):
    request.session.clear()
    return redirect('/')