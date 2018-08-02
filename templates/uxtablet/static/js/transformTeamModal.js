/**
 * Created by Michaël on 29/10/2017.
 */

$(function(){
    var modal = $("#validationModal");
    var baseURL = '/ux/user/';
    var modalTitle = modal.find(".modal-title")[0];
    var modalLink= $('#validationModal div.modal-footer a');

    $(".company-link").click(
        function () {
            var user_id = $(this).find('input').attr('value');
            var companyName = $(this).find('.caption-text').find('p')[0].innerText.toLowerCase();
            modalLink.attr('href', baseURL + user_id + "/");
            modalTitle.innerText= "Hello ami de "+ companyName;
            $(".modal-title").css("text-transform", "capitalize");
        }
    );


});