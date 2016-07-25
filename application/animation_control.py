import os

def save_frame(test_environment, config):
    postscript_file_name = "%srendered_frame.ps" %(config.animation_folder)
    test_environment.canvas.postscript(file = postscript_file_name, colormode='color')
    file_name = "%stmp_frames/%06d%06d.png" %(config.animation_folder, test_environment.generation_number, test_environment.steps_this_generation)
    os.system("convert %s %s" %(postscript_file_name, file_name))
    os.system("rm %s" %(postscript_file_name))