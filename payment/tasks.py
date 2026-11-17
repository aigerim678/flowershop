from io import BytesIO
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.staticfiles import finders
from orders.models import Order


@shared_task
def payment_completed(order_id):
    import weasyprint  # lazy: needs system Pango libs, only used for PDFs
    order = Order.objects.get(id=order_id)
    subject = f'Guldershop - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         settings.DEFAULT_FROM_EMAIL,
                         [order.email])
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(finders.find('css/pdf.css'))]
    weasyprint.HTML(string=html).write_pdf(out,
                                           stylesheets=stylesheets)
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    email.send()