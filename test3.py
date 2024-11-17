import subprocess
from azure.storage.fileshare import ShareServiceClient

# Replace with your Azure Storage connection string and file share name
connection_string = "DefaultEndpointsProtocol=https;AccountName=mlwdp100labs7488979237;AccountKey=MVN0XNPc4CLxgr8fr2gu19Yr2jqoPNFDcu0x0zxQHNmgP50AHcHLa76exO9aZqGFCztmD031xn3v+ASteHIi2g==;EndpointSuffix=core.windows.net"
share_name = "code-391ff5ac-6576-460f-ba4d-7e03433c68b6"

# Initialize the ShareServiceClient using the connection string
service_client = ShareServiceClient.from_connection_string(connection_string)

# Get the share client for the specified file share
share_client = service_client.get_share_client(share_name)

def run_py_file_in_share(file_name, directory_client=None):
    # If directory_client is not passed, start from the root directory
    if directory_client is None:
        directory_client = share_client.get_directory_client('')  # Root directory
    
    try:
        # List all items in the directory
        items = directory_client.list_directories_and_files()
        for item in items:
            if item['is_directory']:
                # If it's a directory, recurse into it
#                print(f"Directory: {item['name']}")
                subdirectory_client = directory_client.get_subdirectory_client(item['name'])
                run_py_file_in_share(file_name, subdirectory_client)
            else:
                # If it's a .py file, run it using bash command
                if item['name'].endswith('.py') and item['name'] == file_name:
#                    print(f"Found Python file: {item['name']}")
                    
                    # Prepare the bash command to run the python script directly
                    # Assuming that the file is mounted or accessible via the system path
                    command = f"python {item['name']}"
#                    print(f"Running: {command}")

                    # Run the python script using subprocess
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)

#                    # Print the output of the script
#                    print(f"STDOUT:\n{result.stdout}")
#                    if result.stderr:
#                        print(f"STDERR:\n{result.stderr}")
#                    return  # Exit after running the file (only the first match will be run)

    except Exception as e:
        print(f"Error: {e}")

# Call the function to find and run the .py file
run_py_file_in_share('github_actions_testing.py')
