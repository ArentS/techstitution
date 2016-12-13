 $(document).ready(function () {
     $('#reg_form').bootstrapValidator({
         // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
         feedbackIcons: {
             valid: 'glyphicon glyphicon-ok'
             , invalid: 'glyphicon glyphicon-remove'
             , validating: 'glyphicon glyphicon-refresh'
         }
         , fields: {
             emri_nder: {
                 validators: {
                     regexp: {
                         regexp: /^[a-z\s]+$/i
                         , message: 'Emri duhet te permbaje shkronja dhe hapesira!'
                     }
                     , stringLength: {
                         min: 5
                         , message: 'Min 5 karaktere'
                     }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani merin e nderrmarrjes'
                     }
                 }
             }
             , nr_biz: {
                 validators: {
                     between: {
                         min: 0
                         , max: 999999999999
                         , message: 'Ju lutem, shkruani sakte nr e biznesit'
                     }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani nr e biznesit'
                     }
                 }
             }
             , nr_fiskal: {
                 validators: {
                     between: {
                         min: 0
                         , max: 999999999999
                         , message: 'Ju lutem, shkruani sakte nr e biznesit'
                     }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani nr e biznesit'
                     }
                 }
             }
             , adresa: {
                 validators: {
                     stringLength: {
                         min: 8
                     , }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani adresen'
                     }
                 }
             }
             , nr_tel: {
                 validators: {
                     notEmpty: {
                         message: 'Ju lutem, shkruani nr e telefonit'
                     }
                     , regexp: {
                         message: 'Nr telefonit duhet te permbaje vetem numra, hapesira, -, (, ), + dhe .'
                         , regexp: /^[0-9\s\-()+\.]+$/
                     }
                 }
             }
             , nr_fax: {
                 validators: {
                     notEmpty: {
                         message: 'Ju lutem, shkruani nr e fax-it'
                     }
                     , regexp: {
                         message: 'Nr fax-it duhet te permbaje vetem numra, hapesira, -, (, ), + dhe .'
                         , regexp: /^[0-9\s\-()+\.]+$/
                     }
                 }
             }
             , email: {
                 validators: {
                     notEmpty: {
                         message: 'Ju lutem, shkruani email-in'
                     }
                     , emailAddress: {
                         message: 'Ju lutem, shkruani email-in e sakte'
                     }
                 }
             }
             , emri_zyrtarit: {
                 validators: {
                     regexp: {
                         regexp: /^[a-z\s]+$/i
                         , message: 'Emri duhet te permbaje shkronja dhe hapesira!'
                     }
                     , stringLength: {
                         min: 5
                         , message: 'Min 5 karaktere'
                     }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani merin e nderrmarrjes'
                     }
                 }
             }
             , adresa_zyrtarit: {
                 validators: {
                     stringLength: {
                         min: 8
                     , }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani adresen'
                     }
                 }
             }
             , nr_tel_zyrtarit: {
                 validators: {
                     notEmpty: {
                         message: 'Ju lutem, shkruani nr e telefonit'
                     }
                     , regexp: {
                         message: 'Nr telefonit duhet te permbaje vetem numra, hapesira, -, (, ), + dhe .'
                         , regexp: /^[0-9\s\-()+\.]+$/
                     }
                 }
             }
             , nr_fax_zyrtarit: {
                 validators: {
                     notEmpty: {
                         message: 'Ju lutem, shkruani nr e fax-it'
                     }
                     , regexp: {
                         message: 'Nr fax-it duhet te permbaje vetem numra, hapesira, -, (, ), + dhe .'
                         , regexp: /^[0-9\s\-()+\.]+$/
                     }
                 }
             }
             , email_zyrtarit: {
                 validators: {
                     notEmpty: {
                         message: 'Ju lutem, shkruani email-in'
                     }
                     , emailAddress: {
                         message: 'Ju lutem, shkruani email-in e sakte'
                     }
                 }
             }
             , nr_id: {
                 validators: {
                     between: {
                         min: 1000000000
                         , max: 9999999999
                         , message: 'Ju lutem, shkruani sakte nr e biznesit'
                     }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani nr e biznesit'
                     }
                 }
             }
             , about_you: {
                 validators: {
                     stringLength: {
                         min: 8
                     , }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani adresen'
                     }
                 }
             }
         , about_you2: {
                 validators: {
                     stringLength: {
                         min: 8
                     , }
                     , notEmpty: {
                         message: 'Ju lutem, shkruani adresen'
                     }
                 }
             }
         ,cer_biznesit: {
                validators: {
                    notEmpty: {
                        message: 'Please select an image'
                    },
                    file: {
                        extension: 'jpeg,jpg,png',
                        type: 'image/jpeg,image/png',
                        maxSize: 2097152,   // 2048 * 1024
                        message: 'The selected file is not valid'
                    }
                }
            },cert_fiskal: {
                validators: {
                    notEmpty: {
                        message: 'Please select an image'
                    },
                    file: {
                        extension: 'jpeg,jpg,png',
                        type: 'image/jpeg,image/png',
                        maxSize: 2097152,   // 2048 * 1024
                        message: 'The selected file is not valid'
                    }
                }
            },info_biz: {
                validators: {
                    notEmpty: {
                        message: 'Please select an image'
                    },
                    file: {
                        extension: 'jpeg,jpg,png',
                        type: 'image/jpeg,image/png',
                        maxSize: 2097152,   // 2048 * 1024
                        message: 'The selected file is not valid'
                    }
                }
            },}
     }).on('success.form.bv', function (e) {
         $('#success_message').slideDown({
                 opacity: "show"
             }, "slow") // Do something ...
         $('#reg_form').data('bootstrapValidator').resetForm();
         // Prevent form submission
         e.preventDefault();
         // Get the form instance
         var $form = $(e.target);
         // Get the BootstrapValidator instance
         var bv = $form.data('bootstrapValidator');
         // Use Ajax to submit form data
         $.post($form.attr('action'), $form.serialize(), function (result) {
             console.log(result);
         }, 'json');
     });
 });