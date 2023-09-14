# Project Name - Address-Manager
<br><img src="assets/images/">

## View Live Project
* [Link to Deployed Project](https:)

## Contents
* [User Experience (UX)](#user-experience)
    *  [Purpose & target audience](#purpose-and-target-audience)
    *  [User Story](#user-story)
    *  [Goals](#goals)

* [Design](#design)
  * [Wireframes](#wireframes)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [](#)
  * [Planned features](#planned-features)
* [Logic](#logic)
* [Validation](#validation)
* [Technology](#technology)
* [Modules & Libraries](#modules-libraries)
* [Deployment](#deployment)
* [Testing](#testing)
  * [Tests performed](#tests-performed)
  * [User Story Tests](#user-story-tests)
  * [Bugs resolved](#bugs-resolved)
  * [Unresolved bugs](#unresolved-bugs)
  * [Improvements & future developments](#improvements-and-future-developments)
* [Forking & Cloning Instructions](#forking-cloning-instructions)
* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## User Experience

### Purpose and Target Audience
   * Address_Manager is a simple contacts storing system, safely backed up and updated to a google worksheet.
   * The app is made for everyone to add, find, update and view contacts information, including name, contact number and address.

### User Story
   * The user is presented with an attractive intuitive command-line admin portal, navigating through various menu choices.
   * The user can choose to add a contact.
   * The user can choose to find a contact.
   * The user can choose to update a contact.
   * The user can choose to delete a contact.
   * The user can choose to view contacts in the app.
   * The user can find contact by name (first, last or full name).
   * The app will display all the contacts with similar name (first, last or full name) with all information included.
   * The user is notified when the information has been updated after each a certain action.
   * The user is notified in case of an invalid character/data entered, and will prompt the user to enter the information correctly.

### Goals
   * The app must be simple and clear to use by anyone, with very little or no training required.
   * The data displayed should be relevant to each menu item selected.
   * The program should find, update, add or delete the given input from a Google worksheet via API calls.
   * The user should easily be able to exit a menu.
   * The user must be well informed if an entry or selection is invalid.

## Design
* The design is a simple terminal application that uses Python as the building langugae.  The Code Institute mock terminal template was used.

* The initial concept and the logic behind the program's menu was created using Lucid chart.
* Only desktop was considered.  The mock terminal is not suitable for mobile.

### Lucid chart  (created in [](https://))
<br>
Main Menu 
<br>
<br><img src="assets/images/">
<br>
<br>
Add a Contact Menu Flow and Logic
<br>
<br><img src="assets/images/">
<br>
<br>
Find a Contact Flow and Logic
<br>
<br><img src="assets/images/">
<br>
<br>
Update Contact Flow and Logic
<br>
<br><img src="assets/images/">
<br>
<br>
Delete Contact Flow and Logic
<br>
 <br><img src="assets/images/">
<br>
<br>
Display Contacts Flow and Logic
<br>
<br><img src="assets/images/">
<br>
<br>

## Color Scheme (created in [](https://))

### Main Background
   * The app uses no background image
   * It was downloaded from.
   <br><img src="assets/images/">

### Terminal Colors
   * In the terminal multiple font colors were chosen:
   * White for Menu items and headers
   * Green for successfully getting the results from the user query
   <br><img src="assets/images/color green output">
   <br>
   <br>
   * Purple for displaying results from the user queries such as: contact information, updated contact information.
   <br>
   <br><img src="assets/images/purple color output">
   <br>
   <br>
   * Red for errors
   <br><img src="assets/images/red color output">
   <br>
   <br>
   

### Typography
   * The main text font is the default font in the command line terminal.
   * Font chosen for the title = 
   * For the body including the start button = 

### MVP
   * A simple yet fully functionable app was created to add, find, update, delete and display contacts to anyone who looks for a contact in the system 
   * It also checks for any invalid errors and handles them according for the program to keep running wihtout causing any problem to the user.

### Planned features
   * The initial plan waas to have a simple address manager with options to add, find and display contacts.
   * 


## Validation
* Various validation messages were used to ensure that the user was notified correctly of any incorrect input and to ensure the program would not crash.
<br><img src="assets/images">
<br>

## Technology
* The following tools and technology were used to complete this project:
* [Balsamiq](https://) - wireframes
* [Canva](https://) - graphic design
* [Lucid](https://) - logic chart
* [Google Cloud Service Accounts & API](https://cloud.google.com)
* HTML - landing page
* CSS - landing page
* Python - terminal application
* GitHub - version control
* GitPod - IDE
* [Heroku](https://www.heroku.com/)
* [HTML Validator](https://validator.w3.org/nu)
* [CSS Validator](https://jigsaw.w3.org/css-validator)
* [PEP-8 Validator](https://pep8ci.herokuapp.com/)

## Modules & Libraries
* The following libraries were imported to run the application:
* gspread - for Google worksheet API
* ASCI - for displaying fontin different colors

## Deployment
* The following steps were taken to deploy this site:
* The project was initially set up in GitHub using Code Institute's project template
* A Google worksheet was created to store the data
* An API was setup through [Google Cloud](https://cloud.google.com)
* A JSON key was created from the Service Account and copied into the repo as creds.json
* The creds.json file was added to git ignore
* The email address in the creds.json file was shared with the Google Worksheet
* gspread was installed by typing "pip3 install gspread google-auth" in the terminal
* The live site was deployed to Heroku early on so the final UX could be experienced early and often, using the following steps:
* [Login to Heroku (create an account if needed)](https://id.heroku.com/login)
* Create New App - choosing a unique name
* Under Settings / Config Vars enter the PORT in the KEY section as 8000
* Add buildpacks: Python and then Node.js - in that order
<br>
<br><img src="assets/images/">
<br>
* Under Deploy - select GitHub and link to repo name
* Under Manual Deployment, click Deploy Branch
<br>
<br><img src="assets/images/">
<br>

## Testing
* Extensive testing was carried out on the site which can be viewed here:
* [Tests]()

### Bugs resolved:
  *

### Unresolved bugs:
  * During testing on the Mock Terminal,

### Improvements and Future Developments:
  * 

## Forking & Cloning Instructions
* To create a copy of the repo in GitHub to edit:
1. Log in to your GitHub account.
2. Navigate to [address_manager repository](https://github.com/)
3. Click on the "Fork" button located in the upper right-hand corner of the repository's page.
4. Select the account where you want to fork the repository.
5. Wait for GitHub to complete the forking process.
6. Open the project in GitPod (or whichever IDE you have setup)

* To clone a copy of the repo on your local machine to edit:
1. Log in to your GitHub account.
2. Navigate to [address_manager](https://github.com/)
3. Click on the "Code" button located in the upper right-hand corner of the repository's page.
4. Click on the "HTTPS" link to copy the URL of the repository.
5. Open the terminal or command prompt on your local machine and navigate to the directory where you want to clone the repository.
6. Type the following command, replacing the "repository_URL" with the URL of the repository that you copied in step 4: git clone repository_URL.
7. Press Enter and wait for the cloning process to complete.

## Credits:
### Code
  * All the code was written and developed entirely for this project.
  * YouTube Videos, Stack Overflow, Google Search and ChatGPT were used to clarify functions, PEP-8 requirements and docstring formats.

### Content
  

### Media
  * The media used for the landing page background is royalty-free. The design was created specifically for this project.

### Acknowledgements
  * Medale Oluwafemi for your mentorship.
  * Code Institute's Love Sandwiches project for the Google API
  * Inspiration from  []()
  * Inspiration from  []()
  