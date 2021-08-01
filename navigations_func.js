const url_get_movies = "/getMovies/";
$(document).ready(function () {
    $(".opt").on("click", function (e) {
        $(this).addClass("active").not(this).removeClass("active");
    });
    // For get request to know and validate the token for PI authentication for getting all movies.
    $.ajaxSetup({
        headers: {
            'Authorization': $("#get").attr("datasrc")
        }
    });

    $("#get,#getfree").on("click", function (e) {
        e.preventDefault();
        $.get(url_get_movies, {}, function (response) {
            console.log(response.data);
            $(".datafree").css("background","white");
            $(".data, .datafree ").html("<code>" + JSON.stringify(response.data) + "</code>");
        });
    });

    $("#search").on("click", function (e) {
        e.preventDefault();
        var movie_search = $(".movie_search").val();
        $.get("/searchMovies/" + movie_search + "/", function (response) {
            console.log(response.data);
            $(".data").html("<code>" + JSON.stringify(response.data) + "</code>");
        });
    });
});

