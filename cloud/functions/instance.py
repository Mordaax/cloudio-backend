from datetime import datetime, timedelta
from google.protobuf.json_format import MessageToJson, MessageToDict

# ... (previous code)

# Calculate the deletion time (1 hour from now)
delete_time = datetime.utcnow() + timedelta(hours=1)
delete_time_str = delete_time.isoformat() + 'Z'


from google.cloud import compute_v1

from google.oauth2 import service_account
import proto
import json
import os
credentials = service_account.Credentials.from_service_account_file(
    'key.json')

INSTANCE_NAME = 'instance-name'
MACHINE_TYPE = 'projects/peaceful-rex-298113/zones/asia-southeast1-a/machineTypes/e2-micro'

SUBNETWORK = 'projects/peaceful-rex-298113/regions/asia-southeast1/subnetworks/default'

SOURCE_IMAGE = 'projects/debian-cloud/global/images/debian-11-bullseye-v20231115'
NETWORK_INTERFACE = {
    'subnetwork':SUBNETWORK,
    'access_configs': [
        {
            'name':'External NAT'
        }
    ]
}

compute_client = compute_v1.InstancesClient(credentials=credentials)


from Crypto.PublicKey import RSA  # provided by pycryptodome

def create_instance(instance_name):
    try:
        key = RSA.generate(2048,os.urandom)

        private_key_string = key.export_key().decode('utf-8')


        public_key_string = f"ssh-rsa {key.export_key(format='OpenSSH').decode('utf-8').split(' ')[1]}"


        config = {
        'name' : instance_name,
        'machine_type' : MACHINE_TYPE,
        'disks': [
            {
                'boot': True,
                'auto_delete': True,
                'initialize_params': {
                    'source_image': SOURCE_IMAGE,
                }
            }
        ],
        'network_interfaces' : [NETWORK_INTERFACE],

        'metadata': {
                        'items': [
                            {
                                'key': 'ssh-keys',
                                'value': f'user:{public_key_string}'
                            }
                        ]
                    },


        }
        operation = compute_client.insert(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance_resource=config
        )

        operation.result()

        instance = compute_client.get(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name  
        )
        json_string = json.loads(proto.Message.to_json(instance))

        network_interface = json_string.get("networkInterfaces")[0]

        subnet = json_string.get("networkInterfaces")[0].get("subnetwork").split('/')[-1]
        machinetype = json_string.get("machineType").split('/')[-1]
        zone = json_string.get("zone").split('/')[-1]
        disksize = json_string.get("disks")[0].get("diskSizeGb")+"GB"
        sourceimage = json_string.get("disks")[0].get("licenses")[0].split("/")[-1]

        return network_interface.get("accessConfigs")[0].get("natIP"), network_interface.get("networkIP"), zone,subnet, sourceimage,machinetype,disksize,private_key_string

    except:
        return False    

def delete_instance(instance_name):
    print("Deleting instance.....")
    try:
        operation = compute_client.delete(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name
        )
        operation.result()
        return True
    except:
        return False

def stop_instance(instance_name):
    try:
        operation = compute_client.stop(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name  
        )
        operation.result()
        return True
    except:
        return False
    
def start_instance(instance_name):
    try:
        operation = compute_client.start(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name  
        )
        operation.result()

        instance = compute_client.get(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name 
        )
        json_string = json.loads(proto.Message.to_json(instance))


        network_interface = json_string.get("networkInterfaces")[0]
        
        return network_interface.get("accessConfigs")[0].get("natIP")

        
    except:
        return False
    
def publish_to_vuln(instance_name):
    try:
        
        new_subnetwork = 'projects/peaceful-rex-298113/regions/asia-southeast1/subnetworks/vuln-network'


        instance = compute_client.get(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name
        )
     
        instance['networkInterfaces'][0]['subnetwork'] = new_subnetwork

        update_operation = compute_client.instances().update(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name,
            body=instance
        )


        instance = compute_client.get(
            project='peaceful-rex-298113',
            zone='asia-southeast1-a',
            instance=instance_name 
        )
     
        return 'hello' 

        
    except:
        return False

