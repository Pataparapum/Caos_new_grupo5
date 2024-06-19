$(document).ready(function () {
    
    if (sessionStorage.getItem('usuario')){
        var user = sessionStorage.getItem('usuario');
        if (user != null) {
            $('#boton').text(`${user}`);
            $('#boton').removeClass('btn-danger').addClass('btn-success')
            $('#sesion').attr('diseable');
        }
    }

    
    
    
});