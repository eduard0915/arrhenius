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
            {'data': 'zone_condition'},
            {'data': 'description_condition'},
            {'data': 'study_type'},
            {'data': 'temperture_sup'},
            {'data': 'percent_humidity_sup'},
            {'data': 'period_minimum_time'},
            {'data': 'condition_enabled'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3, 4, 5],
                class: 'text-center'
            },
            {
                targets: [3],
                render: function (data, type, row) {
                    return row['temperture_inf'] + ' / ' + row['temperture_sup'] + '°C';
                }
            },
            {
                targets: [4],
                render: function (data, type, row) {
                    return row['percent_humidity_inf'] + ' / ' + row['percent_humidity_sup'] + '%';
                }
            },
            {
                targets: [6],
                class: 'text-center',
                render: function (data, type, row) {
                    if (row['condition_enabled']) {
                        return '<span class="badge badge-success">Activo</span>';
                    }
                    return '<span class="badge badge-danger">Inactivo</span>';
                }
            },
            {
                targets: [7],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/condition/detail/' + row['id'] + '/" class="btn btn-round btn-info btn-sm btn-icon"><i class="now-ui-icons business_badge"></i></a>&nbsp;';
                    buttons += '<a href="/condition/update/' + row['id'] + '/" class="btn btn-round btn-warning btn-sm btn-icon"><i class="now-ui-icons ui-2_settings-90"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});
