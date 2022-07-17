from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from clinic.reservationsapp import models as reservation_models


@login_required
def home(request):
    today = date.today()
    last_week_date = today - timedelta(days=6)
    # graph
    #   total
    last_seven_days_reservations = reservation_models.Reservation.objects.filter(
        date__lte=today, date__gte=last_week_date
    )
    last_seven_days_reservations_count = last_seven_days_reservations.count()
    last_seven_days_reservations_revenue = last_seven_days_reservations.aggregate(
        Sum("price")
    )["price__sum"]
    #  last 7 days
    last_7_days_dates = []
    last_7_days_values = []
    for i in range(7):
        day_date = today - timedelta(days=i)
        day = reservation_models.Reservation.objects.filter(date=day_date)
        day_revenue = day.aggregate(Sum("price"))["price__sum"]
        last_7_days_dates.append(str(day_date))
        if day_revenue:
            last_7_days_values.append(day_revenue)
        else:
            last_7_days_values.append(0)
    # cards
    #   daily
    today_reservations = reservation_models.Reservation.objects.filter(date=today)
    today_reservations_count = today_reservations.count()
    today_reservations_revenue = today_reservations.aggregate(Sum("price"))[
        "price__sum"
    ]
    #   weekly
    first_day_of_week = date.today() - timedelta(
        days=((datetime.now().isoweekday() + 1) % 7)
    )
    this_week_reservations = reservation_models.Reservation.objects.filter(
        date__gte=first_day_of_week
    )
    this_week_reservations_count = this_week_reservations.count()
    this_week_reservations_revenue = this_week_reservations.aggregate(Sum("price"))[
        "price__sum"
    ]
    #   total
    all_reservations = reservation_models.Reservation.objects.all()
    all_reservations_count = all_reservations.count()
    if all_reservations_count > 0:
        first_date = all_reservations.first().date
    else:
        first_date = None

    all_reservations_revenue = all_reservations.aggregate(Sum("price"))["price__sum"]
    context = {
        "title": "information",
        "today": today,
        "today_reservations_count": today_reservations_count,
        "today_reservations_revenue": today_reservations_revenue,
        "first_day_of_week": first_day_of_week,
        "this_week_reservations_count": this_week_reservations_count,
        "this_week_reservations_revenue": this_week_reservations_revenue,
        "all_reservations_count": all_reservations_count,
        "all_reservations_revenue": all_reservations_revenue,
        "first_date": first_date,
        "last_seven_days_reservations_count": last_seven_days_reservations_count,
        "last_seven_days_reservations_revenue": last_seven_days_reservations_revenue,
        "last_7_days_dates": last_7_days_dates,
        "last_7_days_values": last_7_days_values,
    }
    return render(request, "new/index.html", context=context)
