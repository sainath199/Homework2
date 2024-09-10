import subprocess

def random_array(arr):
    """
    Fills the input array with random numbers by the 'shuf' command.

    Args:
        arr (list): The list to be filled with random integers.

    Returns:
        list: The input list filled with random integers.
    """
    for i, _ in enumerate(arr):
        # Intentionally using subprocess without shell=True; no untrusted input is involved
        # nosec: B603
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr


