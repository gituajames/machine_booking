from django.shortcuts import render, redirect
from .models import BookingDetails

# settings
from django.conf import settings

# django sending mail
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html',)


def book_machine(request):
    if request.method == 'POST':
        equipment = request.POST.get('equipment')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        message = request.POST.get('message')

        booking = BookingDetails.objects.create(
            machine_booked = equipment,

            name_of_person_booking = name,
            email_of_person_booking = email,
            phone_of_person_booking = phone,

            project_location = location,
            rental_start_date = start_date,
            rental_end_date = end_date,

            message = message,
        )

        mail_subject = "Geomird machine Booking {}".format(booking.machine_booked)
        mail_body_message = "Hello {}, \nYou have booked {}, \nfor date {} to {}, \nbooking reference geo-00{}2026\
        \nOur team will conntact you via \n{} \nfor payment and collection arragements to finalize the booking".format(
            booking.name_of_person_booking,
            booking.machine_booked,
            booking.rental_start_date,
            booking.rental_end_date,
            booking.id,
            booking.phone_of_person_booking,
        )

        try:
            send_mail(
            mail_subject,
            mail_body_message,
            settings.EMAIL_HOST_USER,
            [booking.email_of_person_booking]
        )
        except Exception as e:
            print(e)

        context = {
            'booking' : booking,
        }

        # return render(request, 'thankyou.html', context=context)
        return redirect('success_booking', pk=booking.id)

    return redirect('booking_machine')

def success_booking(request, pk):
    booking = BookingDetails.objects.get(id=pk)

    return render(request, 'thankyou.html', {'booking':booking})


# Create your views here.
