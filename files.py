"""working with files"""

demo_file = open("demo.txt", mode="r", encoding="utf-8")
file_content = demo_file.read()
demo_file.close()
print(file_content)
