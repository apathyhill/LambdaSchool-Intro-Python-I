"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os

with open(os.path.dirname(__file__) + "\\foo.txt", "r") as f:
    print(f.read())
    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open(os.path.dirname(__file__) + "\\bar.txt", "w") as f:
    f.writelines([
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n",
        "Duis eu enim ut ante rhoncus fermentum ac ut massa.\n"
        "Curabitur vulputate mi eget lectus accumsan hendrerit a vitae metus.\n"])
    f.close()