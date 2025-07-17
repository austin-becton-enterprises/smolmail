# -----------------------------------------------------------------------------
# Copyright (c) 2025 SmolMail Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This project is open-source and maintained by the community.
# Contributions are welcome—please see the CONTRIBUTING.md file for guidelines.
#
# "SmolMail" and the SmolMail logo are trademarks of SmolMail, Inc.
# Use of these trademarks is subject to SmolMail's trademark policy.
#
# Created by Austin Becton
# -----------------------------------------------------------------------------


import pytest
from unittest.mock import MagicMock, patch, call

@pytest.fixture
def mock_fs():
    """Mock FirestoreService used by ClientService."""
    with patch('core.services.client_service.FirestoreService') as MockFS:
        mock = MagicMock()
        MockFS.return_value = mock
        yield mock


@pytest.fixture
def client_service(mock_fs):
    from core.services.client_service import ClientService
    return ClientService()


def test_register_client(client_service, mock_fs):
    with patch('core.services.client_service.input', side_effect=['']), \
         patch('core.services.client_service.input_non_empty') as mock_non_empty, \
         patch('core.services.client_service.is_valid_phone') as mock_valid_phone, \
         patch('core.services.client_service.is_valid_email') as mock_valid_email, \
         patch('core.services.client_service.generate_unique_id', return_value='auto123'), \
         patch('builtins.print') as mock_print:

        mock_fs.read_client.return_value = None

        mock_valid_phone.side_effect = [False, True]
        mock_valid_email.side_effect = [False, True]

        mock_non_empty.side_effect = [
            'Test Client',
            '123 Main St',
            'invalid-phone',
            '555-123-4567',
            'bad-email',
            'test@example.com',
            '12345'
        ]

        client_service.register_client()

        assert call("Invalid phone number format.") in mock_print.call_args_list
        assert call("Invalid email format.") in mock_print.call_args_list

        mock_fs.create_client.assert_called_once_with(
            'auto123',
            {
                'client_name': 'Test Client',
                'client_address': '123 Main St',
                'client_phno': '555-123-4567',
                'client_email': 'test@example.com',
                'client_zipcode': '12345'
            }
        )


def test_list_clients(client_service, mock_fs):
    mock_doc = MagicMock()
    mock_doc.to_dict.return_value = {'client_id': 'test1', 'client_name': 'Test Client'}
    mock_fs.list_clients.return_value = [mock_doc]

    clients = client_service.list_clients()
    assert len(clients) == 1
    assert clients[0]['client_name'] == 'Test Client'


def test_read_client(client_service, mock_fs):
    mock_client = {'client_id': 'test1', 'client_name': 'Test Client'}
    mock_fs.read_client.return_value = mock_client

    result = client_service.read_client('test1')
    assert result == mock_client


def test_update_client(client_service, mock_fs):
    updates = {'client_name': 'Updated Name'}
    client_service.update_client('test1', updates)
    mock_fs.update_client.assert_called_once_with('test1', updates)


def test_delete_client(client_service, mock_fs):
    client_service.delete_client('test1')
    mock_fs.delete_client.assert_called_once_with('test1')
