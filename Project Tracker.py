#Project Tracker
import json
import time
import sys
import copy
from tkinter import *

with open('ProjectList.txt', 'r') as projectListFile:
    #json.dump(projectList, projectListFile)
    projectList = json.load(projectListFile)

def mainMenu():
    mainMenuChoice = input('\n1) View Project Lists\n2) Edit Project\n3) Add New Project\n4) Delete Project\n5) Exit\n')
    if mainMenuChoice == '1':
        printProjectList()
    elif mainMenuChoice == '2':
        editProject()
    elif mainMenuChoice == '3':
        addNewProject()
    elif mainMenuChoice == '4':
        deleteProject()
    elif mainMenuChoice == '5':
        sys.exit()

def printProjectList():
    print('\n')
    for i, n in enumerate(projectList):
        print(i, (projectList[i]['Name']))
        print('  ' + projectList[i]['Notes'])
        print('  Invoiceable? ' + projectList[i]['Invoiceable'])
        print('  ' + projectList[i]['Date Added'] + '\n')
    mainMenu()

def editProject():

    #Copies the selected list entry to a temp version, which is then edited
    print('\n')
    for i, n in enumerate(projectList):
        print(i, (projectList[i]['Name']))
    editIndex = int(input('\nProject Index to Edit: '))
    
    projCache = copy.copy(projectList[editIndex])


    #Below edits the temp project name
    projCache['Name'] = input('Enter new name for \'' + projectList[editIndex]['Name'] + '\' (blank entry leaves it unchanged): ')
    if projCache['Name'] == '':
        projCache['Name'] = copy.copy(projectList[editIndex]['Name'])
        print('Name: ' + projCache['Name'])
              
    else: print(projectList[editIndex]['Name'] + ' changed to ' + projCache['Name'])

              
    #Below edits the temp project notes             
    projCache['Notes'] = input('Enter new notes for \'' + projectList[editIndex]['Name'] + '\' (blank entry leaves it unchanged): ')
    if projCache['Notes'] == '':
        projCache['Notes'] = copy.copy(projectList[editIndex]['Notes'])
        print('Name: ' + projCache['Name'])
        print('Notes: ' + projCache['Notes'])
        
    else:
        print(projectList[editIndex]['Notes'] + ' changed to ' + projCache['Notes'])

    #Below edits the temp project invocieable status             
    projCache['Invoiceable'] = ''
    while projCache['Invoiceable'] != 'Y' and projCache['Invoiceable'] != 'N': 
        projCache['Invoiceable'] = input('Invoiceable yet? (Y/N) ').upper()

    #Updates the main list file    
    projectList.remove(projectList[editIndex])
    projectList.append(projCache)
    with open('ProjectList.txt', 'w') as projectListFile:
        json.dump(projectList, projectListFile)

    mainMenu()

    

        
def addNewProject():
    newProject = {'Name': '', 'Notes': '', 'Invoiceable': '', 'Date Added': ''}
    newProject['Name'] = input('Project Name: ')
    newProject['Notes'] = input('Notes: ')
    while newProject['Invoiceable'] != 'Y' and newProject['Invoiceable'] != 'N': 
        newProject['Invoiceable'] = input('Invoiceable yet? (Y/N) ').upper()
    newProject['Date Added'] = time.ctime()
    projectList.append(newProject)
    with open('ProjectList.txt', 'w') as projectListFile:
        json.dump(projectList, projectListFile)
    print(newProject['Name'] + ' added to project list.\n')
    mainMenu()

def deleteProject():
    for i, n in enumerate(projectList):
        print(i, (projectList[i]['Name']))
    deleteIndex = int(input('\nProject Index to Delete: '))
    projectList.remove(projectList[deleteIndex])
    with open('ProjectList.txt', 'w') as projectListFile:
        json.dump(projectList, projectListFile)
    print('Removed successfully.\n')
    mainMenu()

    

    
mainMenu()
