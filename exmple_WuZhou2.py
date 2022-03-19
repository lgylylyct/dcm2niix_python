import subprocess
import os


root_dicom = r"I:\linguoyu\DataSet\wuzhou2\001_Dicom"
root_nii = r"I:\linguoyu\DataSet\wuzhou2\002_Nii"

for pid in os.listdir(root_dicom):
    dir_dicom = os.path.join(root_dicom, pid)
    dir_nii = os.path.join(root_nii, pid)
    os.makedirs(dir_nii)
    cmd_string = "dcm2niix -z y -f %p_%t_%s -o {} {}".format(dir_nii, dir_dicom)
    subprocess.run(cmd_string)
