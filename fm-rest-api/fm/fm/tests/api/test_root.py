# Copyright 2013 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# Copyright 2020 Intel Corporation.
#

from fm.tests.api import base


class TestRoot(base.FunctionalTest):

    def test_get_root(self):
        data = self.get_json('/', path_prefix='')
        self.assertEqual(data['default_version']['id'], 'v1')
        # Check fields are not empty
        [self.assertNotIn(f, ['', []]) for f in list(data.keys())]


class TestV1Root(base.FunctionalTest):

    def test_get_v1_root(self):
        data = self.get_json('/')
        self.assertEqual(data['id'], 'v1')
        # Check fields are not empty
        [self.assertNotIn(f, ['', []]) for f in list(data.keys())]
        # Check if the resources are present
        self.assertIn({'type': 'application/vnd.openstack.fm.v1+json',
                       'base': 'application/json'}, data['media_types'])
