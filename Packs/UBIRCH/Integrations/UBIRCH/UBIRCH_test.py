import io
from UBIRCH import get_incident_type, get_severity, create_incidents, AUTHENTICATION_TYPE, LOW_SEVERITY, HIGH_SEVERITY,\
    UNKNOWN_SEVERITY


def util_load_json(path: str) -> str:
    with io.open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def test_get_incident_type() -> None:
    """Test get_incident_type function.

    Checks the incident type is the expected one.

    No mock is needed here.
    """
    authentication_incident = {
        "error": "Authentication Error: Missing header/param"
    }
    unclassified_incident = {
        "error": "Unknown"
    }

    assert get_incident_type(authentication_incident) == AUTHENTICATION_TYPE
    assert get_incident_type(unclassified_incident) == ''


def test_get_severity() -> None:
    """Test get_severity function.

    Checks the severity is the expected one.

    No mock is needed here.
    """
    incident_auth_1000 = {
        "errorCode": "1000",
        "microservice": "niomon-auth"
    }
    incident_decoder_1300 = {
        "errorCode": "1300",
        "microservice": "niomon-decoder"
    }
    incident_enricher_0000 = {
        "errorCode": "0000",
        "microservice": "niomon-enricher"
    }
    incident_filter_0000 = {
        "errorCode": "0000",
        "microservice": "filter-service"
    }
    incident_unknown1 = {}
    incident_unknown2 = {
        "errorCode": "1000",
        "microservice": "niomon"
    }
    incident_unknown3 = {
        "errorCode": "5000",
        "microservice": "niomon-auth"
    }

    assert get_severity(incident_auth_1000) == LOW_SEVERITY
    assert get_severity(incident_decoder_1300) == HIGH_SEVERITY
    assert get_severity(incident_enricher_0000) == HIGH_SEVERITY
    assert get_severity(incident_filter_0000) == HIGH_SEVERITY
    assert get_severity(incident_unknown1) == UNKNOWN_SEVERITY
    assert get_severity(incident_unknown2) == UNKNOWN_SEVERITY
    assert get_severity(incident_unknown3) == UNKNOWN_SEVERITY


def test_create_incidents() -> None:
    """Test create_incidents function.

    Checks the incidents is the expected one.

    No mock is needed here.
    """
    ERROR_MESSAGE = util_load_json('test_data/raw_json_error_message.json')
    incidents = create_incidents(ERROR_MESSAGE)
    assert incidents == INCIDENT_RESPONSE


INCIDENT_RESPONSE = [{
    'name': "SignatureException: Invalid signature",
    'type': "",
    'labels': [
        {'type': "requestId", 'value': "ec15d266-5822-4fa5-ba82-64f1653d46a4"},
        {'type': "hwDeviceId", 'value': "ba70ad8b-a564-4e58-9a3b-224ac0f0153f"}
    ],
    'rawJSON': '{"requestId": "ec15d266-5822-4fa5-ba82-64f1653d46a4", "hwDeviceId": '
               '"ba70ad8b-a564-4e58-9a3b-224ac0f0153f", "errorCode": "1300", "error": "SignatureException: Invalid '
               'signature", "microservice": "niomon-decoder", "timestamp": "2021-01-07T18:47:52.025Z"}',
    'details': '{"requestId": "ec15d266-5822-4fa5-ba82-64f1653d46a4", "hwDeviceId": '
               '"ba70ad8b-a564-4e58-9a3b-224ac0f0153f", "errorCode": "1300", "error": "SignatureException: Invalid '
               'signature", "microservice": "niomon-decoder", "timestamp": "2021-01-07T18:47:52.025Z"}',
    'severity': HIGH_SEVERITY
}]
