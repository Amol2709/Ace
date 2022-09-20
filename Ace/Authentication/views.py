from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		print('Hey ................................')
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "Registration successful." )
			return redirect("Authentication:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="Authentication/register.html", context={"register_form":form})


# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Your account has been created! You are now able to log in')
# 			return redirect('login')
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="registeration.html", context={"register_form":form,"title":"Join Today"})


# # @login_required
# # def profile(request):
# #     return render(request, 'users/profile.html')