from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookingDetails


# settings
from django.conf import settings

# django sending mail
from django.core.mail import send_mail

# add seding mail logic here
@receiver(post_save, sender=BookingDetails)
def send_email_to_customer(sender, instance, created, **kwargs):
    if created:

        mail_subject = "Geomird machine Booking {}".format(instance.machine_booked)
        mail_body_message = "Hello {}, \nYou have booked {}, \nfor date {} to {}, \nbooking reference geo-00{}2026\
        \nOur team will conntact you via \n{} \nfor payment and collection arragements to finalize the booking".format(
            instance.name_of_person_booking,
            instance.machine_booked,
            instance.rental_start_date,
            instance.rental_end_date,
            instance.id,
            instance.phone_of_person_booking,
        )

        try:
            send_mail(
            mail_subject,
            mail_body_message,
            settings.EMAIL_HOST_USER,
            [instance.email_of_person_booking]
        )
        except Exception as e:
            print(e)


@receiver(post_save, sender=BookingDetails)
def send_email_to_admin(sender, instance, created, **kwargs):
    if created:

        mail_subject = "{} booked ".format(instance.machine_booked)
        mail_body_message = "Hello admin, \n{} has booked {}, \nfor date {} to {}, \nbooking reference geo-00{}2026\
        site of work is {}, \n nature of work is {}\
        \nYou can contact them via \n{} \nfor payment and collection arragements to finalize their booking".format(
            instance.name_of_person_booking,
            instance.machine_booked,
            instance.rental_start_date,
            instance.rental_end_date,
            instance.id,
            instance.project_location,
            instance.message,
            instance.phone_of_person_booking,
        )

        try:
            send_mail(
            mail_subject,
            mail_body_message,
            settings.EMAIL_HOST_USER,
            ['gitua85@gmail.com']
        )
        except Exception as e:
            print(e)