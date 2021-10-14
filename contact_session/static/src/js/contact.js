odoo.define("contacts", function (require) {
    "use strict";

    $(document).ready(function(){

//        FOR MAKING THE LIST ROW CLICKABLE
        $(".contact_list_tbl").on('click', '.contact_row', function(e){
            let href = $(this).attr("data-href");
            window.location.href = href;
        });

//        CHECKING THE TEAM LEAD CHECKBOX
        $("#team_lead").on('change', function(e){
            if ($(this).is(":checked"))
            {
                $('.partner_team_details_wrapper').removeClass("d-none");
            }
            else
            {
                $('.partner_team_details_wrapper').addClass("d-none");
            }
        });

//      FOR CHANGING IMAGE WHEN THE INPUT IS GIVEN
        $("#partner_image_input").on('change', function(e){
            var partner_img = $('#partner_image');
            var default_image = "/contact_session/static/src/img/placeholder.png";
            var input = this
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    partner_img.attr("src", e.target.result)
                };
                reader.readAsDataURL(input.files[0]);
            }
            else
            {
                var partner_id = $("#partner_id").val()
                if (partner_id)
                {
                    default_image = "/web/image/res.partner/"+partner_id+"/image_1920"
                }

                partner_img.attr("src", default_image)
            }
        });

//      FOR SEARCHING IN THE CONTACT LIST
        $("#filter_table").on("keypress", function(e) {
            console.log("e.keyCode----", e.keyCode)
            if (e.keyCode == 13 || e.keyCode == 8)
            {
                var value = $(this).val().toLowerCase();
                $(".contact_list_tbl tbody tr").filter(function() {
                    $(this).toggle($(this).find(".contact_name_col").text().toLowerCase().indexOf(value) > -1)
                });
            }
        });

    });

});
