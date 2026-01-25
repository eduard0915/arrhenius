from core.protocol.models import Protocol


def protocol_list_selector():
    return Protocol.objects.all().order_by('code_protocol', '-version')


def protocol_detail_selector(protocol_id):
    return Protocol.objects.filter(id=protocol_id).first()
