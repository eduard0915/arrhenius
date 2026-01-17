$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json"
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {'data': 'code_product'},
            {'data': 'description_product'},
            {'data': 'pharma_form'},
            {'data': 'brand_product'},
            {'data': 'product_enabled'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3],
                class: 'text-center'
            },
            {
                targets: [2],
                render: function (data, type, row) {
                    return data ? data : '';
                }
            },
            {
                targets: [3],
                render: function (data, type, row) {
                    return data ? data : 'No aplica';
                }
            },
            {
                targets: [4],
                class: 'text-center',
                render: function (data, type, row) {
                    if (row['product_enabled']) {
                        return '<span class="badge badge-success">Activo</span>';
                    }
                    return '<span class="badge badge-danger">Inactivo</span>';
                }
            },
            {
                targets: [5],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/product/detail/' + row['id'] + '/" class="btn btn-info btn-sm btn-icon"><i class="now-ui-icons business_badge"></i></a>&nbsp;';
                    buttons += '<a href="/product/update/' + row['id'] + '/" class="btn btn-warning btn-sm btn-icon"><i class="now-ui-icons ui-2_settings-90"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});
