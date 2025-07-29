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