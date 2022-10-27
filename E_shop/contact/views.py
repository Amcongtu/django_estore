from django.shortcuts import render
from contact.forms import FormContact
from contact.models import  *
from django.core.mail import send_mail, EmailMultiAlternatives
from E_shop.settings import EMAIL_HOST_USER

# Create your views here.
def contact(request):
    
    locations = Location.objects.filter(status_Location=1)
    


    chuoi_kq = ''
    form_contact = FormContact()
    if request.POST.get('send_message'):
        form_contact = FormContact(request.POST, Contact)
        if form_contact.is_valid():
            request.POST._mutable = True
            post = form_contact.save(commit=False)
            post.name = form_contact.cleaned_data['name']
            post.email = form_contact.cleaned_data['email']
            post.subject = form_contact.cleaned_data['subject']
            post.message = form_contact.cleaned_data['message']
            post.save()

            # Gửi mail
            send_mail(post.subject, post.message, EMAIL_HOST_USER, [post.email])

            noi_dung = '<p>Xin chào bạn <b><i>' + post.name + '</i></b></p>'
            noi_dung += '<p>Chúng tôi đã nhận được thông tin phản hồi của bạn từ website TTC Shopper với nội dung như sau:</p>'
            noi_dung += '<p>' + post.message + '</p>'
            noi_dung += '<p>Chúng tôi sẽ phản hồi thông tin đến bạn trong thời gian sớm nhất.</p>'

            msg = EmailMultiAlternatives(post.subject, noi_dung, EMAIL_HOST_USER, [post.email])
            msg.attach_alternative(noi_dung, 'text/html')
            msg.send()

            chuoi_kq = '''
            <div class="alert alert-success" role="alert">
                Gửi thông tin thành công.
            </div>
            '''
        
    return render(request,"contact/contact.html",{
        "nav":"Contact",
        'form_contact': form_contact,
        'chuoi_kq': chuoi_kq,
        'locations':locations,
    })