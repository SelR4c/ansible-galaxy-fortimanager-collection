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
module: fmgr_firewall_address6
short_description: Configure IPv6 firewall addresses.
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
    firewall_address6:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            cache-ttl:
                type: int
                description: 'Minimal TTL of individual IPv6 addresses in FQDN cache.'
            color:
                type: int
                description: 'Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1).'
            comment:
                type: str
                description: 'Comment.'
            dynamic_mapping:
                description: no description
                type: list
                suboptions:
                    _scope:
                        description: no description
                        type: list
                        suboptions:
                            name:
                                type: str
                                description: no description
                            vdom:
                                type: str
                                description: no description
                    cache-ttl:
                        type: int
                        description: no description
                    color:
                        type: int
                        description: no description
                    comment:
                        type: str
                        description: no description
                    end-ip:
                        type: str
                        description: no description
                    fqdn:
                        type: str
                        description: no description
                    host:
                        type: str
                        description: no description
                    host-type:
                        type: str
                        description: no description
                        choices:
                            - 'any'
                            - 'specific'
                    ip6:
                        type: str
                        description: no description
                    obj-id:
                        type: str
                        description: no description
                    sdn:
                        type: str
                        description: no description
                        choices:
                            - 'nsx'
                    start-ip:
                        type: str
                        description: no description
                    tags:
                        type: str
                        description: no description
                    template:
                        type: str
                        description: no description
                    type:
                        type: str
                        description: no description
                        choices:
                            - 'ipprefix'
                            - 'iprange'
                            - 'nsx'
                            - 'dynamic'
                            - 'fqdn'
                            - 'template'
                    uuid:
                        type: str
                        description: no description
                    visibility:
                        type: str
                        description: no description
                        choices:
                            - 'disable'
                            - 'enable'
            end-ip:
                type: str
                description: 'Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).'
            fqdn:
                type: str
                description: 'Fully qualified domain name.'
            host:
                type: str
                description: 'Host Address.'
            host-type:
                type: str
                description: 'Host type.'
                choices:
                    - 'any'
                    - 'specific'
            ip6:
                type: str
                description: 'IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx).'
            list:
                description: no description
                type: list
                suboptions:
                    ip:
                        type: str
                        description: 'IP.'
            name:
                type: str
                description: 'Address name.'
            obj-id:
                type: str
                description: 'Object ID for NSX.'
            sdn:
                type: str
                description: 'SDN.'
                choices:
                    - 'nsx'
            start-ip:
                type: str
                description: 'First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).'
            subnet-segment:
                description: no description
                type: list
                suboptions:
                    name:
                        type: str
                        description: 'Name.'
                    type:
                        type: str
                        description: 'Subnet segment type.'
                        choices:
                            - 'any'
                            - 'specific'
                    value:
                        type: str
                        description: 'Subnet segment value.'
            tagging:
                description: no description
                type: list
                suboptions:
                    category:
                        type: str
                        description: 'Tag category.'
                    name:
                        type: str
                        description: 'Tagging entry name.'
                    tags:
                        description: no description
                        type: str
            template:
                type: str
                description: 'IPv6 address template.'
            type:
                type: str
                description: 'Type of IPv6 address object (default = ipprefix).'
                choices:
                    - 'ipprefix'
                    - 'iprange'
                    - 'nsx'
                    - 'dynamic'
                    - 'fqdn'
                    - 'template'
            uuid:
                type: str
                description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
            visibility:
                type: str
                description: 'Enable/disable the visibility of the object in the GUI.'
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
    - name: Configure IPv6 firewall addresses.
      fmgr_firewall_address6:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_address6:
            cache-ttl: <value of integer>
            color: <value of integer>
            comment: <value of string>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  cache-ttl: <value of integer>
                  color: <value of integer>
                  comment: <value of string>
                  end-ip: <value of string>
                  fqdn: <value of string>
                  host: <value of string>
                  host-type: <value in [any, specific]>
                  ip6: <value of string>
                  obj-id: <value of string>
                  sdn: <value in [nsx]>
                  start-ip: <value of string>
                  tags: <value of string>
                  template: <value of string>
                  type: <value in [ipprefix, iprange, nsx, ...]>
                  uuid: <value of string>
                  visibility: <value in [disable, enable]>
            end-ip: <value of string>
            fqdn: <value of string>
            host: <value of string>
            host-type: <value in [any, specific]>
            ip6: <value of string>
            list:
              -
                  ip: <value of string>
            name: <value of string>
            obj-id: <value of string>
            sdn: <value in [nsx]>
            start-ip: <value of string>
            subnet-segment:
              -
                  name: <value of string>
                  type: <value in [any, specific]>
                  value: <value of string>
            tagging:
              -
                  category: <value of string>
                  name: <value of string>
                  tags: <value of string>
            template: <value of string>
            type: <value in [ipprefix, iprange, nsx, ...]>
            uuid: <value of string>
            visibility: <value in [disable, enable]>

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
        '/pm/config/adom/{adom}/obj/firewall/address6',
        '/pm/config/global/obj/firewall/address6'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/address6/{address6}',
        '/pm/config/global/obj/firewall/address6/{address6}'
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
        'firewall_address6': {
            'required': False,
            'type': 'dict',
            'options': {
                'cache-ttl': {
                    'required': False,
                    'type': 'int'
                },
                'color': {
                    'required': False,
                    'type': 'int'
                },
                'comment': {
                    'required': False,
                    'type': 'str'
                },
                'dynamic_mapping': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        '_scope': {
                            'required': False,
                            'type': 'list',
                            'options': {
                                'name': {
                                    'required': False,
                                    'type': 'str'
                                },
                                'vdom': {
                                    'required': False,
                                    'type': 'str'
                                }
                            }
                        },
                        'cache-ttl': {
                            'required': False,
                            'type': 'int'
                        },
                        'color': {
                            'required': False,
                            'type': 'int'
                        },
                        'comment': {
                            'required': False,
                            'type': 'str'
                        },
                        'end-ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'fqdn': {
                            'required': False,
                            'type': 'str'
                        },
                        'host': {
                            'required': False,
                            'type': 'str'
                        },
                        'host-type': {
                            'required': False,
                            'choices': [
                                'any',
                                'specific'
                            ],
                            'type': 'str'
                        },
                        'ip6': {
                            'required': False,
                            'type': 'str'
                        },
                        'obj-id': {
                            'required': False,
                            'type': 'str'
                        },
                        'sdn': {
                            'required': False,
                            'choices': [
                                'nsx'
                            ],
                            'type': 'str'
                        },
                        'start-ip': {
                            'required': False,
                            'type': 'str'
                        },
                        'tags': {
                            'required': False,
                            'type': 'str'
                        },
                        'template': {
                            'required': False,
                            'type': 'str'
                        },
                        'type': {
                            'required': False,
                            'choices': [
                                'ipprefix',
                                'iprange',
                                'nsx',
                                'dynamic',
                                'fqdn',
                                'template'
                            ],
                            'type': 'str'
                        },
                        'uuid': {
                            'required': False,
                            'type': 'str'
                        },
                        'visibility': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        }
                    }
                },
                'end-ip': {
                    'required': False,
                    'type': 'str'
                },
                'fqdn': {
                    'required': False,
                    'type': 'str'
                },
                'host': {
                    'required': False,
                    'type': 'str'
                },
                'host-type': {
                    'required': False,
                    'choices': [
                        'any',
                        'specific'
                    ],
                    'type': 'str'
                },
                'ip6': {
                    'required': False,
                    'type': 'str'
                },
                'list': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'ip': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'name': {
                    'required': True,
                    'type': 'str'
                },
                'obj-id': {
                    'required': False,
                    'type': 'str'
                },
                'sdn': {
                    'required': False,
                    'choices': [
                        'nsx'
                    ],
                    'type': 'str'
                },
                'start-ip': {
                    'required': False,
                    'type': 'str'
                },
                'subnet-segment': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'name': {
                            'required': False,
                            'type': 'str'
                        },
                        'type': {
                            'required': False,
                            'choices': [
                                'any',
                                'specific'
                            ],
                            'type': 'str'
                        },
                        'value': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'tagging': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'category': {
                            'required': False,
                            'type': 'str'
                        },
                        'name': {
                            'required': False,
                            'type': 'str'
                        },
                        'tags': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'template': {
                    'required': False,
                    'type': 'str'
                },
                'type': {
                    'required': False,
                    'choices': [
                        'ipprefix',
                        'iprange',
                        'nsx',
                        'dynamic',
                        'fqdn',
                        'template'
                    ],
                    'type': 'str'
                },
                'uuid': {
                    'required': False,
                    'type': 'str'
                },
                'visibility': {
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
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_address6'),
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
