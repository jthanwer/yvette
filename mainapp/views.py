from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import ColocationForm
from .models import Colocation
from django.contrib import messages


def home(request):
    return render(request, 'mainapp/accueil.html')


# View to create a new coloc
@login_required
def create_coloc(request):
    if hasattr(request.user, 'colocation'):
        already_coloc = True
    else:
        form = ColocationForm(request.POST or None)
        if form.is_valid():
            envoi = True
            coloc = form.save(commit=False)
            coloc.owner = request.user
            coloc.mean_age = request.user.age
            coloc.save()
            return redirect('list_colocs')

    return render(request, 'mainapp/create_coloc.html', locals())


class ListColocs(ListView):
    model = Colocation
    context_object_name = 'colocations'
    template_name = 'mainapp/list_colocs.html'

    def get_queryset(self):
        if self.request.GET:
            filter_val = self.request.GET.get('city')
            order = self.request.GET.get('city', 'city')
            new_context = Colocation.objects.filter(owner__city=filter_val)
        else:
            new_context = Colocation.objects.all()
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ListColocs, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('city')
        # context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context


class DetailColoc(DetailView):
    model = Colocation
    context_object_name = 'coloc'
    template_name = 'mainapp/detail_coloc.html'


class UpdateColoc(UpdateView):
    model = Colocation
    template_name = 'mainapp/update_coloc.html'
    form_class = ColocationForm

    def get_object(self, queryset=None):
        obj = super(UpdateColoc, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('detail_coloc', kwargs={'pk': pk})
        return success_url


class DeleteColoc(DeleteView):
    model = Colocation
    context_object_name = 'coloc'
    template_name = 'mainapp/delete_coloc.html'
    success_url = reverse_lazy(home)

    def get_object(self, queryset=None):
        obj = super(DeleteColoc, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


@login_required
def change_coloc(request, op, id_coloc):
    if op == 'goin':
        Colocation.add_tenant(request, id_coloc, request.user)
        Colocation.update_mean_age(id_coloc)
        return HttpResponseRedirect(reverse('detail_coloc', kwargs={'pk': id_coloc}))
    if op == 'leave':
        Colocation.remove_tenant(request, id_coloc, request.user)
        Colocation.update_mean_age(id_coloc)
        return HttpResponseRedirect(reverse('detail_coloc', kwargs={'pk': id_coloc}))

    return render(request, 'mainapp/detail_coloc.html', locals())

