""" sample_text.txt initial text:
Python files, directories, and paths are fundamental concepts when working with file systems.
A Python file is simply a script with a .py extension that contains Python code.
Directories are folders that organize and store files, and Python provides various functions to work with them, such as os.mkdir() for creating new directories.
Paths represent the location of files or directories within a file system, and Python offers functions like os.path.join() to handle them in a platform-independent manner.
Managing files, directories, and paths correctly is crucial for tasks such as reading and writing data, organizing project files, and navigating the file system efficiently.
"""

"""
This script demonstrates different ways of working with files in Python,
including reading, writing, and appending content, as well as managing file paths.

The file operations are done using:
1. `open` and `close` methods.
2. `with` statement for automatic file handling.
3. Writing files using `write()` and `append()` methods.
4. Accessing files with absolute and relative paths.

File handling in Python involves both absolute and relative paths:
- **Absolute Path**: Specifies the full path from the root directory, e.g., "C:/Users/Admin/Desktop/new_file.txt".
- **Relative Path**: Specifies the location of a file relative to the current working directory, e.g., "../new_file.txt" refers to a file in the parent directory.

"""

# Reading a file using open and close method
print("Reading a file using open and close method")
file = open("sample_text.txt")  # Opens file in default read mode
contents = file.read()  # Reads the entire contents of the file
print(contents)
file.close()  # Closes the file to release the resources

# Reading a file using 'with' keyword (No need to call close() method)
print("\nReading a file using 'with' keyword. (No need to call close() method)")
with open("sample_text.txt") as file:  # Automatically closes file after reading
    contents = file.read()  # Reads the entire contents of the file
    print(contents)

# Writing to a file using write() method
print("\nWriting a file using write() method.")
with open("sample_text.txt", mode="w") as file:  # Opens file in write mode, overwriting content
    file.write("Rewrite entire text file using write() method.")
with open("sample_text.txt") as file:  # Reads the modified file
    contents = file.read()
    print(contents)

# Writing to a file using append mode
print("\nWrite things using the append mode.")
with open("sample_text.txt", mode="a") as file:  # Opens file in append mode, does not overwrite
    file.write("\nAppending the line without altering the previous texts.")
with open("sample_text.txt") as file:  # Reads the updated file
    contents = file.read()
    print(contents)

# Handling the case where file is not present; creates a new file
print("\nWhen the file mentioned is not present, it creates a new file with the name.")
with open("new_file.txt", mode="w") as file:  # Creates new file in write mode
    file.write("New content written in new file.")
with open("new_file.txt") as file:  # Reads the newly created file
    contents = file.read()
    print(contents)

# Absolute path example: Accessing file with the full path (starting from root directory)
print("\nSo far the file and the code were in same directory.\nWhat if they are in different directory?")
with open("C:/Users/Admin/Desktop/new_file.txt") as file:  # Absolute path to the file
    contents = file.read()
    print(contents)

# Relative path example: Going up one directory and accessing the file
print("\nGoing up by one directory above and accessing the file")
with open("../new_file.txt") as file:  # Relative path, accesses file one directory above
    contents = file.read()
    print(contents)

"""
Explanation of Path Types:
- **Absolute Path**: A complete path from the root directory, specifying the exact location of the file on the file system. For example, "C:/Users/Admin/Desktop/new_file.txt" is an absolute path.
- **Relative Path**: A path relative to the current working directory. For example, "../new_file.txt" refers to the file "new_file.txt" in the parent directory (one level above the current directory).

In this code, `open("sample_text.txt")` and `open("new_file.txt")` assume that these files are in the current working directory.
The absolute path `open("C:/Users/Admin/Desktop/new_file.txt")` requires the exact location of the file, whereas `open("../new_file.txt")` uses a relative path to access the file one directory above the current directory.
"""
