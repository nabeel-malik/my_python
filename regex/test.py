import os

src = 'input_files/my_packsim/src/include'
os.chdir(src)

for file in os.listdir():
    with open(file, 'w') as f:
        pass

