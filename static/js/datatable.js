$(document).ready(function () {
    $("#example").DataTable({
      language: {
        decimal: "",
        emptyTable: "No hay información",
        info: "Mostrando START a END de TOTAL Entradas",
        infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
        infoFiltered: "(Filtrado de MAX total entradas)",
        infoPostFix: "",
        thousands: ",",
        lengthMenu: "Mostrar MENU Entradas",
        loadingRecords: "Cargando...",
        processing: "Procesando...",
        search: "Buscar:",
        zeroRecords: "Sin resultados encontrados",
        paginate: {
          first: "Primero",
          last: "Ultimo",
          next: "Siguiente",
          previous: "Anterior",
        },
      },
    });
  });