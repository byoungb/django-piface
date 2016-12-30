from pifacedigitalio import PiFaceDigital
from threading import local

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


_active = local()


def get_piface():
    if not hasattr(_active, 'piface'):
        _active.piface = PiFaceDigital()
    return _active.piface


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request):
        self.pfd = get_piface()
        return super(IndexView, self).dispatch(request)

    def get(self, request):
        is_on = self.pfd.relays[0].value = self.pfd.relays[1].value
        return self.render_to_response({
            'is_on': is_on,
        })

    def post(self, request):
        self.pfd.relays[0].value = self.pfd.relays[1].value = (request.POST.get('action') == 'on')
        return HttpResponseRedirect(
            redirect_to=reverse(
                viewname='index',
            ),
        )

