from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import SubscriptionPlan, Subscription


@login_required
def user_subscription_plans(request):
    """ Fetch subscription plans specific to the logged-in user """
    plans = SubscriptionPlan.objects.filter(user=request.user).values('id', 'name', 'price', 'duration_days')
    return JsonResponse({"plans": list(plans)})

@login_required
def select_subscription(request):
    """ Allow the logged-in user to select one of their available subscription plans """
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        plan = get_object_or_404(SubscriptionPlan, id=plan_id)

        # Create subscription
        Subscription.objects.create(user=request.user, plan=plan)
        
        # Redirect to subscription history page after selection
        return redirect('subscription_history')  

    return JsonResponse({"error": "Invalid request"}, status=400)
@login_required
def subscription_history(request):
    """ Show the logged-in user's subscription history in an HTML page """
    subscriptions = Subscription.objects.filter(user=request.user)
    
    return render(request, "subscriptions/subscription_history.html", {"subscriptions": subscriptions})

def subscription_home(request):
    plans = SubscriptionPlan.objects.all()  # Get all plans
    return render(request, "subscriptions/subscription_home.html", {"plans": plans})