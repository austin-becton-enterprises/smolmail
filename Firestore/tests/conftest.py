import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_firestore():
    with patch('core.firestore_service.firebase_admin') as mock_firebase, \
         patch('core.firestore_service.firestore') as mock_firestore:
        mock_db = MagicMock()
        mock_firestore.client.return_value = mock_db
        yield mock_db

@pytest.fixture
def client_service(mock_firestore):
    from core.services.client_service import ClientService
    return ClientService()

@pytest.fixture
def template_service(mock_firestore):
    from core.services.template_service import TemplateService
    return TemplateService()