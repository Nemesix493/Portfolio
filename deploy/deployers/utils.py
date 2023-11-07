import subprocess


def run_terminal_command(command: str, command_name: str, display_output: bool = True, return_output: bool = False):  # noqa: E501
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        if display_output:
            print(f"{command_name} output:")
            print(output)
        if return_output:
            return output
    except subprocess.CalledProcessError as e:
        raise Exception(f"{command_name} failed with return code:", e.returncode)
