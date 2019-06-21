from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth import login, authenticate
from .forms import NewScheduleForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Schedule,Profile
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ScheduleSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    schedules = Schedule.objects.all()
    for x in schedules:
        print(x.day)
    profiles = Profile.objects.all()
    return render(request,'index.html',locals())


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Time Mangement Account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
   
@login_required(login_url='/accounts/login/')
def new_schedule(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user.profile
            image.user = current_user

            image.save()
        return redirect('index')

    else:
        form = NewScheduleForm()
    return render(request, 'new_schedule.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    """
    Function that enables one to see their profile
    """
    title = "Profile"

    schedule = Schedule.get_schedule_by_id(id= user_id).order_by('-posted_time')
    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html',{'title':title, "schedule":schedule,"profiles":profiles})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    profile=Profile.objects.get(user=request.user)
    image= Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = ProfileForm()
    return render(request, "edit_profile.html", {"form":form,"image":image}) 

# class ScheduleList(APIView):
#     def get(self, request, format=None):
#         all_merch = Schedule.objects.all()
#         serializers = ScheduleSerializer(all_merch, many=True)
#         return Response(serializers.data)   
#     def post(self, request, format=None):
#         serializers = ScheduleSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProfileList(APIView):
#     def get(self, request, format=None):
#         all_merch = Profile.objects.all()
#         serializers = ProfileSerializer(all_merch, many=True)
#         return Response(serializers.data)
#         permission_classes = (IsAdminOrReadOnly,)

#     def post(self, request, format=None):
#         serializers = ProfileSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#         permission_classes = (IsAdminOrReadOnly,)


# class ScheduleDescription(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get_merch(self, pk):
#         try:
#             return Schedule.objects.get(pk=pk)
#         except Schedule.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         merch = self.get_merch(pk)
#         serializers = ScheduleSerializer(merch)
#         return Response(serializers.data)  

#     def put(self, request, pk, format=None):
#         merch = self.get_merch(pk)
#         serializers = ProfileSerializer(merch, request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
#     def delete(self, request, pk, format=None):
#         merch = self.get_merch(pk)
#         merch.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)       

# class ProfileDescription(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get_merch(self, pk):
#         try:
#             return Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         merch = self.get_merch(pk)
#         serializers = ProfileSerializer(merch)
#         return Response(serializers.data)   

#     def put(self, request, pk, format=None):
#         merch = self.get_merch(pk)
#         serializers = ProfileSerializer(merch, request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

#     def delete(self, request, pk, format=None):
#         merch = self.get_merch(pk)
#         merch.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        
