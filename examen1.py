from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    command = "ip address print"
    device = {
         'device_type': 'mikrotik_routeros', 
         'host':   '192.168.88.1', 
         'username': 'admin', 
         'password': 'Unsij2022', 
         'port':'23',
    }
    result = send_show_command(device, command)
    print(result)