import pytest
from unittest.mock import MagicMock, patch

def test_login(template_service, mock_firestore):
    mock_doc = MagicMock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {'client_id': 'test1'}
    mock_firestore.collection.return_value.document.return_value.get.return_value = mock_doc
    
    assert template_service.login('test1') is True
    assert template_service.logged_in_client_id == 'test1'

def test_create_template(template_service, mock_firestore):
    template_service.logged_in_client_id = 'test1'
    
    with patch('core.services.template_service.input', return_value=''), \
         patch('core.services.template_service.input_non_empty', side_effect=[
             'Test Template', 'Hello {name}!'
         ]), \
         patch('utils.helpers.generate_unique_id', return_value='tpl123'):
        
        template_service.create_template()
        mock_firestore.collection.assert_called_with('templates')

def test_render_template(template_service, mock_firestore):
    template_service.logged_in_client_id = 'test1'
    
    mock_template_doc = MagicMock()
    mock_template_doc.exists = True
    mock_template_doc.to_dict.return_value = {
        'template_code': 'Hello {client_name}!',
        'client_id': 'test1'
    }
    
    mock_client_doc = MagicMock()
    mock_client_doc.exists = True
    mock_client_doc.to_dict.return_value = {
        'client_name': 'Test Client'
    }
    
    mock_firestore.collection.side_effect = lambda name: {
        'templates': MagicMock(document=MagicMock(return_value=MagicMock(get=MagicMock(return_value=mock_template_doc)))),
        'contacts': MagicMock(document=MagicMock(return_value=MagicMock(get=MagicMock(return_value=mock_client_doc))))
    }[name]
    
    with patch('builtins.print') as mock_print:
        template_service.render_template('tpl123')
        mock_print.assert_called_with('\n--- Rendered Template ---\nHello Test Client!\n-------------------------')

def test_log_email(template_service, mock_firestore):
    template_service.logged_in_client_id = 'test1'
    template_service.fs.logged_in_client_id = 'test1'
    
    email_id = template_service.log_email('tpl123', {'opened': True})
    mock_firestore.collection.assert_called_with('emails')