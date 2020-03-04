var ins_auto = function () {
    "use strict"
    return {
        // ---------------------------------
        //           Propiedades 
        // ---------------------------------
        //..	


        // ---------------------------------
        //           Metodos 
        // ---------------------------------

        init: function () {
            this.manageMarcas();
            this.manageModelos();
            this.manageColores();
            this.onSubmit();
        },

        manageMarcas: function () {
            $('[name=marcas_id]').select2({
                dropdownParent: $("#modalBs .modal-content"),
                theme: 'bootstrap4',
                ajax: {
                    url: "../crud/get_marcas",
                    dataType: 'json',
                    data: function (params) {
                        return {
                            search: params.term
                        }
                    },
                    processResults: function (data) {
                        return { results: data };
                    }
                }
            });
            $('[name=marcas_id]').on('select2:select', function (e) {
                $('[name=modelo_id]').val(null).trigger('change');
                $('[name=modelo_id]').prop("disabled", false);
            });
        },

        manageModelos: function () {
            $('[name=modelo_id]').select2({
                dropdownParent: $("#modalBs .modal-content"),
                theme: 'bootstrap4',
                ajax: {
                    url: "../crud/get_modelos",
                    dataType: 'json',
                    data: function (params) {
                        return {
                            marca: parseInt($("[name=marcas_id] option:selected").val()),
                            search: params.term
                        }
                    },
                    processResults: function (data) {
                        return { results: data };
                    }
                }
            });
            $('[name=modelo_id]').prop("disabled", true);
        },

        manageColores: function () {
            $('[name=colores]').select2({
                dropdownParent: $("#modalBs .modal-content"),
                theme: 'bootstrap4',
                ajax: {
                    url: "../crud/get_colores",
                    dataType: 'json',
                    data: function (params) {
                        return {
                            search: params.term
                        }
                    },
                    processResults: function (data) {
                        return { results: data };
                    }
                }
            });
        },

        onSubmit: function (result) {
            $(document).on('submit', '#form0', function (e) {
                e.preventDefault();
                $.ajax({
                    type: $(this).attr('method'),
                    url: $(this).attr('action'),
                    data: $(this).serialize(),
                    success: function (json) {
                        $('#modalBs').modal('hide');
                        $('#autos').DataTable().ajax.reload();
                    },
                    error: function (xhr, errmsg, err) {
                        console.log(xhr.status + ": " + xhr.responseText);
                    }
                });
            });
        }
    }
}();