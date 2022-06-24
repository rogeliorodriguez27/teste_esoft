from django.shortcuts import render,get_object_or_404
from .models import Products
from .forms import ProductsForm
from django.http import JsonResponse
from django.template.loader import render_to_string

def products_list(request):
	products = Products.objects.all()
	context = {
	'products': products
	}
	return render(request, 'product_list.html',context)

def save_all(request,form,template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			products = Products.objects.all()
			data['product_list'] = render_to_string('product_list_2.html',{'products':products})
		else:
			data['form_is_valid'] = False
	context = {
	'form':form
	}
	data['html_form'] = render_to_string(template_name,context,request=request)
	return JsonResponse(data)

def products_create(request):
	if request.method == 'POST':
		form = ProductsForm(request.POST)
	else:
		form = ProductsForm()
	return save_all(request,form,'product_create.html')

def product_update(request,id):
	product = get_object_or_404(Products,id=id)
	if request.method == 'POST':
		form = ProductsForm(request.POST,instance=product)
	else:
		form = ProductsForm(instance=product)
	return save_all(request,form,'product_update.html')

def product_delete(request,id):
	data = dict()
	product = get_object_or_404(Products,id=id)
	if request.method == "POST":
		product.delete()
		data['form_is_valid'] = True
		products = Products.objects.all()
		data['product_list'] = render_to_string('product_list_2.html',{'products':products})
	else:
		context = {'product':product}
		data['html_form'] = render_to_string('product_delete.html',context,request=request)

	return JsonResponse(data)





