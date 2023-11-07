$(document).ready(function() {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            id: {
                validators: {
                    stringLength: {
                        min: 2,
                        max: 30,
                        message: 'ID must be between 2 and 30 characters long'
                    },
                    notEmpty: {
                        message: 'Please supply your ID'
                    },
                    remote: {
                        url: '/check_id',
                        type: 'POST',
                        message: 'This ID is already in use',
                    }
                }
            },
             wifi: {
                validators: {
                    stringLength: {
                        max: 255,
                        message: 'Wifi password must be less than 255 characters long'
                    },
                }
            },
            address: {
                validators: {
                    stringLength: {
                        max: 255,
                        message: 'Address must be less than 255 characters long'
                    },
                }
            },
            hot_water_solution: {
                validators: {                    stringLength: {
                        max: 1000,
                        message: 'Address must be less than 1000 characters long'
                    },
                }
            },
            pool_price: {
                validators: {
                    stringLength: {
                        max: 255,
                        message: 'Price of the pool must be less than 255 characters long'
                    },
                    numeric: {
                        decimalSeparator: '.', // Imposta la virgola come separatore decimale
                        message: 'Price must be a number (use . as decimal separator)'
                    }
                }
            },
            breakfast: {
                validators: {
                    stringLength: {
                        max: 1000,
                        message: 'Address must be less than 1000 characters long'
                    },
                }
            }
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                $('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});