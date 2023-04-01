(function () {

    let image_fields = $('form .form-row input[accept="image/*"]');
    //localStorage.setItem('test_admin_form_image_preivew', 1);
    if(localStorage.getItem('test_admin_form_image_preivew')){
        test_usability();
    }
    //localStorage.removeItem('test_admin_form_image_preivew');

    function test_usability(){
        let cnt = image_fields.length;
        if(!cnt){
            console.log('No file inputs with accept="image/*" were found in form.');
            return;
        }

        let subject = ' Image Preview => ';
        let message = 'You should see an image preview after changing any of '+cnt+' file input having accept="image/*"';
        if($('a.deletelink').length > 0){
            let upload_field_conrtainers = $('p.file-upload');
            let cnt1 = upload_field_conrtainers.length;
            let cnt2 = upload_field_conrtainers.find('a').length;
            if(cnt2 == cnt){
                console.log('Success:' + subject, 'edit mode');
            }
            else{
                let message1 = 'Preview only available for ';
                let message2 = '  file inputs having accept="image/*" enclosed by <p class="file-upload"> ';
                if(cnt1 == cnt){
                    message2 += ' and containing link (a) to image';
                    message = message1 + cnt2 + message;
                }
                else{
                    message = message1 + cnt1 + message;
                }
                console.log('Failure:' + subject, 'edit mode');
            }
        }
        else{
            console.log('Success:' + subject, 'create mode');
        }
        console.log(message);
    }

    image_fields.each((i, el) => {
        if (el.name.indexOf('__prefix__') > -1) { return; }
        el.onchange = readFileShowImage;
        let parent_obj = $(el).parent();
        let link_el = parent_obj.find('a');
        if(link_el.length) { link_el.attr('target', '_blank'); }
        let preview_container = parent_obj.find('.image-preview');
        if(!preview_container.length){
            parent_obj.append(`<div class="image-preview" style="padding-top:10px"></div>`);
            preview_container = parent_obj.find('.image-preview');
        }
        if(link_el.length){
            let link_href = link_el.attr('href');
            preview_container.html(`<a href="${link_href}" target="_blank"><img src="${link_href}" style="max-height:20vh;" /></div></a>`);
        }
        else{
            preview_container.html('');
        }
    });

    function readFileShowImage(ev) {
        let input = ev.target;
        let parent_obj = $(input).parent().find('.image-preview');
        console.log(input.files, input);
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (ev1) {
                parent_obj.html(`<img src="${ev1.target.result}" style="max-height:20vh;" /></div>`);
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            parent_obj.html('');
        }
    }
})();