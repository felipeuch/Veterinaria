jQuery.extend(jQuery.validator.messages, {
    required: "Este campo es obligatorio.",
    remote: "Por favor, rellena este campo.",
    email: "Por favor, escribe una dirección de correo válida",
    url: "Por favor, escribe una URL válida.",
    date: "Por favor, escribe una fecha válida.",
    dateISO: "Por favor, escribe una fecha (ISO) válida.",
    number: "Por favor, escribe un número entero válido.",
    digits: "Por favor, escribe sólo dígitos.",
    creditcard: "Por favor, escribe un número de tarjeta válido.",
    equalTo: "Por favor, escribe el mismo valor de nuevo.",
    accept: "Por favor, escribe un valor con una extensión aceptada.",
    maxlength: jQuery.validator.format("Por favor, no escribas más de {0} caracteres."),
    minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
    rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
    range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
    max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
    min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
});

var validator = $("#formularioRaza").validate({
    rules: {
        txtNombre_mascota: {
            required: true,
            minlength: 3,
            maxlength: 80
        },
         txtTipoMascota: {
            required: true,
            minlength: 10,
            maxlength: 100
        },
        txtRaza: {
            required: true,
            minlength: 10,
            maxlength: 200
        },

        txtDescripcion: {
            required: false,
            minlength: 10,
            maxlength: 200
        },

        txtColor_principal: {
            required: true,
            minlength: 10,
            maxlength: 30
        },

        txtPeso:{
            required: true,
            number: true,
            min: 1,
            max: 500
        },

        fl_imagen: {
            required: false
        }


    },
    messages: {
        txtNombre_mascota: {
            minlength: "Este campo debe tener al menos 3 caracteres"
        },
        txtMensaje: {
            minlength: "este campo debe tener almenos 10 caracteres"
        }
    }
});

$("#btnEnviar").click(function(){
    if(validator.form()){
        alert("Datos enviados");
    }
})