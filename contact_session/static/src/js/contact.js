odoo.define("contacts", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');

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
            console.log("this------", this)
            console.log("$(this)------", $(this))
            var partner_img = $('#partner_image');
            var default_image = "/contact_session/static/src/img/placeholder.png";
            var input = this
            if (input.files && input.files[0]) {
                $("#delete_image").val("False");
                var reader = new FileReader();
                reader.onload = function (e) {
                    partner_img.attr("src", e.target.result)
                };
                reader.readAsDataURL(input.files[0]);
            }
            else
            {
                if ($("#delete_image").val() == "False")
                {
                    console.log("hello")
                    var partner_id = $("#partner_id").val()
                    if (partner_id)
                    {
                        default_image = "/web/image/res.partner/" + partner_id + "/image_1920";
                    }
                }
                partner_img.attr("src", default_image)
            }
        });

        $(".delete_image").on('click', function(e){
            $("#partner_image_input").val("");
            $("#delete_image").val("True");
            $("#partner_image_input").trigger("change");
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

        $("#country_id").on("change", function(e) {
            $('#contact_form_submit_btn').attr("disabled", "disabled");
            let state_ele = $('#state_id');
            let selected_state = state_ele.val();
            let element = $(this)
            let country_id = element.val();
            ajax.jsonRpc('/get/filtered/states', 'call', {'country_id': country_id}).then(function(data) {
                console.log(data)
                if (data['status'])
                {
                    let markup = ""
                    markup += "<option value=''>Select State</option>"
                    $.each(data['states'], function(){
                        if (selected_state == this['id'])
                        {
                            markup += "<option value='"+this['id']+"' selected='selected'>"+this['name']+"</option>"
                        }
                        else
                        {
                            markup += "<option value='"+this['id']+"'>"+this['name']+"</option>"
                        }
                    });

                    state_ele.empty().append(markup);
                    $('#contact_form_submit_btn').attr("disabled", false);
                }
                else
                {
                    $('#contact_form_submit_btn').attr("disabled", false);
                    ajax.jsonRpc('/get/error/dialog', 'call', {'error': data['error']}).then(function(modal) {
                        var $modal = $(modal)
                        $modal.modal('show')

                        $modal.on('hidden.bs.modal', function (e) {
                            $modal.modal('dispose');
                        });

                    });

                }
                
            });
        });

        console.log('starting')
        rpc.query({
            route: '/get/filtered/states',
            params: {'country_id': 104},

        }).then(function (data) {
            console.log("-----------", data)
            console.log('ends')
        });

    });

});
