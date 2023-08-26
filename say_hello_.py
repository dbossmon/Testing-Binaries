import subprocess

binary_path = "./hello"
arguments = ["./hello"]  # Optional command-line arguments

try:
    subprocess.run([binary_path] + arguments, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the binary: {e}")
