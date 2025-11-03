from napalm import get_network_driver
import json 

# Get NX-OS driver class using NAPALM's factory function
nxos_driver = get_network_driver('nxos')

# Create NX-OS device instance with credentials
nxos_device = nxos_driver(hostname='sbx-nxos-mgmt.cisco.com', username='admin', password='Admin_1234!')

# Open connection to NX-OS device
nxos_device.open()

# Retrieve basic facts from NX-OS device
nxos_facts = nxos_device.get_facts()

# Close connection
nxos_device.close()

print("NX-OS Device Facts:")
print(json.dumps(nxos_facts, indent=2))


iosxr_driver = get_network_driver('iosxr')
iosxr_device = iosxr_driver(hostname='sandbox-iosxr-1.cisco.com', username='admin', password='C1sco12345')
iosxr_device.open()
iosxr_facts = iosxr_device.get_facts()
iosxr_device.close()
print("\nIOS-XR Device Facts:")
print(json.dumps(iosxr_facts, indent=2))
