import os
import platform


print(platform.uname())

os.mkdir("./os-module/my_first_dir")
print(os.listdir())

os.makedirs("01/02")
os.chdir("01")
print(os.listdir())
