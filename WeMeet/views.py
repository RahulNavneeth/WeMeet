
import json
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import *
from datetime import datetime
from string import *
from .models import *
import random
from .forms import *
from django.contrib.auth.models import Group



def HomePage(request):
    return render(request,'home.html')

def register_school_page(request):
    form=CustomRegFormSchool()


    if request.method == 'POST':
        form=CustomRegFormSchool(request.POST)
        if form.is_valid():
            form.save()
            # print(form.username)
            print('yee valid')
            user                                        = request.POST.get('username')
            schoolState                                 = request.POST.get('schoolState')
            schoolDistrict                              = request.POST.get('schoolDistrict')
            schoolArea                                  = request.POST.get('schoolArea')
            schoolProfilePicture                        = request.FILES.get('schoolProfilePicture')
            yrsOfSchooling                              = request.POST.get('yrsOfSchooling')
            yrStartes                                   = request.POST.get('yrStartes')
            schoolDescription                           = request.POST.get('schoolDescription')
            noOfBatches                                 = request.POST.get('noOfBatches')
            batchStrength                               = request.POST.get('batchStrength')
            batchStd                                    = request.POST.get('batchStd')
            batchDescription                            = request.POST.get('batchDescription')
            print(user)
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

            url = ascii_uppercase+ascii_lowercase+'1234567890'
            urlsrandomschool = random.choices(url,k=30)
            randomurl=""

            for randomurlloop in urlsrandomschool:
                randomurl+=randomurlloop

            profile = User.objects.get(username=user)
            print(profile.id)
            
            schoolSave = school.objects.create(
                                            user=profile,
                                            school_url=randomurl,
                                            school_propic=schoolProfilePicture,
                                            school_address_state=schoolState,
                                            school_address_district=schoolDistrict,
                                            school_address_area=schoolArea,
                                            School_description=schoolDescription,
                                            school_noof_batch=noOfBatches,



            )

            schoolSave.save()
            
            my_group = Group.objects.get(name='school') 
            my_group.user_set.add(profile)
            

            for batches in range(int(noOfBatches)):
                skl=school.objects.get(user=profile.id)
                randomurl=""+str(batches)
                urlsrandomschool = random.choices(url,k=29)
                for randomurlloop in urlsrandomschool:
                    randomurl+=randomurlloop
                batchSave=batch.objects.create(
                                    batch_year=str(2021-batches)+'-06-14',
                                    batch_std=batchStd,
                                    batch_url=randomurl,
                                    batch_strength=batchStrength,
                                    batch_description=batchDescription,
                                    school_reference=skl
                )
                batchSave.save()
                # skl = school.objects.get(school_name=schoolName)
                # btc=batch.objects.create(school_reference = skl.id)
                # btc.save()
            return redirect('/')

        else:
            print('nope')
    else:
        print('not post')
    context={'form':form}

    return render(request,'register_school.html',context)

def register_student_page(request):
    form=CustomRegFormStudent()
    if request.method == 'POST':
        studentSchoolCode                           = request.POST.get('studentSchoolCode')
        studentBatchCode                            = request.POST.get('studentBatchCode')
        if studentSchoolCode is not None or studentBatchCode is not None:
            form=CustomRegFormStudent(request.POST)
            if form.is_valid():
                form.save()
                # print(form.username)
                print('yee valid')
                studentSchoolCode                           = request.POST.get('studentSchoolCode')
                studentBatchCode                            = request.POST.get('studentBatchCode')
                user                                        = request.POST.get('username')
                studentState                                = request.POST.get('studentState')
                studentDistrict                             = request.POST.get('studentDistrict')
                studentArea                                 = request.POST.get('studentArea')
                studentProfilePicture                       = request.FILES.get('studentProfilePicture')
                studentStandard                             = request.POST.get('studentStandard')
                studentDescription                          = request.POST.get('studentDescription')
                url = ascii_uppercase+ascii_lowercase+'1234567890'
                urlsrandomschool = random.choices(url,k=30)
                randomurl=""

                for randomurlloop in urlsrandomschool:
                    randomurl+=randomurlloop

                profile = User.objects.get(username=user)
                from .models import school
                from .models import batch
                schoolId= school.objects.get(school_url=studentSchoolCode)
                batchId= batch.objects.get(school_reference=schoolId,batch_url=studentBatchCode)

                studentSave = student.objects.create(
                                                user=profile,
                                                student_aka_name=user,
                                                student_propic=studentProfilePicture,
                                                student_address_state=studentState,
                                                student_address_district=studentDistrict,
                                                student_address_area=studentArea,
                                                student_std=int(studentStandard),
                                                student_description=studentDescription,
                                                school_reference_id_student=schoolId,
                                                batch_reference_id_student=batchId,



                )

                studentSave.save()
                my_group = Group.objects.get(name='Student') 
                my_group.user_set.add(profile)
                return redirect('/')
    context={'form':form}

    return render(request,'register_student.html',context)


@login_required(login_url='/')
def schoolUser(request):
    return render(request,'school.html')



def loginPage(request):
    if request.method == 'POST':
        if 'btnschool' in request.POST:
            username =       request.POST['emailEmail']
            password =       request.POST['password']
            # print('Email: '+email , 'Password: '+password)
            user = authenticate(request,username=username,password=password)
            print('user: ',user)
            if user is not None:
                if user.groups.filter(name__in=['school']).exists():
                    login(request,user)
                    print('working')
                    return redirect('/school')
                else:
                    messages.info(request,username+' Is Not A School')
                    return redirect('/')

            else:
                messages.info(request,'Intresting...  Please Check Your USERNAME/PASSWORD, Might Have Gone Wrong')
                return redirect('/')




        elif 'btnadmin' in request.POST:
            username =       request.POST['emailEmail']
            password =       request.POST['password']
            # print('Email: '+email , 'Password: '+password)
            user = authenticate(request,username=username,password=password)
            print('user: ',user)
            if user is not None:
                if user.groups.filter(name__in=['admin']).exists():
                    login(request,user)
                    print('working')
                    return redirect('/admin/')
                else:
                    messages.info(request,username+' Is Not A Admin')
                    return redirect('/')

            else:
                messages.info(request,'Intresting...  Please Check Your USERNAME/PASSWORD, Might Have Gone Wrong')
                return redirect('/')


def logoutUser(request):
    logout(request)
    return redirect('/')