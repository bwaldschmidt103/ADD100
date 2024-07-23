"""
In this assignment, you will create a Python script to practice basic file operations using the os module. Your script will organize files into newly created directories based on their file types.

Objectives
Create a new directory.
Create subdirectories and organize files into them.
Understand and apply basic file operations in Python.
 
Instructions
Create a new Python script named file_organizer.py.
Use the os.mkdir() function to create a new directory named MyFiles.
Inside MyFiles, create three subdirectories named Docs, Images, and Videos using the same mkdir() function.
Hand in a screenshot. Include your code and the created folders. image sample  

Submission
Submit the following two items by uploading to a single folder on GitHub and handing in the link (you can drag the whole folder to GitHub):

Your file_organizer.py script file.
A screenshot showing the created directories MyFiles, Docs, Images, and Videos in your file system. Ensure that the path and directory names are visible in the screenshot. You can 
 
Evaluation Criteria
Correct creation of directories and subdirectories.
"""

import os

def create_directories(base_path):
    # Create the main directory
    os.mkdir(base_path)

    # Create subdirectories
    os.mkdir(os.path.join(base_path, 'Docs'))
    os.mkdir(os.path.join(base_path, 'Images'))
    os.mkdir(os.path.join(base_path, 'Videos'))

def main():
    base_path = os.path.abspath('C:\z_admin\School\Assignments\add100\python\pe2_4.4\MyFiles')
    create_directories(base_path)
    print("Directories created successfully!")

if __name__ == "__main__":
    main()

    