from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from piface import get_piface


class IndexView(TemplateView):
    template_name = 'index.html'
    _pfd = None

    def dispatch(self, request, *args, **kwargs):
        self._pfd = get_piface()
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        is_on = self._pfd.relays[0].value = self._pfd.relays[1].value
        return self.render_to_response({
            'is_on': is_on,
        })

    def post(self, request, *args, **kwargs):
        self._pfd.relays[0].value = self._pfd.relays[1].value = (request.POST.get('action') == 'on')
        return HttpResponseRedirect(
            redirect_to=reverse(
                viewname='index',
            ),
        )

