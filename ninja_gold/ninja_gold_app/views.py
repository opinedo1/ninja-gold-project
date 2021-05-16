from django.shortcuts import redirect, render, HttpResponse
import random

GOLD_RANGES = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

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
    # checks which box was selected
    selected_building = request.POST['building']
    print("selected building:", selected_building)
    # assigns range depending on box selected
    gold_range_for_building = GOLD_RANGES[selected_building]
    print('gold range: ', gold_range_for_building)
    # generates random number for that range
    gold_change = random.randint(gold_range_for_building[0], gold_range_for_building[1])
    print('gold received: ', gold_change)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')