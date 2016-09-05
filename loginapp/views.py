from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import get_perms, assign_perm


# Create your views here.
@login_required(login_url="login/")
def home(request):
    active_user = request.user
    # active_user.assign_perm()
    username = active_user.username
    patients = active_user.doctor.patients.all()
    has_commented = False
    sys_hint = 'sorry, no comments here.'
    if request.session.get('has_commented', True):
        # comment = "this is my comment."
        has_commented = True
        # request.session['has_comment'] = True
        sys_hint = "you've already commented."

    my_comment = "this is my comment."
    request.session['has_comment'] = True

    context = {
        'username': username,
        'patients': patients,
        'user': active_user,
        'has_commented': has_commented,
        'my_comment': my_comment,
        'sys_hint': sys_hint,

    }
    return render(request, "home.html", context)


@login_required(login_url='/login/')
def show_color(request):
    if 'favorite_color' in request.session:
        # return HttpResponse("your favorite color is %s a" % request.session["favorite_color"])
        return HttpResponse(request.COOKIES['sessionid'])
    else:
        return HttpResponse(request.COOKIES['sessionid'])


@login_required(login_url='login/')
def set_color(request):
    if "favorite_color" not in request.session:
        request.session["favorite_color"] = 'red'
        response = HttpResponse(request.session.keys())
        return response
    return HttpResponse(request.session.keys())
