//The code in this file will deal withe the JavaScript on the create_table page 
$(document).ready(function() {

    var max_fields      = 6; //maximum input boxes allowed
    var wrapper         = $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID
    
    var x = 1; //initlal text box count

    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            content = '<div>' + 
                        '<input type="text" name="mytext' + x + 
            '"/><a href="#" class="remove_field">Remove</a></div>'
            $(wrapper).append(content);

        }
    });
    
    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
    
});


