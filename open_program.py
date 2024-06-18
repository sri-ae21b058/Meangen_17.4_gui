import subprocess
def run_program():
    subprocess.run(['gfortran', 'meangen-17.4.f', '-o', 'meangen-17.4'])

    process= subprocess.Popen(['./meangen-17.4'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    process.stdin.write("F") # This is the input that the program is waiting for
    process.stdin.flush() # This will send the input to the program

    output, error = process.communicate()
    print(output)
    print(error)

    process.stdin.close()