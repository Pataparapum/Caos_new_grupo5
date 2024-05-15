$(document).ready(function () {
    
    if (localStorage.getItem('usuario')){
        var user = localStorage.getItem('usuario');
        if (user != null) {
            $('#sesion').text(`${user}`);
            $('#boton').removeClass('btn-danger').addClass('btn-success')
            $('#sesion').attr('disabled');
            $('#cerrarSesion').text("Log out...");
        }

        $('#cerrarSesion').click(function () {
            $('#sesion').text("Login");
            $('#boton').removeClass('btn-success').addClass('btn-danger');
            $('#sesion').removeAttr('disabled');
            $('#cerrarSesion').text("");
            localStorage.removeItem('usuario');
        })
    }

    
});