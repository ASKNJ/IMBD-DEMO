from django.shortcuts import render, redirect, reverse
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from my_App.utils import verify_user, validate_keys
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from my_App.models import UserApiToken, ImbdRatedMovies
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
import json, uuid
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View


def error_404_view(request, exception):
    render_template = 'my_App/404.html'
    base_template = 'my_App/base.html'
    return render(request, render_template, {'base_template': base_template})
    

def index(request):
    render_template = 'my_App/login_card.html'
    base_template = 'my_App/base.html'
    if request.user.is_authenticated:
        print("get started")
        return redirect('myapp:get_started')
    return render(request, render_template, {'base_template': base_template})


def get_signup_data(request):
    status, msg = 'F', 'Something went wrong while authenticating!'
    if request.method == 'POST' and request.is_ajax() and request.POST.get('action', False) == 'gdata':
        google_data = request.POST.get('google_response_data', None)
        if google_data:
            google_user_data = google_data.split(",")
            fname = google_user_data[1].split(' ')[0]
            lname = google_user_data[1].split(' ')[1]
            email = google_user_data[5]
            password = make_password(email)
            user_exists = User.objects.filter(username__iexact=email).exists()
            if user_exists:
                user = User.objects.get(username__iexact=email)
                login(request, user)
                return JsonResponse({"status": "A", 'message': "Already registered"})
            User.objects.create(first_name=fname, last_name=lname, email=email, is_active=True,
                                last_login=timezone.now(), date_joined=timezone.now(), username=email,
                                password=password)
            user = authenticate(request, username=email, password=email)
            if user:
                login(request, user)
            status = 'S'
            msg = 'Welcome!'
        return JsonResponse({"status": status, 'message': msg})


@login_required
def get_started(request):
    render_template = 'my_App/get_started.html'
    base_template = 'my_App/base.html'
    return render(request, render_template, {'base_template': base_template, 'main': "Y"})


@login_required
def user_logout(request):
    logout(request)
    return redirect("myapp:home")


@login_required
def set_admin(request):
    user, message = str(request.user), "You are already admin."
    is_admin = User.objects.filter(username__iexact=user, is_superuser=True, is_active=True).exists()
    if request.method == "POST":
        if not is_admin:
            token = uuid.uuid4().hex
            user = User.objects.get(username__iexact=user)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            UserApiToken.objects.create(USER_ID_id=user.id, USER_API_TOKEN=token, IS_ACTIVE=True)
        return redirect('myapp:set_Admin')
    if request.method == 'GET':
        render_template = "my_App/setadmin_page.html"
        main = "my_App/base.html"
        base = 'my_App/get_started.html'
        msg = f"Added {request.user} as admin user" if is_admin else message
        return render(request, render_template,
                      {"base_template": main, 'get_started': base, 'admin': is_admin, 'msg': msg, "on_admin": "Y"})


@login_required
def user_api(request):
    render_template = 'my_App/user_api_interface.html'
    baset = 'my_App/get_started.html'
    base = 'my_App/base.html'
    userid = User.objects.get(username__iexact=str(request.user)).id
    token_exists = UserApiToken.objects.filter(USER_ID_id=userid).exists()
    key = UserApiToken.objects.filter(USER_ID_id=userid).values("USER_API_TOKEN")[0][
        "USER_API_TOKEN"] if token_exists else None
    if request.method == 'POST' and not token_exists:
        api_token = uuid.uuid4().hex
        UserApiToken.objects.create(USER_ID_id=userid, USER_API_TOKEN=api_token, IS_ACTIVE=True,
                                    CREATED_DATE=timezone.now(),
                                    UPDATED_DATE=timezone.now())
        return redirect("myapp:user_api")
    return render(request, render_template, {'get_started': baset, "main": "N", "base_template": base, "key": key})


@method_decorator(csrf_exempt, name='dispatch')
class ManipulateData(View):
    def check_admin(func):
        def inner(self, request, **kwargs):
            auth = request.headers.get("Authorization", False)
            if auth:
                userid = UserApiToken.objects.get(USER_API_TOKEN=auth).id
                is_admin = User.objects.filter(id=userid, is_superuser=True).exists()
                if is_admin:
                    if kwargs.get("id", False):
                        return func(self, request, kwargs["id"], auth)
                    else:
                        return func(self, request, auth)
                else:
                    return JsonResponse({"message": "You do not have admin rights."})
            else:
                return JsonResponse({"message": "Need a valid token to access this API."})

        return inner

    @check_admin
    def post(self, request, *args):
        data = json.loads(request.body)
        if type(data) is dict:
            print("adding data")
            validate_keys(request, data.keys())
            ImbdRatedMovies.objects.create(POPULARITY=data["99popularity"], DIRECTOR=data["director"],
                                           GENRE=data["genre"], IMDB_SCORE=data["imdb_score"],
                                           MOVIE_NAME=data["name"], CREATE_USER=args[0])
        else:
            print("adding data")
            validate_keys(request, data[0].keys())
            for row in data:
                ImbdRatedMovies.objects.create(POPULARITY=row["99popularity"], DIRECTOR=row["director"],
                                               GENRE=row["genre"], IMDB_SCORE=row["imdb_score"],
                                               MOVIE_NAME=row["name"], CREATE_USER=args[0])
        message = "Data loaded Successfully"
        return JsonResponse({"message": message, "status": "ok"})

    @check_admin
    def patch(self, request, *args):
        param, row = json.loads(request.body), {}
        data_id_exists = ImbdRatedMovies.objects.filter(id=args[0]).exists()
        keys = list(param.keys())
        valid_keys = validate_keys(request, keys)
        if not valid_keys:
            return JsonResponse({"message": f"You have invalid keys.", "status": "Fail"})
        if data_id_exists:
            for col, new_value in param.items():
                col = col.upper()
                row[col], row["UPDATED_DATE"], row["UPDATE_USER"] = new_value, timezone.now(), args[1]
                ImbdRatedMovies.objects.filter(id=args[0]).update(**row)
        else:
            return JsonResponse({"message": f"requested id: {args[0]} is not found", "status": "ok"})
        return JsonResponse({"message": f"{keys} updated for id: {args[0]}", "status": "ok"})

    @check_admin
    def delete(self, request, *args):
        id_exists = ImbdRatedMovies.objects.filter(id=args[0]).exists()
        if id_exists:
            row = ImbdRatedMovies.objects.get(id=args[0])
            row.delete()
        else:
            return JsonResponse({"message": f"requested id: {args[0]} is not found", "status": "ok"})
        return JsonResponse({"message": f"{keys} updated for id: {args[0]}", "status": "ok"})


@verify_user
def get_movies(request, *args):
    if request.method == "GET":
        if args[0]:
            print("auth version")
            all_movies = ImbdRatedMovies.objects.values("id", "POPULARITY", "DIRECTOR", "GENRE", "IMDB_SCORE",
                                                        "MOVIE_NAME")
            return JsonResponse({"status": "ok", "data": list(all_movies)}, safe=False)
        else:
            print("free version")
            all_movies = ImbdRatedMovies.objects.values("id", "POPULARITY", "DIRECTOR", "GENRE", "IMDB_SCORE",
                                                        "MOVIE_NAME").order_by("IMDB_SCORE")[:10]
            return JsonResponse({"status": "ok", "data": list(all_movies)}, safe=False)


@verify_user
def search_movies(request, *args):
    if request.method == "GET":
        if args[0]:
            movie = args[1]["movie"]
            movies = ImbdRatedMovies.objects.filter(MOVIE_NAME__icontains=movie).values("id", "POPULARITY", "DIRECTOR",
                                                                                        "GENRE", "IMDB_SCORE",
                                                                                        "MOVIE_NAME").distinct()
            return JsonResponse({"status": "ok", "data": list(movies)}, safe=False)
        else:
            return JsonResponse({"status": "ok", "data": "You don't have a valid token."})
