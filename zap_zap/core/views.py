from django.shortcuts import render,HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.generic import View, ListView, CreateView, DetailView
# Create your views here.
def index(request):
    
    return HttpResponse("OK!")

#тут зробити, шоб воно вертало ліст продуктів на хтмл стору
def products(request): 
    pass

#те саме шо в def products тільки за допомогою ListView
class HomeView(ListView):
    pass

#почитаєш про DetailView
class ProductDetail(DetailView):
    pass

class OrderView(View):
    pass

class OrderSummaryView(View):
    pass


    

