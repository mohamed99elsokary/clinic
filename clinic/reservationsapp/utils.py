import calendar
import time
from datetime import datetime

from clinic.clinicapp import models as work_times_models

from . import models


def time_to_tiemstamp(date_time):
    return calendar.timegm(
        time.strptime(f"1970-01-01 {date_time}", "%Y-%m-%d %H:%M:%S")
    )


def get_available_time_normal_service(date):
    # get day name
    day = datetime.strptime(f"{date} 0:0:00", "%Y-%m-%d %H:%M:%S")
    day_name = day.strftime("%A").lower()
    # get work times in that day
    try:
        working_time = work_times_models.WorkTimes.objects.get(day=day_name)
        working_start_time = time_to_tiemstamp(working_time.start_time)
        working_end_time = time_to_tiemstamp(working_time.end_time)
        # get all reservations for the same day
        reserved_times = models.Reservation.objects.filter(date=date).order_by(
            "start_time"
        )
        reserved_times_count = reserved_times.count()
        reservations = []
        if reserved_times_count > 0:
            for reservation in reserved_times:
                reservations.append(
                    {
                        "start_time": time_to_tiemstamp(reservation.start_time),
                        "end_time": time_to_tiemstamp(reservation.end_time),
                    }
                )
            # get the avaliable times
            index = 0
            available_times = []

            reservations_length = len(reservations)

            for reservation in reservations:
                index += 1
                start_time = reservation["start_time"]
                end_time = reservation["end_time"]
                if start_time >= working_start_time:

                    available_times.append(
                        {
                            "start_time": working_start_time,
                            "end_time": start_time,
                        }
                    )
                    working_start_time = end_time
                    if index == reservations_length:
                        available_times.append(
                            {
                                "start_time": working_start_time,
                                "end_time": working_end_time,
                            }
                        )

        else:
            available_times = [
                {
                    "start_time": working_start_time,
                    "end_time": working_end_time,
                }
            ]

    except:
        available_times = None
    return available_times


def get_available_time_online_service(date):
    # get day name
    day = datetime.strptime(f"{date} 0:0:00", "%Y-%m-%d %H:%M:%S")
    day_name = day.strftime("%A").lower()
    # get work times in that day
    try:
        working_time = work_times_models.OnlineWorkTimes.objects.get(day=day_name)
        working_start_time = time_to_tiemstamp(working_time.start_time)
        working_end_time = time_to_tiemstamp(working_time.end_time)
        # get all reservations for the same day
        reserved_times = models.Reservation.objects.filter(date=date).order_by(
            "start_time"
        )
        reserved_times_count = reserved_times.count()
        reservations = []
        if reserved_times_count > 0:
            for reservation in reserved_times:
                reservations.append(
                    {
                        "start_time": time_to_tiemstamp(reservation.start_time),
                        "end_time": time_to_tiemstamp(reservation.end_time),
                    }
                )
            # get the avaliable times
            index = 0
            available_times = []

            reservations_length = len(reservations)

            for reservation in reservations:
                index += 1
                start_time = reservation["start_time"]
                end_time = reservation["end_time"]
                if start_time >= working_start_time:

                    available_times.append(
                        {
                            "start_time": working_start_time,
                            "end_time": start_time,
                        }
                    )
                    working_start_time = end_time
                    if index == reservations_length:
                        available_times.append(
                            {
                                "start_time": working_start_time,
                                "end_time": working_end_time,
                            }
                        )

        else:
            available_times = [
                {
                    "start_time": working_start_time,
                    "end_time": working_end_time,
                }
            ]

    except:
        available_times = None
    return available_times
