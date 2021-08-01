const url_get_google_data = '/get_social_details/';
const url_home_redirect = '/';
const url_signup_home_redirect = '/get_started/';

function fetchdata_google(google_response_data_onform) {
    $.ajax({
        type: 'POST',
        contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        url: url_get_google_data,
        data: {
            'google_response_data': google_response_data_onform,
            action: 'gdata'
        },
        dataType: 'json',
        success: function (response_social) {
            if (response_social.status === 'S') {
                setTimeout(redirect_delay, 100);
            }
            if (response_social.status === 'A') {
                $("._m1").html("<p style='margin-top: .8em;'>" + response_social.message + "</p>");
                setTimeout(redirect_delay, 2000);
            }
        },
        error: function () {
            console.log("error in get data from google");
        }
    });
}

function redirect_delay() {
    location.href = url_signup_home_redirect;
}

function attachSignin(element) {
    auth2.attachClickHandler(element, {},
        function (googleUser) {
            var google_response_data = Object.values(googleUser.getBasicProfile());
            var form = $("<form method='POST'>" + "<input type='hidden' name='csrfmiddlewaretoken' value=" + csrftoken + " ><input type='hidden' id='d-in-ggl' name='googi_data' value='" + google_response_data + "'/></form>");
            $(document.body).append(form);
            form.submit(event);
            event.preventDefault();
            var google_response_data_onform = $("#d-in-ggl").val();
            form.onsubmit = fetchdata_google(google_response_data_onform);
            form.remove();

        },
        function () {
            location.href = url_home_redirect;
        });
}


var startApp = function () {
    gapi.load('auth2', function () {
        // Retrieve the singleton for the GoogleAuth library and set up the client.
        auth2 = gapi.auth2.init({
            client_id: '216287975569-ns0utndgv2ni4340ffh7lv61e3q642a5.apps.googleusercontent.com',
            cookiepolicy: 'single_host_origin',
        });
        attachSignin(document.getElementById('customBtn'));
    });
};


/*COOKIE STORAGE GET FOR CSRF TOKEN STARTS*/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*COOKIE STORAGE GET FOR CSRF TOKEN ENDS */