# tests/core/services/test_client_service.py
import pytest
from unittest.mock import MagicMock, patch, call

def test_register_client(client_service, mock_firestore):
    """Test the complete client registration flow with all input validations"""
    with patch('builtins.input', return_value='') as mock_input, \
         patch('core.services.client_service.input_non_empty') as mock_non_empty, \
         patch('core.services.client_service.is_valid_phone') as mock_valid_phone, \
         patch('core.services.client_service.is_valid_email') as mock_valid_email, \
         patch('utils.helpers.generate_unique_id', return_value='auto123') as mock_gen_id, \
         patch('builtins.print') as mock_print:
        
        # Configure input validation responses
        mock_valid_phone.side_effect = [False, True]  # First invalid, then valid
        mock_valid_email.side_effect = [False, True]   # First invalid, then valid
        
        # Configure input sequence
        mock_non_empty.side_effect = [
            'Test Client',      # Name
            '123 Main St',      # Address
            'invalid-phone',    # Phone (first attempt)
            '555-123-4567',     # Phone (second attempt)
            'bad-email',        # Email (first attempt)
            'test@example.com', # Email (second attempt)
            '12345'             # Zipcode
        ]
        
        # Mock Firestore responses
        mock_firestore.read_client.return_value = None  # Client doesn't exist
        
        # Execute
        client_service.register_client()
        
        # Verify input prompts
        mock_input.assert_called_once_with("Client ID (leave blank to auto-generate): ")
        
        # Verify validation messages
        assert call("Invalid phone number format.") in mock_print.call_args_list
        assert call("Invalid email format.") in mock_print.call_args_list
        
        # Verify Firestore call
        mock_firestore.create_client.assert_called_once_with(
            'auto123',
            {
                'client_name': 'Test Client',
                'client_address': '123 Main St',
                'client_phno': '555-123-4567',
                'client_email': 'test@example.com',
                'client_zipcode': '12345'
            }
        )

def test_list_clients(client_service, mock_firestore):
    """Test listing clients"""
    mock_doc = MagicMock()
    mock_doc.to_dict.return_value = {'client_id': 'test1', 'client_name': 'Test Client'}
    mock_firestore.list_clients.return_value = [mock_doc]
    
    clients = client_service.list_clients()
    assert len(clients) == 1
    assert clients[0]['client_name'] == 'Test Client'

def test_read_client(client_service, mock_firestore):
    """Test reading a single client"""
    mock_client = {'client_id': 'test1', 'client_name': 'Test Client'}
    mock_firestore.read_client.return_value = mock_client
    
    result = client_service.read_client('test1')
    assert result == mock_client

def test_update_client(client_service, mock_firestore):
    """Test client update"""
    updates = {'client_name': 'Updated Name'}
    client_service.update_client('test1', updates)
    mock_firestore.update_client.assert_called_once_with('test1', updates)

def test_delete_client(client_service, mock_firestore):
    """Test client deletion"""
    client_service.delete_client('test1')
    mock_firestore.delete_client.assert_called_once_with('test1')