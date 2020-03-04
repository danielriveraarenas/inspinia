/* Global definitions
----------------------------------------------  */
var modalBs = $('#modalBs');
var modalBs2 = $('#modalBs2');

/* 01. Handles para operaciones ajax con modales bootstrap
---------------------------------------------  */
// Configura eventos y manejo de profundidades del modal principal y secundario
function handleModalConfig() {
    console.log("((handleModalConfig))");
    modalBs.on('hidden.bs.modal', function () {
        $(this).find(".modal-content").empty();
        $(this).find(".modal-dialog").removeClass("modal-lg");
        $(this).find(".modal-dialog").removeClass("modal-xl");
    });

    modalBs2.on('hidden.bs.modal', function () {
        $(this).find(".modal-content").empty();
        $(this).find(".modal-dialog").removeClass("modal-lg");
        $(this).find(".modal-dialog").removeClass("modal-xl");
    });
}

// Configura los objetos que tengan especificado la apertura del modal
function handleAjaxModal() {
    console.log("((handleAjaxModal))");
    // Limpia los eventos asociados para elementos ya existentes, asi evita duplicación
    $("a[data-modal]").unbind("click");
    $("a[data-modal2]").unbind("click");

    // Corrige bug presentado en Firefox que cierra los dropdownlist
    // automaticamente cuando tienen filtro en los modales - https://github.com/select2/select2/issues/1645#issuecomment-24296615
    $.fn.modal.Constructor.prototype._enforceFocus = function () { };

    // Evita cachear las transaccione Ajax previas
    $.ajaxSetup({ cache: false });

    var onClick = function (e) {
        var modalName = e.data;
        var currentModal = (modalName == "modal") ? modalBs :
            (modalName == "modal2") ? modalBs2 : null;
        var dataModalValue = $(this).data(modalName);
        var modalContent = currentModal.find(".modal-content");

        modalContent.load(this.href, function (response, status, xhr) {
            switch (status) {
                case "success":
                    currentModal.modal({ backdrop: 'static', keyboard: false }, 'show');
                    // Limpia el tipo de modal que exista previamente
                    currentModal.find(".modal-dialog").removeClass("modal-lg");
                    currentModal.find(".modal-dialog").removeClass("modal-xl");

                    // Especifica tamaño de modal
                    if (dataModalValue == "modal-lg") {
                        currentModal.find(".modal-dialog").addClass("modal-lg");
                    }
                    else if (dataModalValue == "modal-xl") {
                        currentModal.find(".modal-dialog").addClass("modal-xl");
                    }

                    // Inicializa el popup v1
                    try {
                        onModalInit();
                    } catch (ex) { }

                    // Configura links existentes en segundo modal
                    if (modalName != "modal2") {
                        handleAjaxModal();
                    }

                    break;

                case "error":
                    var message = "Error de ejecución: " + xhr.status + " " + xhr.statusText;
                    if (xhr.status == 403) $.msgbox(response, { type: 'error' });
                    else $.msgbox(message, { type: 'error' });
                    break;
            }
        });

        return false;
    }
    // Configura evento del link para aquellos para los que desean abrir modales
    $("a[data-modal]").bind("click", "modal", onClick);
    $("a[data-modal2]").bind("click", "modal2", onClick);
}

var Cpanel = function () {
    "use strict"
    return {
        init: function () {
            handleModalConfig();
            handleAjaxModal();
            this.enableAjaxCache();
        },

        // Se habilita cache para evitar la carga de los scripts adicionales desde los modales
        enableAjaxCache: function () {
            $.ajaxSetup({ cache: true });
        }
    };
}();