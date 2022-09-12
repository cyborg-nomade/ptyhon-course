"""working with files"""

with open("demo.txt", mode="r", encoding="utf-8") as demo_file:
    line = demo_file.readline()
    while line:
        print(line)
        line = demo_file.readline()
    demo_file.close()
