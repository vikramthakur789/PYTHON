# Write and read from a file
with open("example.txt", "w") as file:
    file.write("Hello, Python File Handling!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
