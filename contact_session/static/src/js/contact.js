odoo.define("contacts", function (require) {
    "use strict";

    $(document).ready(function(){
        $(".contact_list_tbl").on('click', '.contact_row', function(e){
            let href = $(this).attr("data-href");
            window.location.href = href;
        });

    });

});
