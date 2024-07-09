$(document).ready(function() {
    $('form').submit(function(event) {
        let formIsValid = true;
        $('.form-control').each(function() {
            let isValid = true; // Variable para controlar la validación específica de cada campo
            let value = $(this).val().trim(); // Obtener el valor del campo y eliminar espacios en blanco
  
            // Verificar la validez básica y condiciones específicas
            if (!this.checkValidity() || !isValidInput($(this), value)) {
                $(this).addClass('is-invalid');
                $(this).css('border', '2px solid red');
                formIsValid = false;
            } else {
                $(this).removeClass('is-invalid').addClass('is-valid');
                $(this).css('border', '');
            }
        });
  
        if (!formIsValid) {
            event.preventDefault();
        }
    });
  // aqui la clase css para las validaciones
    $('.form-control').on('input', function() {
        let value = $(this).val().trim();
        if (this.checkValidity() && isValidInput($(this), value)) {
            $(this).removeClass('is-invalid').addClass('is-valid');
            $(this).css('border', '');
        } else {
            $(this).removeClass('is-valid').addClass('is-invalid');
            $(this).css('border', '2px solid red');
        }
    });
  
    // Función para validar los campos con condiciones específicas
    function isValidInput(element, value) {
        let id = element.attr('id');
        switch (id) {
            case 'nombreInput':
            case 'apellidoInput':
                return value.length >= 2;
            case 'paisInput':
              case 'ciudadInput':
                return value.length >= 3;
            case 'emailInput':
                return /^[^@]+@[^@]+\.[^@]+$/.test(value); // validar el email
            case 'mensajeInput':
                return value.length >= 10;
            default:
                return true; // Si no hay condiciones específicas, se considera válido
        }
    }
  });