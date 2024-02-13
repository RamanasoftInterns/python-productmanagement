from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
# rendering the table page


def pdf_table(request):
    products = Product.objects.all()
    return render(request, 'pdf_convert/pdf_convert.html', {'products': products})

# converting the table to pdf


@login_required(login_url='pdf_convert')
def render_pdf_view(request):
    products = Product.objects.all()
    template_path = 'pdf_convert/pdf_convert.html'
    context = {'products': products}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="product_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
