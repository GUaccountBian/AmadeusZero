import ffmpeg
import os

def convert_to_wav(input_file):
    output_file = os.path.splitext(input_file)[0] + ".wav"
    
    if input_file.endswith('.wav'):
        print(f"{input_file} is already in .wav format")
        return

    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file)
            .global_args('-loglevel', 'error')
            .run(overwrite_output=True)
        )
        print(f"File converted successfully to {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e}")

