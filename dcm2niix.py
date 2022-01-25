# source: https://github.com/rordenlab/dcm2niix
# document: https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#General_Usage
# For more help see help: dcm2niix -h


# dcm2niix.exe可将dir_dicom文件夹所包含的N组序列(比如一个文件中混杂了T1,T1C,T2等多个模态的所有dicom文件)，
# 按类型自动分离并生成N份nii文件保存至dir_nii文件夹
dir_dicom = "G:/DataSet/zhongshan2/001_ExtractObj/ME070814MR1034/T1C"
dir_nii = "./"

# 指令含义：
# -z y： 表示压缩，即gz压缩，默认是 -z n：不压缩
# -f %p_%t_%s：表示文件命名方式，%p=protocol(DICOM tag 0018,1030)，%t=time(DICOM tags 0008,0021 and 0008,0030)，%s=series number(DICOM tag 0020,0011)
#              生成的nii文件将以 %p_%t_%s.nii(.gz)的方式命名，比如 8-NV-NP+NECK_20070815170331_8.nii.gz, 更多查看 dcm2niix -h 或 官方文档
# -o X： 表示输出数据至X文件夹
cmd_string = "dcm2niix -z y -f %p_%t_%s -o {} {}".format(dir_nii, dir_dicom)

# 利用python运行cmd指令
import subprocess

subprocess.run(cmd_string)
