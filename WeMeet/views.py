
import cloudinary.uploader
import json
from django.core import mail
from django.db.models.aggregates import Count
from django.shortcuts import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import *
from datetime import datetime
from string import *
from django.template.loader import render_to_string
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from .models import *
from django.core.mail import EmailMultiAlternatives
import urllib
import random
from django.conf import settings
from django.core.mail import send_mail
from .forms import *
from django.utils.html import strip_tags
from django.contrib.auth.models import Group
import requests
from django.core.files.base import ContentFile


def HomePage(request):
    if request.user.is_authenticated:
        url = ('https://api.adviceslip.com/advice')
        response = requests.get(url)
        data = {
            'auth': True,
            'response': {
                'slip': {
                    'id': response.json()['slip']['id'],
                    'advice': response.json()['slip']['advice'],
                }
            }

        }
        # print(response.json()['slip']['advice'])
        return render(request, 'home.html', {'data': data})
    else:
        data = {
            'auth': False,
            'response': 'NoResponse'

        }
        url = 'https://api.kwelo.com/v1/media/identicon/hlo'
        # from PIL import Image
        # import requests
        # from io import BytesIO

        # response = requests.get(url)
        # img = Image.open(BytesIO(response.content))
        # print(img)
        # img.show()
        # img=img.read()
        # print(img)
        # urllib.request.urlretrieve(url,'hi')
        return render(request, 'home.html', {'data': data})


def register_school_page(request):
    form = CustomRegFormSchool()

    if request.method == 'POST':
        form = CustomRegFormSchool(request.POST)
        user = request.POST.get('username')
        schoolState = request.POST.get('schoolState')
        schoolDistrict = request.POST.get('schoolDistrict')
        schoolArea = request.POST.get('schoolArea')
        schoolProfilePicture = request.FILES.get('schoolProfilePicture')
        yrsOfSchooling = request.POST.get('yrsOfSchooling')
        yrStartes = request.POST.get('yrStartes')
        schoolDescription = request.POST.get('schoolDescription')
        noOfBatches = request.POST.get('noOfBatches')
        batchStrength = request.POST.get('batchStrength')
        batchStd = request.POST.get('batchStd')
        batchDescription = request.POST.get('batchDescription')

        if schoolState or schoolDistrict or schoolArea or yrsOfSchooling or yrStartes or noOfBatches or schoolDistrict or batchStrength or batchStd or batchDescription:

            if form.is_valid():
                form.save()
                # print(form.username)
                print('yee valid')

                print(user)
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

                url = ascii_uppercase+ascii_lowercase+'1234567890'
                urlsrandomschool = random.choices(url, k=30)
                randomurl = ""

                for randomurlloop in urlsrandomschool:
                    randomurl += randomurlloop

                profile = User.objects.get(username=user)
                print(profile.id)

                if schoolProfilePicture is None:
                    from PIL import Image
                    import requests
                    from io import BytesIO
                    url = 'https://api.kwelo.com/v1/media/identicon/'+user

                    response = requests.get(url)
                    img = Image.open(BytesIO(response.content))
                    print(img)
                    img.show()
                    # img=img.read()
                    # img=urllib.request.urlretrieve(url,user+'.png')
                    print(ContentFile(response.content))
                    schoolSave = school.objects.create(
                        user=profile,
                        school_url=randomurl,
                        school_propic=response,
                        school_address_state=schoolState,
                        school_address_district=schoolDistrict,
                        school_address_area=schoolArea,
                        School_description=schoolDescription,
                        school_noof_batch=noOfBatches,



                    )
                    schoolSave.save()
                    # nullprofile = school.objects.get(user=profile)
                    # nullprofile.school_propic.save(user, ContentFile(response.content), save=False)

                else:
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

                my_group = Group.objects.get(name='School')
                my_group.user_set.add(profile)

                for batches in range(int(noOfBatches)):
                    skl = school.objects.get(user=profile.id)
                    randomurl = ""

                    urlsrandomschool = random.choices(url, k=30)
                    for randomurlloop in urlsrandomschool:
                        randomurl += randomurlloop

                    batchSave = batch.objects.create(
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

                mail = request.POST.get('email')
                u = User.objects.get(email=mail)
                skl = school.objects.get(user=u)
                # recipient_list = [mail]
                # data = {
                #     'username': user,
                #     'profilePicture': skl.school_propic.url,
                # }

                # msg_plain ='Test'
                # msg_html = render_to_string('Mail/RegisterSucess.html',{'data':data})

                # email_from = settings.EMAIL_HOST_USER
                # send_mail(
                #     user+', Register Succesfull --WeMeet',
                #     msg_plain,
                #     email_from,
                #     recipient_list,
                #     html_message=msg_html,
                # )
                messages.info(
                    request, "Hey "+user+", Appreciate Your Registration, Now Please LOGIN To Continue")

                return redirect('/')

            else:
                print(form.errors.items)

                messages.info(request, str(form.errors))
                return redirect('/register/school')
        else:
            messages.info(request, 'Make Sure You Fill Everything Out! :)')
            return redirect('/register/school')

    else:
        if request.user.is_authenticated:
            messages.info(request, 'Please Logout to Register')

            return redirect('/')

        else:

            context = {'form': form}

            return render(request, 'register_school.html', context)


def register_student_page(request):
    form = CustomRegFormStudent()
    if request.method == 'POST':
        usernameusername = request.POST.get('username')
        emailemail = request.POST.get('email')
        studentSchoolCode = request.POST.get('studentSchoolCode')
        studentBatchCode = request.POST.get('studentBatchCode')
        studentSchoolCode = request.POST.get('studentSchoolCode')
        studentBatchCode = request.POST.get('studentBatchCode')
        user = request.POST.get('username')
        studentState = request.POST.get('studentState')
        studentDistrict = request.POST.get('studentDistrict')
        studentArea = request.POST.get('studentArea')
        studentProfilePicture = request.FILES.get('studentProfilePicture')
        studentStandard = request.POST.get('studentStandard')
        studentDescription = request.POST.get('studentDescription')

        if studentState or studentDistrict or studentArea or studentProfilePicture or studentStandard or studentDescription:
            if studentSchoolCode != '' and studentBatchCode != '':
                form = CustomRegFormStudent(request.POST)
                from .models import school
                from .models import batch
                if school.objects.filter(school_url=studentSchoolCode).exists():
                    schoolId = school.objects.get(school_url=studentSchoolCode)
                    if batch.objects.filter(school_reference=schoolId, batch_url=studentBatchCode).exists():
                        if form.is_valid():
                            form.save()
                            # print(form.username)
                            print('yee valid')

                            url = ascii_uppercase+ascii_lowercase+'1234567890'
                            urlsrandomschool = random.choices(url, k=30)
                            randomurl = ""

                            for randomurlloop in urlsrandomschool:
                                randomurl += randomurlloop

                            profile = User.objects.get(username=user)

                            from .models import school
                            from .models import batch

                            schoolId = school.objects.get(
                                school_url=studentSchoolCode)
                            batchId = batch.objects.get(
                                school_reference=schoolId, batch_url=studentBatchCode)

                            studentSave = student.objects.create(
                                user=profile,
                                student_aka_name=user,
                                student_url=randomurl,
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
                            mail = request.POST.get('email')
                            u = User.objects.get(email=mail)
                            skl = student.objects.get(user=u)
                            # recipient_list = [mail]
                            # data = {
                            #     'username': user,
                            #     'profilePicture': skl.student_propic.url,
                            # }

                            # msg_plain ='Registration Successfull'
                            # msg_html = render_to_string('Mail/RegisterSucess.html',{'data':data})

                            # email_from = settings.EMAIL_HOST_USER
                            # send_mail(
                            #     user+', Registered Succesfull --WeMeet',
                            #     msg_plain,
                            #     email_from,
                            #     recipient_list,
                            #     html_message=msg_html,
                            # )
                            messages.info(
                                request, "Hey "+user+", Appreciate Your Registration, Now Please LOGIN To Continue")

                            return redirect('/')

                        else:
                            messages.info(request, str(form.errors))
                            return redirect('/register/student')
                    else:
                        messages.info(
                            request, "Please Check Your 'BATCH CODE' / BATCH Doesn't Exist :(")
                        return redirect('/register/student')
                else:
                    messages.info(
                        request, "Please Check Your 'SCHOOL CODE' / SCHOOL Doesn't Exist :(")
                    return redirect('/register/student')
            else:
                messages.info(request, 'Please Fill The "CODE"')
                return redirect('/register/student')
        else:
            messages.info(request, 'Make Sure You Fill Everything Out! :)')
            return redirect('/register/student')
    else:
        if request.user.is_authenticated:
            messages.info(request, 'Please Logout to Register')

            return redirect('/')

        else:
            context = {'form': form}

            return render(request, 'register_student.html', context)


@login_required(login_url='/')
def schoolUser(request, schoolname):
    if User.objects.filter(username=schoolname, groups__name='School').exists():
        if request.user.username == schoolname:
            batch = []
            for i in reversed(request.user.user_school.school_batch.all().order_by('batch_year')):
                batchin = {
                    'school': i.school_reference,
                    'batch_year': i.batch_year,
                    'batch_url': i.batch_url,
                    'batch_strength': i.batch_strength,
                    'batch_description': i.batch_description,

                }
                batch.append(batchin)
            return render(request, 'school.html', {'batch': batch})
        else:
            return HttpResponse("Your are Not authorized to this school")
    else:
        return render(request, '404.html')


@login_required(login_url='/')
def studentUser(request, studentname):
    if User.objects.filter(username=studentname, groups__name='Student').exists():
        if request.user.username == studentname:
            from .models import post
            # posts = post.objects.filter(user=request.user).exsist()
            # print(posts)
            if post.objects.filter(user=request.user).exists():
                posts = post.objects.filter(user=request.user).all()

                postAll = []
                postDict = {
                    'bool': True,
                    'post': postAll
                }
                for i in posts:
                    x = dict(id=i.id,
                             user=i.user.username,
                             media=i.media.url,
                             description=i.description,
                             date=str(i.date.hour)+':' +
                             str(i.date.minute)+' '+str(i.date.date()),
                             like=dict(count=i.likes.count()))
                    postAll.append(x)
                return render(request, 'student.html', {'post': postDict})
            else:
                postDict = {
                    'bool': False,
                    'post': 'Add One'
                }
                return render(request, 'student.html', {'post': postDict})

        else:
            return HttpResponse("Your are Not authorized to this student")
    else:
        return render(request, '404.html')


def loginPage(request):
    if request.method == 'POST':
        if 'btnschool' in request.POST:
            username = request.POST['emailEmail']
            password = request.POST['password']
            # print('Email: '+email , 'Password: '+password)
            user = authenticate(request, username=username, password=password)
            print('user: ', user)
            if user is not None:
                if user.groups.filter(name__in=['School']).exists():
                    login(request, user)
                    print('working')
                    return redirect('u/school/'+request.user.username)
                else:
                    messages.info(request, username+' Is Not A School')
                    return redirect('/')

            else:
                messages.info(
                    request, 'Intresting...  Please Check Your USERNAME/PASSWORD, Might Have Gone Wrong')
                return redirect('/')

        elif 'btnadmin' in request.POST:
            username = request.POST['emailEmail']
            password = request.POST['password']
            # print('Email: '+email , 'Password: '+password)
            user = authenticate(request, username=username, password=password)
            print('user: ', user)
            if user is not None:
                if user.groups.filter(name__in=['Admin']).exists():
                    login(request, user)
                    print('working')
                    return redirect('/admin/')
                else:
                    messages.info(request, username+' Is Not A Admin')
                    return redirect('/')

            else:
                messages.info(
                    request, 'Intresting...  Please Check Your USERNAME/PASSWORD, Might Have Gone Wrong')
                return redirect('/')

        elif 'btnstudent' in request.POST:
            username = request.POST['emailEmail']
            password = request.POST['password']
            # print('Email: '+email , 'Password: '+password)
            user = authenticate(request, username=username, password=password)
            print('user: ', user)
            if user is not None:
                if user.groups.filter(name__in=['Student']).exists():
                    login(request, user)
                    print('working')
                    return redirect('u/student/'+request.user.username)
                else:
                    messages.info(request, username+' Is Not A Student')
                    return redirect('/')

            else:
                messages.info(
                    request, 'Intresting...  Please Check Your USERNAME/PASSWORD, Might Have Gone Wrong')
                return redirect('/')


@login_required(login_url='/')
def batchView(request, schoolname, batchurl):
    if request.user in User.objects.filter(groups__name='School').all():
        if request.user.username == schoolname:
            from .models import school
            from .models import batch

            skl = school.objects.get(user=request.user)
            if batch.objects.filter(school_reference=skl, batch_url=batchurl).exists():
                if User.objects.filter(username=schoolname, groups__name='School').exists():
                    skl = school.objects.get(user=request.user)
                    if batch.objects.filter(school_reference=skl, batch_url=batchurl).exists():
                        skl = school.objects.get(user=request.user)
                        batchs = batch.objects.get(
                            school_reference=skl, batch_url=batchurl)
                        students = student.objects.filter(
                            school_reference_id_student=skl, batch_reference_id_student=batchs).all()
                        msgs = ChatBatch.objects.filter(
                            school_reference_id_chat=skl, batch_reference_id_chat=batchs).all()

                        y = []
                        z = []
                        stdCount = len(students)
                        msgCount = len(msgs)
                        batchPostData = []

                        for i in students:
                            print(i)
                            
                            updata = student.objects.get(id=i.id)
                            udata = User.objects.get(id=updata.user.id)
                            postData = post.objects.filter(user=udata).all()
                            for j in postData:
                                pd = {"id": j.id , 'media': j.media }
                                batchPostData.append(pd)

                        data = [
                            {'BATCH_ID': batchs.id,
                                'BATCH': [{
                                    'school_profilePicture': skl.school_propic.url,
                                    'School_description': skl.School_description,
                                    'School': request.user.username,
                                    'batch_url': batchs.batch_url,
                                    'batch_year': str(batchs.batch_year.year),
                                    'batch_strength': batchs.batch_strength,
                                    'batch_description': batchs.batch_description,
                                    'students_set': {
                                        'students_count': stdCount,
                                        'students_all': y,
                                    },
                                    'msgs': {
                                        'msgCount': msgCount,
                                        'msgContent': z,
                                    },
                                }],
                                'post' : batchPostData

                             }]

                        print(data)
                        stdCount = Count(students)
                        for i in students:
                            x = dict(student_id=i.id,
                                     student_details=dict(
                                         student_url=i.student_url,
                                         student_name=i.user.username,
                                         student_aka_name=i.student_aka_name,
                                         student_profilePicture=i.student_propic.url,
                                         student_std=i.student_std,
                                         student_address=dict(
                                             address_state=i.student_address_state,
                                             address_district=i.student_address_district,
                                             address_area=i.student_address_area,
                                         ),
                                         student_description=i.student_description
                                     )
                                     )
                            y.append(x)
                        for b in msgs:
                            a = dict(msgid=int(b.id),
                                     msgUser=b.user.username,
                                     msgMsg=b.chat,
                                     msgDate=str(b.date),
                                     msgEdit=b.edited
                                     )
                            z.append(a)
                        # s1 = json.dumps(data)


                        # json_object = json.loads(s1)
                        
                        # json_formatted_str = json.dumps(json_object, indent=2)

                        return render(request, 'batch.html', {'data': data})
                        # return HttpResponse(json_formatted_str, content_type="application/json")
                    else:
                        print("1")
                else:
                    return HttpResponse("You are not a")
            else:
                return HttpResponse("batch doesnt exists")

        else:
            return HttpResponse("Your are Not authorized to this School and batch")

    elif request.user in User.objects.filter(groups__name='Student').all():
        if student.objects.filter(user=request.user).exists():
            from .models import school
            from .models import batch
            userr = User.objects.get(username=schoolname)
            skl = school.objects.get(user=userr)
            if batch.objects.filter(school_reference=skl, batch_url=batchurl).exists():
                if User.objects.filter(username=request.user.user_student.school_reference_id_student.user, groups__name='School').exists():
                    if school.objects.filter(user=request.user.user_student.school_reference_id_student.user).exists() and batch.objects.filter(batch_url=batchurl).exists():
                        bth = batch.objects.get(batch_url=batchurl)
                        skl = school.objects.get(
                            user=request.user.user_student.school_reference_id_student.user)
                        if student.objects.filter(school_reference_id_student=skl, batch_reference_id_student=bth).exists():
                            if batch.objects.filter(school_reference=skl, batch_url=batchurl).exists():
                                skl = school.objects.get(
                                    user=request.user.user_student.school_reference_id_student.user)
                                batchs = batch.objects.get(
                                    school_reference=skl, batch_url=batchurl)
                                students = student.objects.filter(
                                    school_reference_id_student=skl, batch_reference_id_student=batchs).all()
                                msgs = ChatBatch.objects.filter(
                                    school_reference_id_chat=skl, batch_reference_id_chat=batchs).all()

                                y = []
                                z = []
                                stdCount = len(students)
                                msgCount = len(msgs)

                                batchPostData = []

                                for i in students:
                                    print(i)
                                    
                                    updata = student.objects.get(id=i.id)
                                    udata = User.objects.get(id=updata.user.id)
                                    postData = post.objects.filter(user=udata).all()
                                    for j in postData:
                                        pd = {"id": j.id , 'media': j.media }
                                        batchPostData.append(pd)

                                data = [
                                    {'BATCH_ID': batchs.id,
                                        'BATCH': [{
                                            'school_profilePicture': skl.school_propic.url,
                                            'School': skl.user.username,
                                            'batch_url': batchs.batch_url,
                                            'batch_year': str(batchs.batch_year.year),
                                            'batch_strength': batchs.batch_strength,
                                            'batch_description': batchs.batch_description,
                                            'students_set': {
                                                'students_count': stdCount,
                                                'students_all': y
                                            },
                                            'msgs': {
                                                'msgCount': msgCount,
                                                'msgContent': z,
                                            },
                                        }],
                                        'post': batchPostData

                                     }]
                                stdCount = Count(students)
                                for i in students:
                                    x = dict(student_id=i.id,
                                             student_details=dict(
                                                 student_url=i.student_url,
                                                 student_name=i.user.username,
                                                 student_aka_name=i.student_aka_name,
                                                 student_profilePicture=i.student_propic.url,
                                                 student_std=i.student_std,
                                                 student_address=dict(
                                                     address_state=i.student_address_state,
                                                     address_district=i.student_address_district,
                                                     address_area=i.student_address_area,
                                                 ),
                                                 student_description=i.student_description
                                             )
                                             )
                                    y.append(x)
                                for b in msgs:
                                    a = dict(msgid=int(b.id),
                                             msgUser=b.user.username,
                                             msgMsg=b.chat,
                                             msgDate=str(b.date),
                                             msgEdit=b.edited
                                             )
                                    z.append(a)
                                # s1 = json.dumps(data)

                                # json_object = json.loads(s1)

                                # json_formatted_str = json.dumps(
                                    # json_object, indent=2)

                                return render(request, 'batch.html', {'data': data})
                                # return HttpResponse(json_formatted_str, content_type="application/json")
                            else:
                                print("1")
                        else:
                            return HttpResponse("You are not in this skl")
                else:
                    return HttpResponse("You are not a")
            else:
                return HttpResponse("batch doesnt exists")

        else:
            return HttpResponse("Your are Not authorized to this School and batch")


@login_required(login_url='/')
def studentView(request, studenturl):
    if request.user.is_authenticated:
        if request.user in User.objects.filter(groups__name='School').all():
            if student.objects.filter(student_url=studenturl).exists():
                skl = school.objects.get(user=request.user)

                if student.objects.filter(student_url=studenturl, school_reference_id_student=skl).exists():

                    skl = school.objects.get(user=request.user)

                    stud = student.objects.get(
                        student_url=studenturl, school_reference_id_student=skl)
                    data = [{'SCHOOL': stud.school_reference_id_student.user.username,
                             'STUDENT':
                            {'STUDENT_ID': stud.id,
                             'STUDENT_DETAILS': [{

                                 'student_name': stud.user.username,
                                 'student_aka_name': stud.student_aka_name,
                                 'student_url': stud.student_url,
                                 'student_propic': stud.student_propic.url,
                                 'student_std': stud.student_std,
                                 'student_description': stud.student_description,
                                 'students_address': {
                                     'student_address_state': stud.student_address_state,
                                     'student_address_district': stud.student_address_district,
                                     'student_address_area': stud.student_address_area,
                                 }
                             }]

                             }}]

                    s1 = json.dumps(data)

                    json_object = json.loads(s1)

                    json_formatted_str = json.dumps(json_object, indent=2)

                    return HttpResponse(json_formatted_str, content_type="application/json")

                    # return render(request,'batch.html',{'data':data})

                else:
                    print('doest exsis in this school')
            else:
                print(' stud does not exsis')

        return HttpResponse(request, 'student')


def logoutUser(request):
    logout(request)
    return redirect('/')


def NotFoundPage404(request):
    return render(request, '404.html')


@login_required(login_url='/')
def adminDataBatch(request, schoolId, batchId):
    if request.user in User.objects.filter(groups__name='Admin').all():
        skl = school.objects.get(id=schoolId)
        batchs = batch.objects.get(school_reference=skl, id=batchId)
        students = student.objects.filter(
            school_reference_id_student=skl, batch_reference_id_student=batchs).all()
        msgs = ChatBatch.objects.filter(
            school_reference_id_chat=skl, batch_reference_id_chat=batchs).all()

        y = []
        z = []
        stdCount = len(students)
        msgCount = len(msgs)
        data = [{'SCHOOL': skl.user.username,
                 'BATCH':
                {'BATCH_ID': batchs.id,
                 'BATCH_DETAILS': [{

                     'batch_url': batchs.batch_url,
                     'batch_year': batchs.batch_year.year,
                     'batch_strength': batchs.batch_strength,
                     'batch_description': batchs.batch_description,
                     'students_set': {
                         'students_count': stdCount,
                         'students_all': y
                     },
                     'msgs': {
                         'msg-count': msgCount,
                         'msg-content': z,
                     },

                 }]

                 }}]
        stdCount = Count(students)
        for i in students:
            x = dict(student_id=i.id,
                     student_details=dict(
                         student_url=i.student_url,
                         student_name=i.user.username,
                         student_aka_name=i.student_aka_name,
                         student_profilePicture=i.student_propic.url,
                         student_std=i.student_std,
                         student_address=dict(
                             address_state=i.student_address_state,
                             address_district=i.student_address_district,
                             address_area=i.student_address_area,
                         ),
                         student_description=i.student_description
                     )
                     )
            y.append(x)

        for b in msgs:
            a = dict(msgid=int(b.id),
                     msgUser=b.user.username,
                     msgMsg=b.chat,
                     msgDate=str(b.date),
                     msgEdit=b.edited
                     )
            z.append(a)
        s1 = json.dumps(data)

        json_object = json.loads(s1)

        json_formatted_str = json.dumps(json_object, indent=2)

        return HttpResponse(json_formatted_str, content_type="application/json")

    else:
        return HttpResponse("This is only for admins")


@login_required(login_url='/')
def adminDataSchool(request, schoolId):
    if request.user in User.objects.filter(groups__name='Admin').all():
        skl = school.objects.get(id=schoolId)
        batchs = batch.objects.filter(school_reference=skl).all()

        y = []

        data = [
            {'School': skl.user.username,
             'SCHOOL_ID': skl.id,
             'SCHOOL': [{

                 'school_url': skl.school_url,
                 'School_ProfilePicture': skl.school_propic.url,
                 'School_Description': skl.School_description,
                        'School_Address': {
                            'Address_State': skl.school_address_state,
                            'Address_District': skl.school_address_district,
                            'Address_Area': skl.school_address_area,
                        },
                        'No_Of_Batchs': skl.school_noof_batch,
                        'BATCHS': y

                        }]

             }]

        for i in batchs:
            noofstud = len(student.objects.filter(
                batch_reference_id_student=i.id).all())

            x = dict(Batch_id=i.id,
                     Batch_Details=dict(
                         Batch_url=i.batch_url,
                         batch_year=i.batch_year.year,
                         batch_std=i.batch_std,
                         batch_strength=i.batch_strength,
                         batch_description=i.batch_description,
                         No_of_students=noofstud,
                     ),
                     link='https://wemeet-web.herokuapp.com/admin/data/school/' +
                     str(skl.id)+'/batch/'+str(i.id)

                     )
            y.append(x)
        s1 = json.dumps(data)

        json_object = json.loads(s1)

        json_formatted_str = json.dumps(json_object, indent=2)

        return HttpResponse(json_formatted_str, content_type="application/json")

    else:
        return HttpResponse("This is only for admins")


@login_required(login_url='/')
def adminDataAllSchool(request):
    if request.user in User.objects.filter(groups__name='Admin').all():
        skl = school.objects.filter().all()
        cntskl = len(skl)

        y = []

        data = [{
            'No_Of_School': cntskl,
                'SCHOOL': y
                }]

        for i in skl:
            noofstud = len(student.objects.filter(
                school_reference_id_student=i.id).all())
            x = dict(School_id=i.id,
                     School_Details=dict(
                         school_name=i.user.username,
                         school_url=i.school_url,
                         school_propic=i.school_propic.url,
                         School_description=i.School_description,
                         school_noof_batchs=i.school_noof_batch,
                         school_noof_students=noofstud,
                         School_address=dict(
                             address_state=i.school_address_state,
                             address_district=i.school_address_district,
                             address_area=i.school_address_area,
                         )
                     ),
                     link='https://wemeet-web.herokuapp.com/admin/data/school/' +
                     str(i.id)

                     )
            y.append(x)
        s1 = json.dumps(data)

        json_object = json.loads(s1)

        json_formatted_str = json.dumps(json_object, indent=2)

        return HttpResponse(json_formatted_str, content_type="application/json")

    else:
        return HttpResponse("This is only for admins")


def mailTest(request):
    return render(request, 'Mail/RegisterSucess.html')


def submitCode(request, codee):
    if request.POST.get('code') == '':
        print(codee)
        return HttpResponse(status=204)
    else:
        print(codee)
        code = request.POST.get('code')
        if code == codee:
            return HttpResponse(code)
        else:
            return HttpResponse(status=204)


def mailacc(request):

    ResetCode = ascii_uppercase+'1234567890'
    urlsrandomschool = random.choices(ResetCode, k=7)
    randomResetCode = ""
    for randomurlloop in urlsrandomschool:
        randomResetCode += randomurlloop

    mail = request.POST.get('mail')

    user = User.objects.get(email=mail)
    recipient_list = [mail]
    data = {
        'username': user.username,
        'code': randomResetCode,
    }

    msg_plain = 'Test'
    msg_html = render_to_string('Mail/PasswordResetMail.html', {'data': data})

    email_from = settings.EMAIL_HOST_USER

    if 'mailsubm' in request.POST:

        send_mail(
            user.username+', Password Reset --WeMeet',
            msg_plain,
            email_from,
            recipient_list,
            html_message=msg_html,
        )
        if user in User.objects.filter(groups__name='School').all():
            school.objects.filter(user=user).update(code=randomResetCode)
            return HttpResponse(status=204)
        if user in User.objects.filter(groups__name='Student').all():
            student.objects.filter(user=user).update(code=randomResetCode)
            return HttpResponse(status=204)
        return HttpResponse(status=204)

    elif 'codesubm' in request.POST:
        if user in User.objects.filter(groups__name='School').all():
            skl = school.objects.get(user=user)

            if request.POST.get('code') == '':
                return HttpResponse(status=204)
            else:
                code = request.POST.get('code')
                if code == skl.code:
                    return redirect('/passwordreset/'+str(code)+'/'+str(user.id))
                else:
                    return HttpResponse(status=204)
        if user in User.objects.filter(groups__name='Student').all():
            stud = student.objects.get(user=user)

            if request.POST.get('code') == '':
                return HttpResponse(status=204)
            else:
                code = request.POST.get('code')

                if code == stud.code:
                    return redirect('/passwordreset/'+str(code)+'/'+str(user.id))
                else:
                    return HttpResponse(status=204)


def passreset(request, code, user):

    if school.objects.filter(user=user, code=code).exists() or student.objects.filter(user=user, code=code).exists():
        if 'passs' in request.POST:
            passwd = request.POST.get('passwordReset')
            conpasswd = request.POST.get('conpasswordReset')
            print(passwd, conpasswd)
            if conpasswd == passwd:
                user = User.objects.get(id=user)
                user.set_password(passwd)
                user.save()
                messages.info(request, ' Password Changed Succesfully')

                return redirect('/')
            else:
                return HttpResponse(status=204)
        else:
            data = {'code': code, 'user': user}
            # skl= school.objects.get(user=user,code=code)
            return render(request, 'passwordReset.html', {'data': data})


@login_required(login_url='/')
def updatepage(request, userid, userurl):
    if request.user.id == userid:
        user = User.objects.get(id=userid)

        if request.method == 'POST':
            propic = request.FILES.get('propic')
            username = request.POST.get('username')
            password = request.POST.get('password')
            displayname = request.POST.get('displayname')
            # password = request.POST.get('password')
            description = request.POST.get('description')
            passchk = user.check_password(password)
            if passchk:
                if user in User.objects.filter(groups__name='School').all():
                    if propic is None:
                        from .models import school

                        User.objects.filter(id=userid).update(
                            username=username)
                        school.objects.filter(school_url=userurl).update(
                            School_description=description)
                        return redirect('/u/school/'+username)

                    else:
                        from .models import school

                        User.objects.filter(id=userid).update(
                            username=username)
                        school.objects.filter(school_url=userurl).update(
                            School_description=description)
                        skl = school.objects.get(school_url=userurl)
                        url = skl.school_propic.url
                        print(url)
                        url = url.replace(
                            'https://res.cloudinary.com/wemeetweb/image/upload/v1/media/ProfilePicture/ProfilePicture/', '')
                        cloudinary.uploader.destroy(
                            "media/ProfilePicture/ProfilePicture/"+url)
                        # cloudinary.uploader.destroy(url)

                        print(url)
                        imageupload = get_object_or_404(
                            school, school_url=userurl)
                        imageupload.school_propic = propic
                        imageupload.save()

                        return redirect('/u/school/'+username)
                if user in User.objects.filter(groups__name='Student').all():
                    if propic is None:

                        from .models import student

                        User.objects.filter(id=userid).update(
                            username=username)
                        student.objects.filter(student_url=userurl).update(
                            student_description=description, student_aka_name=displayname)
                        return redirect('/u/student/'+username)

                    else:
                        from .models import student

                        User.objects.filter(id=userid).update(
                            username=username)
                        student.objects.filter(student_url=userurl).update(
                            student_description=description, student_aka_name=displayname)
                        # student.objects.filter(student_url=userurl).update(student_propic=propic)
                        skl = student.objects.get(student_url=userurl)
                        url = skl.student_propic.url
                        print(url)
                        url = url.replace(
                            'https://res.cloudinary.com/wemeetweb/image/upload/v1/media/ProfilePicture/ProfilePicture/', '')
                        cloudinary.uploader.destroy(
                            "media/ProfilePicture/ProfilePicture/"+url)
                        # cloudinary.uploader.destroy(url)

                        print(url)
                        imageupload = get_object_or_404(
                            student, student_url=userurl)
                        imageupload.student_propic = propic
                        imageupload.save()
                        return redirect('/u/student/'+username)
            else:
                messages.info(request, request.user.username +
                              ", Invalid Password")
                return redirect('/update/'+str(userid)+'/'+userurl)

        else:
            if user in User.objects.filter(groups__name='School').all():
                from .models import school
                user = User.objects.get(id=userid)
                school = school.objects.get(school_url=userurl)
                url = school.school_propic.url
                # url =url.replace('v1','v1626931405')
                data = {
                    'user': user.username,
                    'userpass': user.password,
                    'profilepic': url,
                    'desc': school.School_description
                }

                return render(request, "profileupdate.html", {'data': data})
            if user in User.objects.filter(groups__name='Student').all():
                from .models import student
                user = User.objects.get(id=userid)
                student = student.objects.get(student_url=userurl)
                print(student.student_aka_name)
                data = {
                    'user': user.username,
                    'displayName': student.student_aka_name,
                    'profilepic': student.student_propic.url,
                    'desc': student.student_description
                }
                return render(request, "profileupdate.html", {'data': data})


@login_required(login_url='/')
def batchMsg(request, schoolname, batchurl):
    if request.method == 'POST':
        schoolName = User.objects.get(username=schoolname)
        user = User.objects.get(username=request.user.username)
        skl = school.objects.get(user=schoolName)
        btch = batch.objects.get(school_reference=skl, batch_url=batchurl)
        msgChat = request.POST.get('msg')
        if msgChat != '':
            msg = ChatBatch.objects.create(

                user=user,
                chat=msgChat,
                school_reference_id_chat=skl,
                batch_reference_id_chat=btch,

            )
            msg.save()
            data = {'data': 'working '+msgChat}
            return HttpResponse(json.dumps(data))

        else:
            return HttpResponse(status=204)


@login_required(login_url='/')
def msgView(request, schoolname, batchurl):
    schoolName = User.objects.get(username=schoolname)
    skl = school.objects.get(user=schoolName)
    batchs = batch.objects.get(school_reference=skl, batch_url=batchurl)
    msgs = ChatBatch.objects.filter(
        school_reference_id_chat=skl, batch_reference_id_chat=batchs).all()
    std = student.objects.filter(
        school_reference_id_student=skl, batch_reference_id_student=batchs).all()
    z = []
    msgCount = len(msgs)

    data = {'msgs': {
        'msgCount': msgCount,
        'msgContent': z,
    },
    }

    for b in reversed(msgs):
        if b.user == schoolName:
            skl = school.objects.get(user=schoolName)
            propic = skl.school_propic.url
        else:
            for i in reversed(std):
                if i.user.username == b.user.username:
                    propic = i.student_propic.url
        a = dict(msgid=int(b.id),
                 msgUser=b.user.username,
                 msgUserPfp=propic,
                 msgMsg=b.chat,
                 msgDate=str(b.date.hour)+':'+str(b.date.minute) +
                 ' '+str(b.date.date()),
                 msgEdit=b.edited
                 )
        z.append(a)
    return HttpResponse(json.dumps(data))

# def tagUserChat(request):

#     name = request.POST.get('msg')
#     userdata = User.objects.filter(username__icontains=name).all()
#     data =[]
#     for i in userdata:
#         username = i.username
#         dataloop = {'name':username}
#         data.append(dataloop)
#     return HttpResponse(json.dumps(data))


@login_required(login_url='/')
def updatchat(request, schoolName, batchurl, user, msgid):

    getchat = request.POST.get('uchat')
    if request.user.username == user:
        skluser = User.objects.get(username=schoolName)
        msgUser = User.objects.get(username=user)
        skl = school.objects.get(user=skluser)
        btch = batch.objects.get(school_reference=skl, batch_url=batchurl)
        if ChatBatch.objects.filter(user=msgUser, school_reference_id_chat=skl, batch_reference_id_chat=btch, id=msgid).exists():
            ChatBatch.objects.filter(user=msgUser, school_reference_id_chat=skl,
                                     batch_reference_id_chat=btch, id=msgid).update(chat=getchat, edited=True)
            return HttpResponse(json.dumps('success'))
        else:
            return HttpResponse('nope')
    else:
        return HttpResponse('nope')


@login_required(login_url='/')
def deletechat(request, schoolName, batchurl, user, msgid):

    if request.user.username == user:
        skluser = User.objects.get(username=schoolName)
        msgUser = User.objects.get(username=user)
        skl = school.objects.get(user=skluser)
        btch = batch.objects.get(school_reference=skl, batch_url=batchurl)
        if ChatBatch.objects.filter(user=msgUser, school_reference_id_chat=skl, batch_reference_id_chat=btch, id=msgid).exists():
            ChatBatch.objects.filter(
                user=msgUser, school_reference_id_chat=skl, batch_reference_id_chat=btch, id=msgid).delete()
            return HttpResponse(json.dumps('success'))
        else:
            return HttpResponse('nope')
    else:
        return HttpResponse('nope')


def reactDataSchool(request, schoolId):
    skl = school.objects.get(id=schoolId)
    batchs = batch.objects.filter(school_reference=skl).all()

    y = []

    data = [
        {'School': skl.user.username,
         'SCHOOL_ID': skl.id,
         'SCHOOL': [{

             'school_url': skl.school_url,
             'School_ProfilePicture': skl.school_propic.url,
             'School_Description': skl.School_description,
                    'School_Address': {
                        'Address_State': skl.school_address_state,
                        'Address_District': skl.school_address_district,
                        'Address_Area': skl.school_address_area,
                    },
                    'No_Of_Batchs': skl.school_noof_batch,
                    'BATCHS': y

                    }]

         }]

    for i in batchs:
        noofstud = len(student.objects.filter(
            batch_reference_id_student=i.id).all())

        x = dict(Batch_id=i.id,
                 Batch_Details=dict(
                     Batch_url=i.batch_url,
                     batch_year=i.batch_year.year,
                     batch_std=i.batch_std,
                     batch_strength=i.batch_strength,
                     batch_description=i.batch_description,
                     No_of_students=noofstud,
                 ),
                 link='http://192.168.0.4:8000/admin/data/school/' +
                 str(skl.id)+'/batch/'+str(i.id)

                 )
        y.append(x)
    s1 = json.dumps(data)

    json_object = json.loads(s1)

    json_formatted_str = json.dumps(json_object, indent=2)

    return HttpResponse(json_formatted_str, content_type="application/json")


@login_required(login_url='/')
def batchUpdate(request, schoolname, batchurl):
    if request.method == 'POST':
        # print(str(request.user) + '=='+ str(schoolname))
        # print(request.user.username==schoolname)
        if schoolname == request.user.username:
            if 'delete' in request.POST:
                user = User.objects.get(username=schoolname)
                password = request.POST.get('password')
                passchk = user.check_password(password)
                print('1')
                if passchk:
                    user = User.objects.get(username=schoolname)
                    skl = school.objects.get(user=user)
                    batchs = batch.objects.filter(
                        school_reference=skl, batch_url=batchurl).delete()
                    print('2')

                    return redirect('/u/school/'+request.user.username)
                else:
                    print('3')

                    messages.info(request, request.user.username +
                                  ", Invalid Password")
                    return redirect('/batchupdate/'+schoolname+'/'+batchurl)
            else:

                user = User.objects.get(username=schoolname)
                batchStrength = request.POST.get('batchStrength')
                batchDescription = request.POST.get('batchDescription')
                batch_year = request.POST.get('batch_year')
                password = request.POST.get('password')
                passchk = user.check_password(password)
                print('4')

                if passchk:

                    user = User.objects.get(username=schoolname)
                    skl = school.objects.get(user=user)
                    btch = batch.objects.get(
                        school_reference=skl, batch_url=batchurl)
                    batchs = batch.objects.filter(school_reference=skl, batch_url=batchurl).update(
                        batch_strength=batchStrength, batch_description=batchDescription, batch_year=str(batch_year)+'-'+str(btch.batch_year.month)+'-'+str(btch.batch_year.day))
                    print('5')
                    return redirect('/school/'+schoolname+'/batch/'+batchurl)
                else:
                    print('6')

                    messages.info(request, request.user.username +
                                  ", Invalid Password")
                    return redirect('/batchupdate/'+schoolname+'/'+batchurl)
        else:
            return HttpResponse('You are not authorized')
    else:
        user = User.objects.get(username=schoolname)
        skl = school.objects.get(user=user)
        batchs = batch.objects.get(school_reference=skl, batch_url=batchurl)
        print(batchs.batch_description)
        print('7')

        data = {
            'batchStrength': batchs.batch_strength,
            'batchDescription': batchs.batch_description,
            'batch_year': batchs.batch_year.year,
            'batch_url': batchs.batch_url,
        }
        print(batchs.batch_url)
        return render(request, 'batchUpdate.html', {'data': data})


def DragNDrop(request):
    return render(request, 'dragNdrop.html')


@login_required(login_url='/')
def addPost(request, user):
    if request.user.username == user:
        media = request.FILES.get('media')
        if media is not None:
            print(media)
            desc = request.POST.get('desc')
            postVar = post.objects.create(
                user=request.user,
                media=media,
                description=desc,


            )
            postVar.save()
            return HttpResponse(json.dumps('Success'))
        else:
            return HttpResponse(status=204)

    else:
        return HttpResponse(json.dumps('Your are not authorised'))


@login_required(login_url='/')
def displayPostStd(request):
    if request.user.is_authenticated:
        if post.objects.filter(user=request.user).exists():
            posts = post.objects.filter(user=request.user).all()
            postAll = {'bool': True,
                       'post':
                       [{'postid': i.id,
                        'postMedia': i.media.url,
                         'postDescription': i.description,
                         'postDate': str(i.date.hour)+':'+str(i.date.minute)+' '+str(i.date.date()),
                         'likes': [{'user': j.username,
                                   'userProfilePic': j.user_student.student_propic.url
                                    }
                                   for j in i.likes.all()]

                         } for i in reversed(posts)]
                       }
        else:
            postAll = {'bool': False,
                       'post': []
                       }

        return HttpResponse(json.dumps(postAll))


def jsonAdmin(request):
    user = User.objects.get(id=request.user.id)
    if user.groups.filter(name__in=['Admin']).exists():
        data = [
            {'adminlinks': [
                {
                    'schools': 'admin/data/school',
                    'school': 'admin/data/school/int:schoolId',
                    'batch': 'admin/data/school/int:schoolId/batch/int:batchId'
                }
            ]
            }
        ]
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse('You Are Not Authorized')


def addBatch(request, schoolname):
    if request.user.username == schoolname:
        if request.method == 'POST':
            noofbatch = request.POST.get('noofbatch')
            std = request.POST.get('std')
            fromy = request.POST.get('from')
            Strength = request.POST.get('Strength')
            Description = request.POST.get('Description')
            # to =  request.POST.get('to')
            if noofbatch != '' and std != '' and Strength != '' and Description != '' and fromy != '':
                user = User.objects.get(username=request.user.username)
                from .models import school
                schoolget = school.objects.get(user=user)
                for i in range(int(noofbatch)):
                    url = ascii_uppercase+ascii_lowercase+'1234567890'

                    randomurl = ""

                    urlsrandomschool = random.choices(url, k=30)
                    for randomurlloop in urlsrandomschool:
                        randomurl += randomurlloop
                    batchadd = batch.objects.create(
                        batch_year=str(int(fromy)+i)+'-06-14',
                        batch_std=std,
                        batch_url=randomurl,
                        batch_strength=Strength,
                        batch_description=Description,
                        school_reference=schoolget

                    )
                    batchadd.save()
                return redirect('/u/school/'+request.user.username)
            else:
                messages.info(request, 'Please Fill The Form....!')
                return redirect('/addBatch/'+request.user.username)
        else:
            return render(request, 'addbatch.html')
    else:
        return HttpResponse('Not Authorized')


def postView(request, postid):
    if post.objects.filter(id=postid).exists():
        pst = post.objects.get(id=postid)
        data = {'user': pst.user, 'media': pst.media,
                'description': pst.description, 'likes': pst.likes, 'date': pst.date}
        return render(request, 'post.html', {'data': data})
