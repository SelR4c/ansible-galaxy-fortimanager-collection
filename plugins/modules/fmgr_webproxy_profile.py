#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_webproxy_profile
short_description: Configure web proxy profiles.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    adom:
        description: the parameter (adom) in requested url
        type: str
        required: true
    webproxy_profile:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            header-client-ip:
                type: str
                description: 'Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header.'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-front-end-https:
                type: str
                description: 'Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header.'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-via-request:
                type: str
                description: 'Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header.'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-via-response:
                type: str
                description: 'Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header.'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-x-authenticated-groups:
                type: str
                description: 'Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP hea...'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-x-authenticated-user:
                type: str
                description: 'Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header.'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-x-forwarded-for:
                type: str
                description: 'Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header.'
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            headers:
                description: no description
                type: list
                suboptions:
                    action:
                        type: str
                        description: 'Action when HTTP the header forwarded.'
                        choices:
                            - 'add-to-request'
                            - 'add-to-response'
                            - 'remove-from-request'
                            - 'remove-from-response'
                    content:
                        type: str
                        description: 'HTTP headers content.'
                    id:
                        type: int
                        description: 'HTTP forwarded header id.'
                    name:
                        type: str
                        description: 'HTTP forwarded header name.'
            log-header-change:
                type: str
                description: 'Enable/disable logging HTTP header changes.'
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: 'Profile name.'
            strip-encoding:
                type: str
                description: 'Enable/disable stripping unsupported encoding from the request header.'
                choices:
                    - 'disable'
                    - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Configure web proxy profiles.
      fmgr_webproxy_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         webproxy_profile:
            header-client-ip: <value in [pass, add, remove]>
            header-front-end-https: <value in [pass, add, remove]>
            header-via-request: <value in [pass, add, remove]>
            header-via-response: <value in [pass, add, remove]>
            header-x-authenticated-groups: <value in [pass, add, remove]>
            header-x-authenticated-user: <value in [pass, add, remove]>
            header-x-forwarded-for: <value in [pass, add, remove]>
            headers:
              -
                  action: <value in [add-to-request, add-to-response, remove-from-request, ...]>
                  content: <value of string>
                  id: <value of integer>
                  name: <value of string>
            log-header-change: <value in [disable, enable]>
            name: <value of string>
            strip-encoding: <value in [disable, enable]>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.NAPI import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/web-proxy/profile',
        '/pm/config/global/obj/web-proxy/profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/web-proxy/profile/{profile}',
        '/pm/config/global/obj/web-proxy/profile/{profile}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'webproxy_profile': {
            'required': False,
            'type': 'dict',
            'options': {
                'header-client-ip': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'header-front-end-https': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'header-via-request': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'header-via-response': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'header-x-authenticated-groups': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'header-x-authenticated-user': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'header-x-forwarded-for': {
                    'required': False,
                    'choices': [
                        'pass',
                        'add',
                        'remove'
                    ],
                    'type': 'str'
                },
                'headers': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'action': {
                            'required': False,
                            'choices': [
                                'add-to-request',
                                'add-to-response',
                                'remove-from-request',
                                'remove-from-response'
                            ],
                            'type': 'str'
                        },
                        'content': {
                            'required': False,
                            'type': 'str'
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'name': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'log-header-change': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'strip-encoding': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'webproxy_profile'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.process_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
