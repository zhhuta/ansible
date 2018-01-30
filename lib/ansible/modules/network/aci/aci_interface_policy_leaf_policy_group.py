#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Bruno Calogero <brunocalogero@hotmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: aci_interface_policy_leaf_policy_group
short_description: Add Fabric Interface Policy Leaf Policy Groups on Cisco ACI fabrics.
description:
- Add Fabric Interface Policy Leaf Policy Groups on Cisco ACI fabrics.
- More information from the internal APIC class I(infra:AccBndlGrp), I(infra:AccPortGrp) at
  U(https://developer.cisco.com/site/aci/docs/apis/apic-mim-ref/).
author:
- Bruno Calogero (@brunocalogero)
version_added: '2.5'
notes:
- When using the module please select the appropriate link_aggregation_type (lag_type).
  C(link) for Port Channel(PC), C(node) for Virtual Port Channel(VPC) and C(leaf) for Leaf Access Port Policy Group.
options:
 policy_group:
   description:
   - Name of the leaf policy group to be added/deleted.
   aliases: [ name, policy_group_name ]
 description:
   description:
   - Description for the leaf policy group to be created.
   aliases: [ descr ]
 lag_type:
   description:
   - Selector for the type of leaf policy group we want to create.
   aliases: [ lag_type_name ]
 link_level_policy:
   description:
   - Choice of link_level_policy to be used as part of the leaf policy group to be created.
   aliases: [ link_level_policy_name ]
 cdp_policy:
   description:
   - Choice of cdp_policy to be used as part of the leaf policy group to be created.
   aliases: [ cdp_policy_name ]
 mcp_policy:
   description:
   - Choice of mcp_policy to be used as part of the leaf policy group to be created.
   aliases: [ mcp_policy_name ]
 lldp_policy:
   description:
   - Choice of lldp_policy to be used as part of the leaf policy group to be created.
   aliases: [ lldp_policy_name ]
 stp_interface_policy:
   description:
   - Choice of stp_interface_policy to be used as part of the leaf policy group to be created.
   aliases: [ stp_interface_policy_name ]
 egress_data_plane_policing_policy:
   description:
   - Choice of egress_data_plane_policing_policy to be used as part of the leaf policy group to be created.
   aliases: [ egress_data_plane_policing_policy_name ]
 ingress_data_plane_policing_policy:
   description:
   - Choice of ingress_data_plane_policing_policy to be used as part of the leaf policy group to be created.
   aliases: [ ingress_data_plane_policing_policy_name ]
 priority_flow_control_policy:
   description:
   - Choice of priority_flow_control_policy to be used as part of the leaf policy group to be created.
   aliases: [ priority_flow_control_policy_name ]
 fibre_channel_interface_policy:
   description:
   - Choice of fibre_channel_interface_policy to be used as part of the leaf policy group to be created.
   aliases: [ fibre_channel_interface_policy_name ]
 slow_drain_policy:
   description:
   - Choice of slow_drain_policy to be used as part of the leaf policy group to be created.
   aliases: [ slow_drain_policy_name ]
 port_channel_policy:
   description:
   - Choice of port_channel_policy to be used as part of the leaf policy group to be created.
   aliases: [ port_channel_policy_name ]
 monitoring_policy:
   description:
   - Choice of monitoring_policy to be used as part of the leaf policy group to be created.
   aliases: [ monitoring_policy_name ]
 storm_control_interface_policy:
   description:
   - Choice of storm_control_interface_policy to be used as part of the leaf policy group to be created.
   aliases: [ storm_control_interface_policy_name ]
 l2_interface_policy:
   description:
   - Choice of l2_interface_policy to be used as part of the leaf policy group to be created.
   aliases: [ l2_interface_policy_name ]
 port_security_policy:
   description:
   - Choice of port_security_policy to be used as part of the leaf policy group to be created.
   aliases: [ port_security_policy_name ]
 aep:
   description:
   - Choice of attached_entity_profile (AEP) to be used as part of the leaf policy group to be created.
   aliases: [ aep_name ]
 state:
   description:
   - Use C(present) or C(absent) for adding or removing.
   - Use C(query) for listing an object or multiple objects.
   choices: [ absent, present, query ]
   default: present
extends_documentation_fragment: aci
'''

EXAMPLES = r'''
- name: creating a Port Channel (PC) Interface Policy Group
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: yourusername
    password: yourpassword
    policy_group: policygroupname
    description: policygroupname description
    lag_type: link
    link_level_policy: whateverlinklevelpolicy
    fibre_channel_interface_policy: whateverfcpolicy
    state: present

- name: creating a Virtual Port Channel (VPC) Interface Policy Group (no description)
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: yourusername
    password: yourpassword
    policy_group: policygroupname
    lag_type: node
    link_level_policy: whateverlinklevelpolicy
    fibre_channel_interface_policy: whateverfcpolicy
    state: present

- name: creating a Leaf Access Port Policy Group (no description)
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: yourusername
    password: yourpassword
    policy_group: policygroupname
    lag_type: leaf
    link_level_policy: whateverlinklevelpolicy
    fibre_channel_interface_policy: whateverfcpolicy
    state: present

- name: deleting an Interface policy Leaf Policy Group
  aci_interface_policy_leaf_policy_group:
    host: apic
    username: yourusername
    password: yourpassword
    policy_group: policygroupname
    lag_type: type_name
    state: absent
'''

RETURN = ''' # '''

from ansible.module_utils.network.aci.aci import ACIModule, aci_argument_spec
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = aci_argument_spec()
    argument_spec.update({
        'policy_group': dict(type='str', aliases=['name', 'policy_group_name']),
        'description': dict(type='str', aliases=['descr']),
        # NOTE: Since this module needs to include both infra:AccBndlGrp (for PC andVPC) and infra:AccPortGrp (for leaf access port policy group):
        # NOTE: I'll allow the user to make the choice here (link(PC), node(VPC), leaf(leaf-access port policy group))
        'lag_type': dict(type='str', aliases=['lag_type_name']),
        'link_level_policy': dict(type='str', aliases=['link_level_policy_name']),
        'cdp_policy': dict(type='str', aliases=['cdp_policy_name']),
        'mcp_policy': dict(type='str', aliases=['mcp_policy_name']),
        'lldp_policy': dict(type='str', aliases=['lldp_policy_name']),
        'stp_interface_policy': dict(type='str', aliases=['stp_interface_policy_name']),
        'egress_data_plane_policing_policy': dict(type='str', aliases=['egress_data_plane_policing_policy_name']),
        'ingress_data_plane_policing_policy': dict(type='str', aliases=['ingress_data_plane_policing_policy_name']),
        'priority_flow_control_policy': dict(type='str', aliases=['priority_flow_control_policy_name']),
        'fibre_channel_interface_policy': dict(type='str', aliases=['fibre_channel_interface_policy_name']),
        'slow_drain_policy': dict(type='str', aliases=['slow_drain_policy_name']),
        'port_channel_policy': dict(type='str', aliases=['port_channel_policy_name']),
        'monitoring_policy': dict(type='str', aliases=['monitoring_policy_name']),
        'storm_control_interface_policy': dict(type='str', aliases=['storm_control_interface_policy_name']),
        'l2_interface_policy': dict(type='str', aliases=['l2_interface_policy_name']),
        'port_security_policy': dict(type='str', aliases=['port_security_policy_name']),
        'aep': dict(type='str', aliases=['aep_name']),
        'state': dict(type='str', default='present', choices=['absent', 'present', 'query'])
    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ['state', 'absent', ['policy_group', 'lag_type']],
            ['state', 'present', ['policy_group', 'lag_type']]
        ]
    )

    policy_group = module.params['policy_group']
    description = module.params['description']
    lag_type = module.params['lag_type']
    link_level_policy = module.params['link_level_policy']
    cdp_policy = module.params['cdp_policy']
    mcp_policy = module.params['mcp_policy']
    lldp_policy = module.params['lldp_policy']
    stp_interface_policy = module.params['stp_interface_policy']
    egress_data_plane_policing_policy = module.params['egress_data_plane_policing_policy']
    ingress_data_plane_policing_policy = module.params['ingress_data_plane_policing_policy']
    priority_flow_control_policy = module.params['priority_flow_control_policy']
    fibre_channel_interface_policy = module.params['fibre_channel_interface_policy']
    slow_drain_policy = module.params['slow_drain_policy']
    port_channel_policy = module.params['port_channel_policy']
    monitoring_policy = module.params['monitoring_policy']
    storm_control_interface_policy = module.params['storm_control_interface_policy']
    l2_interface_policy = module.params['l2_interface_policy']
    port_security_policy = module.params['port_security_policy']
    aep = module.params['aep']
    state = module.params['state']
    aci_class_name = ''
    dn_name = ''
    class_config_dict = {}

    if lag_type == 'leaf':
        aci_class_name = 'infraAccPortGrp'
        dn_name = 'accportgrp'
        class_config_dict = dict(
            name=policy_group,
            descr=description,
            dn='uni/infra/funcprof/{0}-{1}'.format(dn_name, policy_group)
        )
    elif lag_type == 'link' or lag_type == 'node':
        aci_class_name = 'infraAccBndlGrp'
        dn_name = 'accbundle'
        class_config_dict = dict(
            name=policy_group,
            descr=description,
            lagT=lag_type,
            dn='uni/infra/funcprof/{0}-{1}'.format(dn_name, policy_group)
        )

    aci = ACIModule(module)
    aci.construct_url(
        root_class=dict(
            aci_class=aci_class_name,
            aci_rn='infra/funcprof/{0}-{1}'.format(dn_name, policy_group),
            filter_target='eq({0}.name, "{1}")'.format(aci_class_name, policy_group),
            module_object=policy_group
        ),
        child_classes=[
            'infraRsMonIfInfraPol', 'infraRsLldpIfPol', 'infraRsFcIfPol',
            'infraRsLacpPol', 'infraRsL2PortSecurityPol', 'infraRsHIfPol',
            'infraRsQosPfcIfPol', 'infraRsStpIfPol', 'infraRsQosIngressDppIfPol',
            'infraRsStormctrlIfPol', 'infraRsQosEgressDppIfPol', 'infraRsQosSdIfPol',
            'infraRsAttEntP', 'infraRsMcpIfPol', 'infraRsCdpIfPol', 'infraRsL2IfPol'
        ]
    )

    aci.get_existing()

    if state == 'present':
        # Filter out module params with null values
        aci.payload(
            aci_class=aci_class_name,
            class_config=class_config_dict,
            child_configs=[
                dict(
                    infraRsMonIfInfraPol=dict(
                        attributes=dict(
                            tnMonInfraPolName=monitoring_policy
                        )
                    )
                ),
                dict(
                    infraRsLldpIfPol=dict(
                        attributes=dict(
                            tnLldpIfPolName=lldp_policy
                        )
                    )
                ),
                dict(
                    infraRsFcIfPol=dict(
                        attributes=dict(
                            tnFcIfPolName=fibre_channel_interface_policy
                        )
                    )
                ),
                dict(
                    infraRsLacpPol=dict(
                        attributes=dict(
                            tnLacpLagPolName=port_channel_policy
                        )
                    )
                ),
                dict(
                    infraRsL2PortSecurityPol=dict(
                        attributes=dict(
                            tnL2PortSecurityPolName=port_security_policy
                        )
                    )
                ),
                dict(
                    infraRsHIfPol=dict(
                        attributes=dict(
                            tnFabricHIfPolName=link_level_policy
                        )
                    )
                ),
                dict(
                    infraRsQosPfcIfPol=dict(
                        attributes=dict(
                            tnQosPfcIfPolName=priority_flow_control_policy
                        )
                    )
                ),
                dict(
                    infraRsStpIfPol=dict(
                        attributes=dict(
                            tnStpIfPolName=stp_interface_policy
                        )
                    )
                ),
                dict(
                    infraRsQosIngressDppIfPol=dict(
                        attributes=dict(
                            tnQosDppPolName=ingress_data_plane_policing_policy
                        )
                    )
                ),
                dict(
                    infraRsStormctrlIfPol=dict(
                        attributes=dict(
                            tnStormctrlIfPolName=storm_control_interface_policy
                        )
                    )
                ),
                dict(
                    infraRsQosEgressDppIfPol=dict(
                        attributes=dict(
                            tnQosDppPolName=egress_data_plane_policing_policy
                        )
                    )
                ),
                dict(
                    infraRsQosSdIfPol=dict(
                        attributes=dict(
                            tnQosSdIfPolName=slow_drain_policy
                        )
                    )
                ),
                dict(
                    infraRsMcpIfPol=dict(
                        attributes=dict(
                            tnMcpIfPolName=mcp_policy
                        )
                    )
                ),
                dict(
                    infraRsCdpIfPol=dict(
                        attributes=dict(
                            tnCdpIfPolName=cdp_policy
                        )
                    )
                ),
                dict(
                    infraRsL2IfPol=dict(
                        attributes=dict(
                            tnL2IfPolName=l2_interface_policy
                        )
                    )
                ),
                dict(
                    infraRsAttEntP=dict(
                        attributes=dict(
                            tDn='uni/infra/attentp-{0}'.format(aep)
                        )
                    )
                )
            ],
        )

        # Generate config diff which will be used as POST request body
        aci.get_diff(aci_class=aci_class_name)

        # Submit changes if module not in check_mode and the proposed is different than existing
        aci.post_config()

    elif state == 'absent':
        aci.delete_config()

    module.exit_json(**aci.result)


if __name__ == "__main__":
    main()
