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
            {'data': 'first_name'},
            {'data': 'username'},
            {'data': 'cargo'},
            {'data': 'groups__name'},
            {'data': 'email'},
            {'data': 'is_active'},
            {'data': 'id'}
        ],
        columnDefs: [
            {
                targets: [1, 2, 4],
                class: 'td-actions text-center'
            },
            {
                targets: [0],
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    return row['first_name'] + ' ' + row['last_name'];
                }
            },
            {
                targets: [3],
                class: 'td-actions text-center',
                render: function (data, type, row) {
                    return '<span class="badge badge-primary">' + row['groups__name'] + '</span>'
                }
            },
            {
                targets: [5],
                className: 'td-actions text-center',
                render: function (data, type, row) {
                    let estado = null;
                    switch (row['is_active']) {
                        case true:
                            estado = 'Activo'
                            break;
                        case false:
                            estado = 'Inactivo'
                            break;
                    }
                    return estado;
                }
            },
            {
                targets: [6],
                class: 'td-actions text-center',
                orderable: false,
                render: function (data, type, row) {
                    let actions
                    actions = '<a href="/user/detail/' + row['slug'] + '/" class="btn btn-round btn-info btn-icon btn-sm like"><i class="fas fa-info" title="Detalle Perfil"></i></a>&nbsp';
                    actions += '<a href="/user/update/' + row['slug'] + '/" class="btn btn-round btn-warning btn-icon btn-sm edit"><i class="far fa-edit" title="Editar"></i></a>&nbsp';
                    actions += '<a href="/user/update-password/' + row['slug'] + '/" class="btn btn-round btn-success btn-icon btn-sm edit"><i class="fas fa-key" title="Resetear Contraseña"></i></a>';
                    return actions
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});