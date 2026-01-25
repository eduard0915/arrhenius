from core.protocol.models import Protocol


def protocol_create_service(*, code_protocol, study_type, condition, objective, numbers_batch, prepared_by, date_prepared, approved_by, date_approved, enabled_protocol=True, version=1):
    protocol = Protocol(
        code_protocol=code_protocol,
        study_type=study_type,
        condition=condition,
        objective=objective,
        numbers_batch=numbers_batch,
        prepared_by=prepared_by,
        date_prepared=date_prepared,
        approved_by=approved_by,
        date_approved=date_approved,
        enabled_protocol=enabled_protocol,
        version=version
    )
    protocol.full_clean()
    protocol.save()
    return protocol


def protocol_update_service(protocol, **data):
    for key, value in data.items():
        setattr(protocol, key, value)
    
    protocol.full_clean()
    protocol.save()
    return protocol


def protocol_delete_service(protocol):
    protocol.delete()
