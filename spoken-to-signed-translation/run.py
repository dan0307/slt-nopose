import subprocess
from pose_format import Pose
from pose_format.pose_visualizer import PoseVisualizer
from IPython.display import Image
import os
import time

# Function to check if the file exists
def file_exists(filename):
    return os.path.exists(filename)

def delete_file(filename):
    if file_exists(filename):
        os.remove(filename)
        print("pose file deleted.")

def text_to_pose(text):
    # DCommand to generate pose file from sequence of words
    command = "text_to_gloss_to_pose   --text '" + text + "'   --glosser 'simple'   --lexicon 'assets/dummy_lexicon'   --spoken-language 'de'   --signed-language 'sgg'   --pose 'result.pose'"    
    subprocess.run(command, shell=True) # Execute the command to generate the file
    if file_exists("result.pose"):
        print("result.pose has been generated. Generating result.gif...")

def pose_to_gif(posedir):
    if file_exists(posedir):
        with open(posedir, "rb") as f:
            pose = Pose.read(f.read())
        v = PoseVisualizer(pose) # THIS IS THE RESULTING GIF
        v.save_gif("result.gif", v.draw())
    else:
        print("Seems like .pose file was not generated. Words might be missing in the vocabulary (Kamila: We still need to catch this exception smoothly + add statistics of files that were not generated)")


text = input("Enter text: ") # Take user'r string. To be changed, but here's the word sequence to be translated
text_to_pose(text)
filename = "result.pose" 
pose_to_gif(filename) # the resulting output
delete_file(filename) # delete pose file
