# JiraIssueReporter
## Good example project for working with JIRA REST API by using Python where GUI is provided with Tkinter

## Project Description
With this project, the issues for the specific project documented in Atlassian Jira can be printed out. 

## User Guide
1. When the project is run, login window appears. Here, the member who has an access to the specific project can enter his or her details.
   After clicking ACCESS button, all those issues and corresponding details regarding to them in the specific project will be printed out

## Some Technical Description
Here, I created a basic authentification for Jira Site using member's API token and Jira login username. By connecting to Jira Rest API, 
I got Json format of issues in the specific project. Finally, I converted the JSON format into more readable form and print it
