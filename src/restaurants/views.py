from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView,ListView, DetailView,CreateView, UpdateView
from django.db.models import Q

from .models import RestaurantsLocation
from .forms import RestaurantCreateForm, RestaurantsLocationCreateForm
# Create your views here.
# @login_required()
# def restaurant_createview(request):
#     # if request.method == 'POST':
#         # print('Get Data POST')
#         # print(request.POST)
#         # title =request.POST.get('title')
#         # location =request.POST.get('location')
#         # category =request.POST.get('category')
#         # form = RestaurantCreateForm(request.POST)
#     form = RestaurantsLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         if request.user.is_authenticated():
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#         # obj = RestaurantsLocation.objects.create(
#         #     name = form.cleaned_data.get('name'),
#         #     location = form.cleaned_data.get('location'),
#         #     category = form.cleaned_data.get('category'),
#         #
#         # )
#             return HttpResponseRedirect('/restaurants/')
#         else:
#             return HttpResponseRedirect('/login/')
#     if form.errors:
#         errors = form.errors
#     template_name = 'restaurants/form.html'
#     context = {"form":form}
#     return render(request, template_name, context, errors)




# def restaurant_listview(request,):
#     template_name = 'restaurants/restaurants_list.html'
#     queryset = RestaurantsLocation.objects.all()
#     context = {
#          "object_list":queryset,
#     }
#     return render(request,template_name, context)
#
# def restaurant_detailview(request,slug):
#     template_name = 'restaurants/restaurantslocation_detail.html'
#     obj = RestaurantsLocation.objects.get(slug=slug)
#     context = {
#          "object":obj,
#     }
#     return render(request,template_name, context)


class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantsLocation.objects.filter(owner=self.request.user)
        # slug = self.kwargs.get("slug")
        # if slug:
        #     queryset = RestaurantsLocation.objects.filter(
        #         Q(category__iexact=slug),
        #         Q(category__icontains=slug)
        #     )
        # else:
        #     queryset = RestaurantsLocation.objects.all()
        # return queryset

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantsLocation.objects.filter(owner=self.request.user)
    # def get_context_data(self,*args ,**kwargs):
    #     context = super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
    #     return context

    # def get_object(self,*args,**kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantsLocation, id=rest_id) # pk = rest_id
    #     return obj

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantsLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    # success_url = '/restaurants/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)



    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context ['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantsLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html'

    # success_url = '/restaurants/'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        # name = self.get_object().name
        context['title'] = 'Update Restaurant'
        return context

    def get_queryset(self):
        return RestaurantsLocation.objects.filter(owner=self.request.user)
#
# class HomeView(TemplateView):
#     template_name = "home.html"
#     def get_context_data(self, *args,**kwargs):
#         context= super(HomeView, self).get_context_data(*args,**kwargs)
#         num = random.randint(0, 10000)
#         some_list = [num, random.randint(0, 10000), random.randint(0, 10000)]
#         context = {
#             "bool_item": False,
#             "num": num,
#             "some_list": some_list
#         }
#         return context
#
# class AboutView(TemplateView):
#     template_name = "about.html"
#
#
# class ContactView(TemplateView):
#     template_name = "contact.html"

