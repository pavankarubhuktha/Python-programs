#7. Write a program to delete files in different ways?
with open("file2","x") as file2:
    pass
with open("file3","x") as file2:
    pass
with open("file4","x") as file2:
    pass
import os
os.remove("file2")
print("file remove from os.remove()")
os.unlink("file3")
print("file remove from os.unlink()")

from pathlib import Path
file = Path("file4")
file . unlink()
print("file deleted from")