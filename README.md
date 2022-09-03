# Recipe site

## UX
### Project Goals
Family recipes which are passed through the generations are special, yet are at risk of being lost forever due to the paper-based way they are kept. This site aims to be an alternative to this paper-based storage system and will keep family recipes safe for as long as the user wishes to store them. 

### User Goals
#### _Upload family recipes (Create)_
A user with family recipes would want an easy and simple way to upload their recipes to the site for safe storage. They would want to give data covering the fields of recipe name, the family member they recieved it from, the time it takes to make it, the number of servings, the ingredients, and the method. 

#### _Read their family recipes (Read)_
A user would also want to be able to see their family recipes in an easy and accessible way.

#### _Edit or update recipes (Update)_
A user may also want to update their recipes with improvements in an easy and accessible way.

#### _Delete recipes (Delete)_
Finally, a user may want to delete a recipe upload. 

### User stories
As someone with lots of family recipes I want:
* A safe space to store them in case my paper notes get damaged or destroyed
* To be able to edit my records in case I make a mistake or improvement
* To share which of my family members the recipe came from
* To be able to categorise my recipes by diet type, and to edit ot delete these.
* To see and record practical cooking information, for example serving size and the time it take to make something.
* To be able to easily navigate the site and to enjoy usuing it!

## Site feaures
### **Home / landing page**

![Screenshot of home page](family_recipes/static/images/home-page.png)

This acts as the landing page for a user entering the site. A responsive navbar is featured at the top, with a hero image and links to view recipes and manage categories. There is also a sticky footer on the page, showing the brand strapline and links to social media.
### **Recipies page**

![Screenshot of home page](family_recipes/static/images/recipes-page.png)

The part of the site shows the recipe cards that the user has created. Each card shows the recipe name, who made it (if applicable), time to make it, serving size, ingredients, method, and diet type. Also, each card has edit or delete buttons. 

### **Add recipes page**
![Screenshot of add recipe page](family_recipes/static/images/add-recipe.png)

The add recipe button on the recipe page leads to the add recipe page where the user can insert details on the recipe they wish to store.Clicking on the button at the bottom of this page redirects the user back to the recipe page, updated with their new recipe card. 

### **Edit recipes**
![Screenshot of edit recipe page](family_recipes/static/images/edit-recipe.png)

This is an important feature of the site. The user is able to edit recipes they have already created by clicking the 'edit' button. Once clicked, they are taken to a page that is pre-populated with the existing information of their recipe, which they can edit the information of. It is styled in the same way as the 'add recipe' page for good UX and intuitive design.

### **Diet page**
![Screenshot of add recipe page](family_recipes/static/images/diet-page.png)

This page features different food diets as categories. Again, the user is able to edit or delete these diet types, or add new ones.

### **Add diet page**
![Screenshot of add diet page](family_recipes/static/images/add-diet.png)

The add diet page is simple, and similar to the edit diet category page. Once the category is submitted successfully the user is redirected to the diets page where they can see all the diets, including their new one. 

### **Navbar and footer**

The navbar and footer is fully responsive. There is a collapsible mobile sidenav for smaller devices using the site.

### **Defensive programming**
![Screenshot of defensive programming model](family_recipes/static/images/defensive-modal.png)

Every delete button on every card has a defensive programming modal built in. When the user clicks 'delete', a modal box appears, asking the user to confirm if they do of don't want to delete the catagory. If they say yes, the box closes and the category is deleted. If they say no, the box is closed and the catergory remains untouched. 

### **Features left to implement**
- A user authentication system where multiple users could log in and use this site. 

## Design Choices

The developer wanted to make this site simple yet effective in providing CRUD functionality. The buttons are clear to see and clear in what they do, and it is easy for a user to navigate around the site. 

### Wireframes

Phone view

![Phone view design](family_recipes/static/images/phone-view.png)

Ipad view

![Ipad view design](family_recipes/static/images/ipad-view.png)

Desktop view

![Desktop view design](family_recipes/static/images/desktop-view.png)

### Images

The images are used minimally but effectively. Their use defines the 'main' pages of the site, where the users may spend most of their time. The developer chose not to use them on the add or edit pages so as not to overcrowd the deisgn. The images are in line with the theme of the page, being food-related.

### Font and colours

The standard Materialize CSS font, and Materialize CSS colour palette are used across the site. Care has been taken to keep the text and background colours contrasting well. 

## Testing

All internal and external navigation links have been tested on the site and on all pages. The form validation, the submit, and edit buttons have also been tested. The responsive design has also been tested using the Chrome Developer Tools. All HTML, CSS, JS, and Python files have been passed through code validators and errors have been fixed.

### **Manual - testing user stories**

*As someone with lots of family recipes I want:*
* A safe space to store them in case my paper notes get damaged or destroyed

The online site means recipes are safely stored, and defensive programming means users can't accidentally delete recipes.

* To be able to edit my records in case I make a mistake or improvement

All recipes and diet categories have the ability to be edited.

* To share which of my family members the recipe came from

When creating the recipes, there is an option to fill in who the recipe came from.

* To be able to categorise my recipes by diet type, and to edit ot delete these.

The Manage diets page stores the categories and lets the user edit or delete them. The categories are also visible when adding or editing recipes.

* To see and record practical cooking information, for example serving size and the time it take to make something.

This input option is avaiable when adding and editing recipes.

* To be able to easily navigate the site and to enjoy usuing it!

The navigation has been designed to be simple and intuitive. 

### **Bugs encountered**

A bug was encountered when editing the database schema. Changes to the scheme were not shwoing on the deployed site. After a while the fix was found during manually migrating the edited scheme across the flask. The developer had to intensively research how to do this.

## Technologies used
### **Languages**
- HTML5
- CSS3
- Javascript
- Python

### **Programmes, Libraries and Frameworks**
- *Balsamiq* to create wireframes for design concepts
- *Font Awesome* for icons on pages and in the footer
- *Git* for verson control
- *GitHub* to store the project after publication from GitPod
- *GitPod* to build the site
- *Materialize CSS* for styling, cards, interactive elements, and grid systems
- *Unsplash* for open-source images used in the site

## Deployment
### How to run this project locally

This project is deployed using Heroku. To deploy to Heroku, follow these steps:

1. In GitPod CLI in the root directoy of the project, run: `pip3 free --local > requirements.txt` to create a `requirements.txt` file.
2. In the Gitpod project's root directory, create a new file called Procfile. Open the Procfile, and inside this, check that `web: python3 app.py` has been added. Remove the blank line at the bottom of the file if that has been created.
3. Login to Heroku, select 'Create new app', add the desired name for your app and choose your closest region.
4. Navigate to the Deploy tab on Heroku dashboard and select Github. Search for your repository and when found, click 'connect'.
5. Navigate to the settings tab, click 'reveal config vars' and input the the following:

Key | Value
----|------
DATABASE_URL | postgres://fhyhmiptktzxqe:7415fc14a9cc743dee27b6058541206335aa172b3df8ae617e7aa28ee32ef55c@ec2-52-210-97-223.eu-west-1.compute.amazonaws.com:5432/dfqlb4s8fmmun0
IP | 0.0.0.0
PORT | 5000
SECTRET_KEY | a_secret_key

6. Return to the Deploy tab and select 'enable automatic deploys'
7. Click 'deploy branch'
8. Click 'Open app' after the build is completed

### Forking the GitHub repository

1. Log into GitHub and find the 'milestone-project-3' repository on the 'anniefenton' account.
2. At the top of the repository page, click on the 'fork' button. This will create a copy of the repository in your GitHub account. For more information follow this link.

### Cloning a repository

1. Log into GitHub and find the 'milestone-project-3' repository on the 'anniefenton' account.
2. At the top of the repository page, click on the 'Code' drop down button and copy the HTTPS URL that is displayed.
3. Open Git Bash.
4. Change the current working directory to the location where you want the cloned directory.
5. Type 'git clone' and paste the URL you copied in step 2.
6. Press enter. Your clone has been created. For more inforation, follow this link.

## Credits

### Media
The developer would like to thank Wasa Crispbread, Ella Olssen and Asterisk Kwon for their images used on the site which were accessed from Unsplash.

### Code
All code, except where credited to other developers, libraries, or frameworks, has been writted by the developer. Credits and URLs have been provided as comments in the HTML, CSS, and JS files.

### Acknowledgements

The developer would specially like to thank the Code Institute's tutor support team for their help and support! She would also like to thank her mentor for feedback and guidance.
