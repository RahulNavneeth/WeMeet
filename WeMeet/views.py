
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
    return render(request,'register_student.html')


@login_required(login_url='/')
def AdminUser(request):
    return render(request,'adminUserTest.html')



#==========register school==========#

def register_school(request):
    form=CustomRegFormSchool()

    if request.method == 'POST':






        # schoolState                                 = request.POST.get('schoolState')
        # schoolDistrict                              = request.POST.get('schoolDistrict')
        # schoolArea                                  = request.POST.get('schoolArea')
        # schoolProfilePicture                        = request.FILES.get('schoolProfilePicture')
        # yrsOfSchooling                              = request.POST.get('yrsOfSchooling')
        # yrStartes                                   = request.POST.get('yrStartes')
        # schoolDescription                           = request.POST.get('schoolDescription')
        # noOfBatches                                 = request.POST.get('noOfBatches')
        # batchStrength                               = request.POST.get('batchStrength')
        # batchStd                                    = request.POST.get('batchStd')
        # batchDescription                            = request.POST.get('batchDescription')

        # now = datetime.now()
        # formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        # url = ascii_uppercase+ascii_lowercase+'1234567890'
        # urlsrandomschool = random.choices(url,k=30)
        # randomurl=""

        # for randomurlloop in urlsrandomschool:
        #     randomurl+=randomurlloop


        # schoolSave = school.objects.create(
        #                                   school_name=schoolName,
        #                                   school_email=schoolEmail,
        #                                   school_joined_WeMeet=formatted_date,
        #                                   school_password=schoolPassword,
        #                                   school_url=randomurl,
        #                                   school_propic=schoolProfilePicture,
        #                                   school_address_state=schoolState,
        #                                   school_address_district=schoolDistrict,
        #                                   school_address_area=schoolArea,
        #                                   School_description=schoolDescription,
        #                                   school_noof_batch=noOfBatches,



        # )

        # schoolSave.save()
        # skl=school.objects.get(school_name=schoolName)
        # # print(skl.id)
        # for batches in range(int(noOfBatches)):
        #     randomurl=""
        #     urlsrandomschool = random.choices(url,k=30)
        #     for randomurlloop in urlsrandomschool:
        #         randomurl+=randomurlloop
        #     batchSave=batch.objects.create(
        #                         batch_year='2021-06-27',
        #                         batch_std=batchStd,
        #                         batch_url=randomurl,
        #                         batch_strength=batchStrength,
        #                         batch_description=batchDescription,
        #                         school_reference=skl
        #     )
        #     batchSave.save()
        #     # skl = school.objects.get(school_name=schoolName)
        #     # btc=batch.objects.create(school_reference = skl.id)
        #     # btc.save()
        return redirect('/')


def loginPage(request):
    if request.method == 'POST':
        username =       request.POST['emailEmail']
        password =       request.POST['password']
        # print('Email: '+email , 'Password: '+password)
        user = authenticate(request,username=username,password=password)
        print('user: ',user)
        if user is not None:
            login(request,user)
            print('working')
            return redirect('/AdminUser')
        else:
            return redirect('/')


def logoutUser(request):
    logout(request)
    return redirect('/')