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
            {'data': 'code_protocol'},
            {'data': 'study_type'},
            {'data': 'condition'},
            {'data': 'prepared_by'},
            {'data': 'date_prepared'},
            {'data': 'enabled_protocol'},
            {'data': 'version'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3, 4, 5, 6, 7],
                class: 'text-center'
            },
            {
                targets: [5],
                render: function (data, type, row) {
                    if (row['enabled_protocol']) {
                        return '<span class="badge badge-success">Habilitado</span>';
                    }
                    return '<span class="badge badge-danger">Inhabilitado</span>';
                }
            },
            {
                targets: [7],
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/protocol/detail/' + row['id'] + '/" class="btn btn-round btn-info btn-sm btn-icon"><i class="now-ui-icons business_badge"></i></a>&nbsp;';
                    buttons += '<a href="/protocol/update/' + row['id'] + '/" class="btn btn-round btn-warning btn-sm btn-icon"><i class="now-ui-icons ui-2_settings-90"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});
