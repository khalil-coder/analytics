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
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>PostHog Test</title>
        <!-- PostHog JS snippet -->
        <script>
            !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src="https://app.posthog.com/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(u.people=u.people||[],o=["capture","identify","alias","people.set","people.set_once","people.increment"],n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
            posthog.init('phc_7G5P78SjtOI9s2ybkbp7Lvy16LR3b6UUvprEZ12Gu3v', {api_host: 'https://us.i.posthog.com'})
        </script>
    </head>
    <body>
        <h1>Hello, world! This is a simple view using PostHog for analytics.</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
