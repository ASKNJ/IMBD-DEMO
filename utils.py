from my_App.models import UserApiToken


def verify_user(func):
    def inner_verify(request, **kwargs):
        auth_token = request.headers.get("Authorization", "Anonymous")
        token = UserApiToken.objects.filter(USER_API_TOKEN=auth_token).exists()
        if token and not kwargs:
            return func(request, token)
        else:
            print("kwargs there", auth_token)
            return func(request, token, kwargs)

    return inner_verify


def validate_keys(request, keys):
    valid_keys = ['99popularity', 'director', 'genre', 'imdb_score', 'name']
    res = [key for key in keys if key.lower() in valid_keys]
    if not res:
        return False
    return res
