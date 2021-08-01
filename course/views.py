from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DetailView

from course.models import Course, Video, Contact, MyProfile
# Create your views here.
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from lms import settings
from django.core.mail import EmailMessage
from django.contrib import messages
def home(request):
    return render(request, 'course/mainn.html')


def courses(request):
    courses = Course.objects.all();
    print(courses)
    return render(request, 'course/courses.html', context={'courses': courses})


def coursePage(request, slug):
    print(slug)
    course = Course.objects.get(slug=slug)
    print(course)
    serial_number = request.GET.get('lecture')

    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1

    video = Video.objects.get(serial_number=serial_number, Course=course)

    context = {
        "course": course,
        "video": video,
        "videos": videos,
        "serialno": serial_number,
    }
    return render(request, template_name="course/CoursePage.html", context=context)

login_required(login_url='/accounts/login')
def mailsnd(request):
    if request.method == "POST":
        message = request.POST['message']
        uname = request.POST['name']
        phone = request.POST['phone']
        to_email = request.POST['email']
        print(message + " " +uname +" " +phone +" " +to_email)
        if message and to_email:
            cont=Contact(name=uname , email=to_email , phone=phone ,message=message)
            cont.save()
            try:
                ctx = {

                    'user': uname,
                    'phone': phone,
                    'emaill': to_email,
                    'message': message,
                }
                message = get_template('course/mail-template.html').render(ctx)
                email = EmailMessage('client', message,to=['M.collections78600@gmail.com'])
                email.content_subtype = "html"  # Main content is now text/html
                email.send()
                print("mail sent successfully")
            except:
                messages.error(request , 'mail not sent')
                return redirect('/')
            messages.success(request ,'Mail sent successfully')
            return redirect('/')
        else:
            messages.error(request , 'please enter your email and message')
            return redirect('/')


def about(request):
    return render(request, 'course/about.html')


@method_decorator(login_required, name="dispatch")
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["name", "age", 'city', "address", 'zipcode', "status", "gender", "phone_no", "description", "pic"]


@method_decorator(login_required, name="dispatch")
class MyProfileDetailView(DetailView):
    model = MyProfile