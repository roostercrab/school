from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from . import models
from . import forms

# Create your views here.


class AlumniList(LoginRequiredMixin, ListView):
    template_name = 'alumni/alumni_list.html'
    model = models.Alumni
    queryset = model.objects.all()
    # context_object_name = 'all_alumni'
    paginate_by = '25'


class AlumniRedirectMostrar(LoginRequiredMixin, RedirectView):
    def get(self, request, *args, **kwargs):
        model = models.Alumni
        alumni_id = self.kwargs.get('pk', None)
        alumni = model.objects.get(pk=alumni_id)
        self.url = '/mostrar/%s' % alumni.id
        return super(AlumniRedirectMostrar, self).get(request, *args, **kwargs)


class AlumniRetrieve(LoginRequiredMixin, DetailView):
    template_name = 'alumni/alumni_retrieve.html'
    model = models.Alumni
    # context_object_name = 'alumno'


class AlumniRetrievePadres(LoginRequiredMixin, DetailView):
    template_name = 'alumni/alumni_retrieve_parents.html'
    model = models.Alumni
    # context_object_name = 'alumno'


class AlumniRetrieveAutorizado(LoginRequiredMixin, DetailView):
    template_name = 'alumni/alumni_retrieve_authorized.html'
    model = models.Alumni
    # context_object_name = 'alumno'


class AlumniRetrieveFinanzas(LoginRequiredMixin, DetailView):
    template_name = 'alumni/alumni_retrieve_finance.html'
    model = models.Alumni
    # context_object_name = 'alumno'


class AlumniRetrieveDocumentos(LoginRequiredMixin, DetailView):
    template_name = 'alumni/alumni_retrieve_docs.html'
    model = models.Alumni
    # context_object_name = 'alumno'


class AlumniRegister(LoginRequiredMixin, CreateView):
    template_name = 'alumni/alumni_register.html'
    form_class = forms.AlumniFormRegister
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-padres', kwargs={'pk': self.object.id})


class AlumniRegisterPadres(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_register_parents.html'
    form_class = forms.AlumniFormRegisterParents
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-autorizado', kwargs={'pk': self.object.id})


class AlumniRegisterAutorizado(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_register_authorized.html'
    form_class = forms.AlumniFormRegisterAuthorized
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-finanzas', kwargs={'pk': self.object.id})


class AlumniRegisterFinanzas(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_register_finance.html'
    form_class = forms.AlumniFormRegisterFinance
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-inscripcion-documentos', kwargs={'pk': self.object.id})


class AlumniRegisterDocumentos(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_register_docs.html'
    form_class = forms.AlumniFormRegisterDocs
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-mostrar', kwargs={'pk': self.object.id})


class AlumniUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_update.html'
    form_class = forms.AlumniFormRegister
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar', kwargs={'pk': self.object.id})


class AlumniUpdatePadres(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_update_parents.html'
    form_class = forms.AlumniFormRegisterParents
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-padres', kwargs={'pk': self.object.id})


class AlumniUpdateAutorizado(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_update_authorized.html'
    form_class = forms.AlumniFormRegisterAuthorized
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-autorizado', kwargs={'pk': self.object.id})


class AlumniUpdateFinanzas(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_update_finance.html'
    form_class = forms.AlumniFormRegisterFinance
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-finanzas', kwargs={'pk': self.object.id})


class AlumniUpdateDocumentos(LoginRequiredMixin, UpdateView):
    template_name = 'alumni/alumni_update_docs.html'
    form_class = forms.AlumniFormRegisterDocs
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-actualizar-documentos', kwargs={'pk': self.object.id})


class AlumniDelete(LoginRequiredMixin, DeleteView):
    template_name = 'alumni/alumni_delete.html'
    model = models.Alumni
    # context_object_name = 'alumno'

    def get_success_url(self, **kwargs):
        return reverse('alumni-lista')
