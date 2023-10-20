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
                        message: 'ID must be at least 2 characters long'
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
             floor: {
                validators: {
                }
            },
            hot_water: {
                validators: {
                }
            },
            parking: {
                validators: {
                }
            },
            air_conditioning: {
                validators: {
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