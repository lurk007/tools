function check_login() {
    var login_name = document.getElementById('login_name').value;
    var password = document.getElementById('password').value;
    alert(login_name + password);
    return false
}

function ajax(url, param) {
    $.ajax({
        url: url,
        type: "POST",
        data: param,//{username: "Yuan", password: 123},
        success: function (data) {
            return data;
        },
        error: function (jqXHR, textStatus, err) {
            console.log(arguments);
        },

        complete: function (jqXHR, textStatus) {
            console.log(textStatus);
        },

        statusCode: {
            '403': function (jqXHR, textStatus, err) {
                console.log(arguments);
            },

            '400': function (jqXHR, textStatus, err) {
                console.log(arguments);
            }
        }
    })
}