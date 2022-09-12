"""working with files"""

demo_file = open("demo.txt", mode="r", encoding="utf-8")
# demo_file.write("Add this content!\n")
# file_content = demo_file.read()
# file_lines = demo_file.readlines()
first_line = demo_file.readline()
demo_file.close()
# print(file_content)
# print(file_lines)
print(first_line)

# for line in file_lines:
#     print(line[:-1])
