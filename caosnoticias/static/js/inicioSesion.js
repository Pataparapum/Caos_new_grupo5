$(document).ready(function () {
    $('#form').submit(function () {
        var user = $('#user').val();
        if (user.length == 0) {
            $('#error').text('El usuario no puede estar vacio');
            event.preventDefault();
            $('#user').focus();

        } else if (user.length > 20) {
            $('#error').text('El nombre de usuario no puede tener mas de 20 letras');
            event.preventDefault();
            $('#user').focus();

        } else {
            var email = $('#email').val();
            if (email.length == 0) {
                $('#error').text('El email no puede estar vacio');
                event.preventDefault();
                $('#email').focus();

            } else {
                sessionStorage.setItem('usuario',user);
            }   

        }

    })
});