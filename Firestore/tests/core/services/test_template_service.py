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
from unittest.mock import MagicMock, patch, ANY

def test_login(template_service, mock_firestore):
    mock_doc = MagicMock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {'client_id': 'test1'}
    mock_firestore.collection.return_value.document.return_value.get.return_value = mock_doc

    assert template_service.login('test1') is True
    assert template_service.logged_in_client_id == 'test1'
    assert template_service.fs.logged_in_client_id == 'test1'


def test_create_template(template_service, mock_firestore):
    template_service.logged_in_client_id = 'test1'
    template_service.fs.logged_in_client_id = 'test1'

    with patch('core.services.template_service.input', return_value=''), \
         patch('core.services.template_service.input_non_empty', side_effect=[
             'Test Template', 'Hello {name}!'
         ]), \
         patch('core.services.template_service.generate_unique_id', return_value='tpl12345'):

        template_service.create_template()

        expected_data = {
            'template_desc': 'Test Template',
            'template_code': 'Hello {name}!',
            'client_id': 'test1',
            'template_id': 'tpl12345',
            'created_at': ANY
        }
        mock_firestore.collection.assert_called_with('templates')
        mock_firestore.collection.return_value.document.assert_called_with('tpl12345')
        mock_firestore.collection.return_value.document.return_value.set.assert_called_once_with(expected_data)


def test_render_template(template_service, mock_firestore):
    template_service.logged_in_client_id = 'test1'
    template_service.fs.logged_in_client_id = 'test1'

    mock_template = MagicMock()
    mock_template.exists = True
    mock_template.to_dict.return_value = {
        'template_code': 'Hello {client_name}!',
        'client_id': 'test1'
    }

    mock_client = MagicMock()
    mock_client.exists = True
    mock_client.to_dict.return_value = {
        'client_name': 'Test Client'
    }

    collections = {
        'templates': MagicMock(
            document=MagicMock(
                return_value=MagicMock(
                    get=MagicMock(return_value=mock_template)
                )
            )
        ),
        'contacts': MagicMock(
            document=MagicMock(
                return_value=MagicMock(
                    get=MagicMock(return_value=mock_client)
                )
            )
        )
    }

    mock_firestore.collection.side_effect = lambda name: collections[name]

    # Mock render_template to return rendered string
    template_service.fs.render_template = MagicMock(return_value="Hello Test Client!")

    with patch('builtins.print') as mock_print:
        template_service.render_template('tpl12345')
        printed = "\n".join(str(call) for call in mock_print.call_args_list)
        assert "Rendered Template" in printed
        assert "Test Client" in printed


def test_log_email(template_service, mock_firestore):
    template_service.logged_in_client_id = 'test1'
    template_service.fs.logged_in_client_id = 'test1'

    mock_firestore.collection.return_value.document.return_value.set.return_value = None

    template_service.log_email('tpl12345', {'opened': True})

    mock_firestore.collection.assert_called_with('emails')
    mock_firestore.collection.return_value.document.assert_called_once()
    mock_firestore.collection.return_value.document.return_value.set.assert_called_once()
