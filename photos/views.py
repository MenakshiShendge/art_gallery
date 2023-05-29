from django.shortcuts import render,redirect
from .models import Category,Photo,profile,urequesr
from django.contrib.auth.models import User
from django.contrib import messages
from .models import*
import uuid
from django.conf import settings
from django.core.mail import send_mail
from photoshare.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def gallery(request):
    category=request.GET.get('category')
    # selling_price=Photo.objects.get('selling_price')
    selling_price=request.GET.get('selling_price')
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    if category==None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)

    categories=Category.objects.all()
    context={
        'categories':categories,
        'photos':photos,
        'selling_price':selling_price,
        'user_name':user_name,
    }
    return render(request,'photos/gallery.html',context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def addPhoto(request):
    categories=Category.objects.all()

    if request.method =='POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category']!='none':
            category=Category.objects.get(id= data['category'])
        else:
            category=None

        photo =Photo.objects.create(
            category= category,
            description=data['description'],
            selling_price=data['selling_price'],
            artist_name=data['artist_name'],
            image=image
        ) 
        artist_name=data['artist_name']

        artist_obj= artistname.objects.all()
        if not artistname.objects.filter(username=artist_name).first():
            artist_obj=artistname(username=artist_name)
            artist_obj.save()
               

        return redirect('gallery')

    return render(request,'photos/add.html',{'categories':categories})

# def home(request):
#     return render(request,'photos/home.html')
def home(request):

    return render(request,'photos/home.html')

def verify(request,auth_token):
    try:
        profile_obj=profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, "your account ia already verified")
                return redirect('login')

            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request, "your account has been verified")
            return redirect('login')
        else:
            messages.success(request, "WE HAVE SEND AN EMAIL\nPlease check your mail")

    except Exception as e:
        print(e)

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        print(password)

        try:
            
            if User.objects.filter(username=username).first():
                messages.success(request, "username is exist")
                return redirect('login')
        
            if User.objects.filter(email=email).first():
                messages.success(request, "email is exist")
                return redirect('login')
        
            user_obj=User.objects.create(username=username,email=email)
            user_obj.set_password(password)
            user_obj.first_name = firstname
            user_obj.last_name = lastname
            user_obj.save()
            auth_token=str(uuid.uuid4())
    
            profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
            profile_obj.save()

            send_mail('Your Account Need To Be Verified',f'hello  pass the link to verify your account http://127.0.0.1:8000/verify/{auth_token}',EMAIL_HOST_USER,[email],fail_silently=True)
            messages.success(request, "WE HAVE SEND AN EMAIL\nPlease check your mail")

        except Exception as e:
            print(e)

           
    if request.method=='POST':
        username=request.POST.get('lusername')
        password=request.POST.get('lpassword')
        user_obj=User.objects.filter(username=username).first() 
        if user_obj is None:
            messages.success(request, "user not found")
            return redirect('login')
        
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, "profile is not verified check your mail")
            return redirect('login')
        
        user1=authenticate(username=username,password=password)
        if user1 is None:
            messages.success(request, "wrong password or username")
            
            return redirect('login')
        login(request,user1)
        return redirect ('/')

    return render(request,'photos/login.html')

def section(request):
    
    if request.method =='POST':
       username=request.POST.get('username')
       msg=request.POST.get('msg')
       insta=request.POST.get('insta')
       artist_name=request.POST.get('artistname')
       obj=urequesr.objects.all()
       data=request.POST

       if data['artistname']!='none':
              artist_name=artistname.objects.get(id= data['artistname'])
       else:
            artist_name="Any Artist"

       
    try:
        
           urequesr_obj=urequesr(username=username,msg=msg,insta=insta,artistname=artist_name)
           urequesr_obj.save()
           messages.success(request, "Request submited")
    except Exception as e:
             print(e)
    obj=urequesr.objects.all()
    p=artistname.objects.all()
    cont={'obj':obj,
          'p':p}
    return render(request,'photos/section.html',cont)

def exit(request):
    logout(request)
    return redirect('/')