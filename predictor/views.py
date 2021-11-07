import datetime
from django.views.generic.list import ListView
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Match, Prediction
from.forms import PredictionForm
# Create your views here.


class RegisterView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "predictor/register.html", {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Account successfully Created, Login....')
            return redirect('login')
        return render(request, "predictor/register.html", {'form': form})


class HomeView(LoginRequiredMixin, View):
    matches = Match.objects.all()

    def get(self, request):
        return render(request, "predictor/home.html",  {"matches": self.matches})

    def post(self, request):
        post_data = request.POST.copy()
        post_data['player'] = request.user
        post_data['match'] = Match.objects.get(pk=request.POST['match'])
        match_exist = Prediction.objects.filter(
            match=request.POST['match']).exists()
        print(match_exist)
        if match_exist:
            prediction = Prediction.objects.filter(match=request.POST['match'])
            if request.POST['prediction'] != "":
                prediction.update(prediction=request.POST['prediction'])
                messages.add_message(request, messages.SUCCESS,
                                 'Your prediction was successfully submitted')
            else: 
                messages.add_message(request, messages.ERROR,
                                     'Please make a prediction.')
            return render(request, "predictor/home.html",  {"matches": self.matches})
        else:
            form = PredictionForm(post_data)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Your prediction was successfully submitted')
                return render(request, "predictor/home.html",  {"matches": self.matches})
            else:
                messages.add_message(request, messages.ERROR,
                                     'Error, please try again.')
                return render(request, "predictor/home.html",  {"matches": self.matches})


class PredictionView(LoginRequiredMixin, View):
    def get(self, request):
        predictions = Prediction.objects.all()
        return render(request, "predictor/prediction.html",  {"predictions": predictions})
