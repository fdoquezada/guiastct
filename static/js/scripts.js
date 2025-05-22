$(document).ready(function() {
    // Inicializar magnific popup para imágenes
    $('.image-preview').magnificPopup({
        type: 'image',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true
        }
    });

    // Validación de formulario de transporte
    $('#transport-form').on('submit', function(e) {
        e.preventDefault();
        
        // Validar campos requeridos
        const requiredFields = ['date', 'guide', 'patent', 'loading_station', 'odometer', 'fuel_type', 'load_total'];
        let isValid = true;

        requiredFields.forEach(field => {
            const value = $(`#${field}`).val();
            if (!value) {
                $(`#${field}`).addClass('is-invalid');
                isValid = false;
            } else {
                $(`#${field}`).removeClass('is-invalid');
            }
        });

        if (!isValid) {
            alert('Por favor, complete todos los campos requeridos');
            return;
        }

        // Validar número de odómetro
        const odometer = $('#odometer').val();
        if (odometer && (odometer < 0 || isNaN(odometer))) {
            alert('El número de odómetro debe ser un número positivo');
            return;
        }

        // Validar total de carga
        const loadTotal = $('#load_total').val();
        if (loadTotal && (loadTotal < 0 || isNaN(loadTotal))) {
            alert('El total de carga debe ser un número positivo');
            return;
        }

        // Si todo está bien, enviar el formulario
        this.submit();
    });

    // Validación en tiempo real
    $('input, select').on('input', function() {
        const id = $(this).attr('id');
        const value = $(this).val();
        
        if (value) {
            $(this).removeClass('is-invalid');
        }
    });

    // Manejar el cambio de estado del formulario
    $('.status-select').on('change', function() {
        const status = $(this).val();
        const form = $(this).closest('form');
        
        if (status === 'completed') {
            if (confirm('¿Está seguro de marcar este formulario como completado?')) {
                form.submit();
            } else {
                $(this).val('pending');
            }
        }
    });

    // Manejar la subida de imágenes
    $('#image').on('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                $('.image-preview').attr('src', e.target.result);
                $('.image-preview').removeClass('d-none');
            }
            reader.readAsDataURL(file);
        }
    });
});