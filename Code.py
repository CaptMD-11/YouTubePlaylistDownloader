import subprocess
import os


path = "~/git/YouTubePlaylistDownloader/ExportedFiles"
exported_directory = os.path.expanduser(path)
os.mkdir(exported_directory)

urls = ['https://youtu.be/oiWWKumrLH8',
        'https://youtu.be/tPEE9ZwTmy0', 'https://youtu.be/6AyEFYjv4W0']

for url in urls:
    command = 'yt-dlp -x ' + url + ' --audio-format \"mp3\"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, cwd=exported_directory)


# Wait for the command to finish and get the output and errors
output, errors = process.communicate()

# Print the output
print("Output:")
print(output.decode())
