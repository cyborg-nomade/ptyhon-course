"""working with files"""

demo_file = open("demo.txt", mode="w", encoding="utf-8")
demo_file.write("Hello from Python!")
demo_file.close()
