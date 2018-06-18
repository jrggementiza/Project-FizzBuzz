from django.http import HttpResponse
from django.shortcuts import render

def fizz_buzz(request):
	return render(request, 'home.html')

def results(request):
	fizz_value, buzz_value, max_value = request.GET['fizz_value'], request.GET['buzz_value'], request.GET['max_value']
	fizz_value, buzz_value, max_value = int(fizz_value), int(buzz_value), int(max_value)
	number_list = {}

	for number in range(1, max_value+1):
		if number % fizz_value == 0 and number % buzz_value == 0:
			number_list[number] = 'fizz buzz!'
		elif number % fizz_value == 0:
			number_list[number] = 'fizz'
		elif number % buzz_value == 0:
			number_list[number] = 'buzz'
		else:
			number_list[number] = number

	return render(request, 'results.html', 
		{'fizz_value':fizz_value, 
		'buzz_value':buzz_value, 
		'max_value':max_value, 
		'number_list':number_list.items})