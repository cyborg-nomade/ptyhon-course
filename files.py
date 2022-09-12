"""working with files"""

demo_file = open("demo.txt", mode="a", encoding="utf-8")
demo_file.write("Add this content!\n")
demo_file.close()
