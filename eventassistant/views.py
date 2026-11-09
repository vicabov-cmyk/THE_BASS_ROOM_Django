from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Event, Guest, Ticket
from .forms import EventForm, GuestForm, TicketForm
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

def dashboard(request):
    events = Event.objects.all().order_by("date")

    total_guests = Guest.objects.count()
    total_tickets = Ticket.objects.count()

    paid_tickets = Ticket.objects.filter(
        is_paid=True
    ).count()

    checked_in = Ticket.objects.filter(
        is_checked_in=True
    ).count()

    total_sales = Ticket.objects.filter(
        is_paid=True
    ).aggregate(total=Sum("price"))["total"] or 0

    context = {
        "events": events,
        "total_guests": total_guests,
        "total_tickets": total_tickets,
        "paid_tickets": paid_tickets,
        "checked_in": checked_in,
        "total_sales": total_sales,
    }

    return render(
        request,
        'eventassistant/dashboard.html',
        context
    )
@staff_member_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)

    else:
        form = EventForm()

    return render(
        request,
        'eventassistant/event_create.html',
        {'form': form}
    )
@staff_member_required
def guest_create(request):

    if request.method == 'POST':

        form = GuestForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('eventassistant_dashboard')

    else:

        form = GuestForm()

    return render(

        request,

        'eventassistant/guest_create.html',

        {'form': form}

            )
@staff_member_required
def ticket_create(request):

    if request.method == "POST":

        form = TicketForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("eventassistant_dashboard")

    else:

        form = TicketForm()

    return render(

        request,

        "eventassistant/ticket_create.html",

        {"form": form}
    )
@staff_member_required
def event_edit(request, pk):

    from django.shortcuts import get_object_or_404, render, redirect

    from .models import Event

    from .forms import EventForm

    event = get_object_or_404(Event, pk=pk)

    form = EventForm(request.POST or None, instance=event)

    if request.method == "POST" and form.is_valid():

        form.save()

        return redirect("eventassistant_dashboard")

    return render(

        request,

        "eventassistant/event_edit.html",

        {"form": form},
    )

@ staff_member_required

def event_delete(request, pk):

    if request.method != "POST":

        return redirect("eventassistant_dashboard")

    event = get_object_or_404(Event, pk=pk)

    if Ticket.objects.filter(event=event).exists():
        return redirect("eventassistant_dashboard")

    event.delete()

    return redirect("eventassistant_dashboard")

