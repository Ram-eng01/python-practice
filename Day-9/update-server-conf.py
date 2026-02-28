def update_config(file_path, key, value):
    # Read the existing content of the server configuration file 
    with open(file_path,'r') as file:
        lines = file.readlines()
        
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config_file = 'server.conf'

key_to_update = 'MAX_CONNECTIONS'
new_value = '6000' # New maximum connections allowed

update_config(server_config_file, key_to_update, new_value)