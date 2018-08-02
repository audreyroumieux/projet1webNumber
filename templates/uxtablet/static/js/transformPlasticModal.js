/**
 * Created by Michaël on 29/10/2017.
 */

$(function(){
    var modal = $("#validationModal");
    var baseURL = '/ux/user/';
    var modalBody = modal.find(".modal-body").find('p')[0];

    $(".plastic-link").click(
        function () {
            var apiURL = $(this).find('input')[3].value;
            var hiddenInput = $(this).find('input')[0];
            var hiddenInputPlaticPoints = $(this).find('input')[1];
            var hiddenInputScore = $(this).find('input')[2];
            var hiddenInputPlasticId = $(this).find('input')[4];

            var plasticPoints = hiddenInputPlaticPoints.value;
            var userScore = hiddenInputScore.value;
            var user_id = hiddenInput.value;
            var plastic_id = hiddenInputPlasticId.value;
            var updateScoreUrl = apiURL+ 'companies/' + user_id + '/update_score/';
            console.log("plastic_id :" + plastic_id);
            console.log(updateScoreUrl);
            var score = parseInt(userScore) + parseInt(plasticPoints);
            console.log(score);
            var data = {"score" : score};
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
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
            $.ajax({
                type: "POST",
                async: true,
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                authorization : "Basic " + btoa("admin:password123"),
                cache: false,
                url: updateScoreUrl,
                data: data
            }).done(function(response){console.log(response)});
            $('.modal-footer a')[0].href= baseURL +user_id+ "/"+ plastic_id + "/your_waste";
            console.log(modal.attr('href'));
            modalBody.innerText= "Yeah, tu viens de gagner "+ plasticPoints +" paillettes !";
        }
    );


});