import subprocess
import os

user_input = input("enter link here: ")

# Command to execute
command = 'yt-dlp -x ' + user_input + ' --audio-format \"mp3\"'

path = "~/git/YouTubeDownloader/test"
working_directory = os.path.expanduser(path)
os.mkdir(working_directory)

# Execute the command
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, cwd=working_directory)

# Wait for the command to finish and get the output and errors
output, errors = process.communicate()

# Print the output
print("Output:")
print(output.decode())
