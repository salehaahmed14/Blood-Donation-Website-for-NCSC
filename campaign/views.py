from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection

from .models import Medical_Information, Campaign
from .forms import UserRegisterForm, PersonalInformationForm, InitialMedicalInformationForm, MedicalInformationForm, VolunteerForm

def home(request):
    co = Campaign.objects.all()
    ci1 = co[0]
    ci2 = co[1]
    ci3 = co[2]
    with connection.cursor() as cursor1:
        cursor1.callproc('get_amount_collected', (2,))
        amount_result1 = cursor1.fetchone()
        amount_collected_1 = round(amount_result1[0])
    with connection.cursor() as cursor2:
        cursor2.callproc('get_amount_collected', (3,))
        amount_result2 = cursor2.fetchone()
        amount_collected_2 = round(amount_result2[0])
    context = {
        'ci1': ci1,
        'ci2': ci2,
        'ci3': ci3,
        'amount_collected_1': amount_collected_1,
        'amount_collected_2': amount_collected_2
    }
    return render(request, 'campaign/home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        p_form = PersonalInformationForm(request.POST)
        m_form = InitialMedicalInformationForm(request.POST)
        if form.is_valid() and p_form.is_valid() and m_form.is_valid():
            p_user = form.save()
            pi = p_form.save(commit = False)
            pi.person_id = p_user
            pi.save()
            mi = m_form.save(commit = False)
            mi.person_id = p_user
            mi.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
        p_form = PersonalInformationForm()
        m_form = InitialMedicalInformationForm()
    return render(request, 'campaign/register.html', {'form': form, 'p_form': p_form, 'm_form': m_form})

@login_required(login_url='login')
def med_info_view(request):
    med_info = Medical_Information.objects.get(person_id = request.user)
    if request.method == 'POST':
        m_form = MedicalInformationForm(request.POST, instance=med_info)
        if m_form.is_valid():
            mi = m_form.save(commit=False)
            mi.person_id = request.user
            mi.save()

            with connection.cursor() as cursor3:
                cursor3.callproc('add_blood_collected', (med_info.person_id.id,))

            with connection.cursor() as cursor:
                cursor.callproc('get_bmi', (med_info.height, med_info.weight))
                bmi_result = cursor.fetchone()
                bmi = round(bmi_result[0])

            last_date = (med_info.last_donation.year * 10000) + (med_info.last_donation.month * 100) + (med_info.last_donation.day)
            with connection.cursor() as cursor1:
                cursor1.callproc('get_days_in_btw', (last_date,))
                date_result = cursor1.fetchone()
                days_in_btw = date_result[0]

            with connection.cursor() as cursor2:
                cursor2.callproc('get_age', (med_info.person_id.id,))
                b_result = cursor2.fetchone()
                age = round(b_result[0])

            if bmi < 19:
                messages.error(request, f'You Are Medically Unfit To Donate Blood! Your BMI is { bmi }')
            elif days_in_btw < 90:
                messages.error(request, f'{ days_in_btw } Days Since Your Last Donation! You Can Not Donate Twice Within 90 Days!')
            elif age < 18 or age > 60:
                messages.error(request, f'You Are Not Eligible To Donate Blood! Age Limit For Blood Donation is From 18 Years To 60 Years!')
            else:
                m_form.save_m2m()
                messages.success(request, f'Information Added For {request.user}!')
        return redirect('home')
    else:
        m_form = MedicalInformationForm(instance=med_info)
    return render(request, 'campaign/med_info.html', {'m_form': m_form})

@login_required(login_url='login')
def volunteer_view(request):
    if request.method == 'POST':
        v_form = VolunteerForm(request.POST)
        if v_form.is_valid():
            vi = v_form.save(commit=False)
            vi.volunteer_id = request.user
            vi.save()
            v_form.save_m2m()
            messages.success(request, f'Information Added For {request.user}!')
            return redirect('home')
    else:
        v_form = VolunteerForm()
    return render(request, 'campaign/volunteer.html', {'v_form': v_form})

def loginView(request):

    page = "login"

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        # Return user object or will give error

        if user is not None:
            login(request, user)
            next = request.POST.get("next_url")
            if next != '':
                return redirect(to=next)
            # It will session in the DB and browser
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')

    context = {"page": page}
    '''
    when a user is redirected to login page by the following decorator
    @login_required(login_url='login')

    This decorator passes a parameter next, which is actually the url
    where user was trying to go after which user wass redirected to login page 

    '''

    next = request.GET.get('next') if request.GET.get('next') != None else ''
    context["next_url"] = next

    return render(request, "campaign/login.html", context)


def logoutUser(request):
    logout(request)
    # Remove the authenticated user's ID from the request and flush their session data.
    return redirect('home')

def contact_us(request):
    return render(request, 'campaign/contact_us.html')

def about_us(request):
    return render(request, 'campaign/about_us.html')