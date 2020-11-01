from django.shortcuts import render

from .task import payment_completed


def payment_process(request):
    """PAYMENT SYSTEM"""
    # request
    # payment
    # payment completed
    payment_completed.delay(order.id)
