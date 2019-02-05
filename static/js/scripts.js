$(document).ready(function () {
    var elements = document.querySelectorAll('input[type=number]');
    var price = 0;
    var order_list = '';

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
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

    function getURLParameter(name) {
        return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
    }

    function update_table() {
        for (var i = 0; i < elements.length; i++) {
            if (elements[i].value > 0) {
                elements[i].value = '';
            }
        }
    }
    $("input[type=number]").keypress(function(event) {
        if (event.which != 8 && event.which != 0 && event.which != 46 && (event.which < 48 || event.which > 57) && event.which != 43) {
            return false;
        }
    });

    $('#complete_order').on('click', function(){
        var show = false;
        price = 0;
        for (var i = 0; i < elements.length; i++) {
            if (elements[i].value > 0) {
                price += elements[i].value * elements[i].getAttribute('data-price');
                show = true;
                order_list += elements[i].getAttribute('data-prod') + '-' + elements[i].value + ' ';
            }
        }
        if(show){
            $("#order_price").val(price);
            $("#orderModal").modal('show');
        }
        else{
            alert('Выберите начинку для пиццы');
        }
    });

    $("#order").on('click', function (event) {
        event.preventDefault();

        var form = $('#createOrderForm')[0];
        var data = new FormData(form);
        data.append('email', $("#email").val());
        data.append('telephone', $("#telephone").val());
        data.append('name', $("#name").val());
        data.append('price', $("#order_price").val());
        data.append('order', order_list);
        $.ajax({
            url: links.create_order,
            type: 'POST',
            data: data,
            dataType: "json",
            processData: false,
            contentType: false,
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            },
            success: function (data) {
                alert(data['Message']);
                location.reload();
                update_table();
            }
        });
    });

});


