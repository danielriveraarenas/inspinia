var index = function () {
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
            this.createAutosTable();
        },

        createAutosTable: function () {
            $('#autos').DataTable({
                ajax: {
                    url: "../crud/get_autos",
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "marca" },
                    { "data": "modelo" },
                    { "data": "precio" },
                    { "data": "colores" },
                    { "data": "descripcion" },
                    {
                        "data": "acciones",
                        "render": function (data, type, row, meta) {
                            return '<a class="btn btn-primary btn-sm" href="/crud/upd_auto/' + row.id + '" data-modal="">Actualizar</a><a class="btn btn-danger btn-sm" href="/crud/upd_auto/' + row.id + '" data-modal="">Eliminar</a>';
                        }
                    }
                ],
                initComplete: function (settings, json) {
                    Cpanel.init();
                }
            });
        }
    }
}();