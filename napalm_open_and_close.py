from napalm import get_network_driver

# NX-OS device
nxos_driver = get_network_driver('nxos')
nxos_device = nxos_driver(hostname='sbx-nxos-mgmt.cisco.com', username='admin', password='Admin_1234!')
nxos_device.open()
nxos_facts = nxos_device.get_facts()
nxos_device.close()
print("NX-OS Device Facts:")
print(nxos_facts)

# IOS-XR device
iosxr_driver = get_network_driver('iosxr')
iosxr_device = iosxr_driver(hostname='sandbox-iosxr-1.cisco.com', username='admin', password='C1sco12345')
iosxr_device.open()
iosxr_facts = iosxr_device.get_facts()
iosxr_device.close()
print("\nIOS-XR Device Facts:")
print(iosxr_facts)
