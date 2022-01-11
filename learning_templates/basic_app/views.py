from django.shortcuts import render

# Create your views here.
def index(response):
    context_dict = {'text':'Hello World','number': 100}
    return render(response,'basic_app/index.html',context_dict)

def other(response):
    return render(response,'basic_app/other.html')

def relative(response):
    return render(response,'basic_app/relative_url_templates.html')
