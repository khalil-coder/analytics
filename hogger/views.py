from django.http import HttpResponse
from django.shortcuts import render
import posthog


# Create your views here.
def hello(request):
    """
    A simple view that returns a greeting.
    """
    posthog.capture(
        distinct_id="user123",
        event="hello_viewed",
        properties={"greeting": "Hello, world!"},
    )
    return HttpResponse("Hello, world! This is a simple view using PostHog for analytics.")
