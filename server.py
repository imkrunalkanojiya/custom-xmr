import subprocess

process = subprocess.Popen(['./xmrig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())
        
stderr_output = process.stderr.read()
if stderr_output:
    print(stderr_output.strip())