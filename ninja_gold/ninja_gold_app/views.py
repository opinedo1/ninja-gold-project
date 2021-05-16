from django.shortcuts import redirect, render, HttpResponse
import random
from datetime import datetime

# dictionary for our gold value ranges
GOLD_RANGES = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

# Create your views here.
def index(request):
    # sets our inital conditions for our mini game
    if not "gold_bal" in request.session or "activities" not in request.session:
        request.session['gold_bal'] = 0
        request.session['activities'] = []
    return render(request, "index.html")

def process_gold(request):
    if request.method == 'GET':
        return redirect("/")
    # checks which box was selected
    selected_building = request.POST['building']
    # assigns range depending on box selected
    gold_range_for_building = GOLD_RANGES[selected_building]
    # generates random number for that range
    gold_change = random.randint(gold_range_for_building[0], gold_range_for_building[1])

    activity_msg = "Earned {} gold from the {}!".format(gold_change, selected_building)
    # if convert sign is positve then casino will lose money
    result = "win"
    if selected_building == "casino":     
        convert_sign = random.randint(0,1)
        if convert_sign:
            gold_change = gold_change * -1
            activity_msg = "Entered a {} and lost {} gold... Ouch..".format(selected_building, gold_change)
            result = "lost"

    # append the date and time to our activity message
    activity_msg += " {}".format(datetime.now().strftime("%m/%d/%Y %I:%M%p"))

    # updates our session values
    request.session['gold_bal'] += gold_change
    request.session['activities'].append({"msg":activity_msg, "result":result})



    
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')