import subprocess
import time

journalctl_cmd = "sudo journalctl -u stationd -f --no-hostname -o cat"

error_keywords = [" Switchyard client connection error", "Failed to Init VRF", " error in json rpc client, with http response metadata", "VRF record is nil", "Failed to get transaction by hash: not found", "Failed to"]
command_to_run = "sudo systemctl restart stationd"

def run_command(command):
    subprocess.run(command, shell=True)

def monitor_log():
    process = subprocess.Popen(journalctl_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            line = output.strip().decode()
            print(line)
            for error_keyword in error_keywords:
                if error_keyword in line:
                    run_command(command_to_run)
                    print(f"Command '{command_to_run}' executed due to error '{error_keyword}' in log.")
                    break 
        time.sleep(1)

if __name__ == "__main__":
    monitor_log()
