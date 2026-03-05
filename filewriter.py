name = "Royce Chua"
file = open("newfile1.txt", 'w')
file.write(f"Hello, {name}!\n")
file.write("Isn't this amazing!\n")
file.write("that we can create and write on text files\n")
file.write("using Python.")
file.close()

with open("newfile2.txt", "w") as file:

    file.write("This message was created using Python!")
    
print("File newfile2.txt has been created with the message.")