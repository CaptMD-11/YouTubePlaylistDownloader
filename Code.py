import subprocess
import os

user_input = input("Enter link here: ")

# Command to execute
command = 'yt-dlp -x ' + user_input + ' --audio-format \"mp3\"'

path = "~/git/YouTubePlaylistDownloader/ExportedFiles"
exported_directory = os.path.expanduser(path)
os.mkdir(exported_directory)

urls = ['https://youtu.be/oiWWKumrLH8', 'https://youtu.be/tPEE9ZwTmy0']

# Execute the command

# for i in urls:
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, cwd=exported_directory)


# Wait for the command to finish and get the output and errors
output, errors = process.communicate()

# Print the output
print("Output:")
print(output.decode())
