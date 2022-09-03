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
### Home / landing page

![Screenshot of home page](family_recipes/static/images/home-page.png)

This acts as the landing page for a user entering the site. A responsive navbar is featured at the top, with a hero image and links to view recipes and manage categories. There is also a sticky footer on the page, showing the brand strapline and links to social media.
### Recipies page

![Screenshot of home page](family_recipes/static/images/recipes-page.png)

The part of the site shows the recipe cards that the user has created. Each card shows the recipe name, who made it (if applicable), time to make it, serving size, ingredients, method, and diet type. Also, each card has edit or delete buttons. 

### Add recipes page
![Screenshot of add recipe page](family_recipes/static/images/add-recipe.png)

The add recipe button on the recipe page leads to the add recipe page where the user can insert details on the recipe they wish to store.Clicking on the button at the bottom of this page redirects the user back to the recipe page, updated with their new recipe card. 

### Edit recipes
![Screenshot of edit recipe page](family_recipes/static/images/edit-recipe.png)

This is an important feature of the site. The user is able to edit recipes they have already created by clicking the 'edit' button. Once clicked, they are taken to a page that is pre-populated with the existing information of their recipe, which they can edit the information of. It is styled in the same way as the 'add recipe' page for good UX and intuitive design.

### Diet page
![Screenshot of add recipe page](family_recipes/static/images/diet-page.png)

This page features different food diets as categories. Again, the user is able to edit or delete these diet types, or add new ones.

### Add diet page
![Screenshot of add diet page](family_recipes/static/images/add-diet.png)

The add diet page is simple, and similar to the edit diet category page. Once the category is submitted successfully the user is redirected to the diets page where they can see all the diets, including their new one. 

### Navbar and footer

The navbar and footer is fully responsive. There is a collapsible mobile sidenav for smaller devices using the site.

### Defensive programming
![Screenshot of defensive programming model](family_recipes/static/images/defensive-modal.png)

Every delete button on every card has a defensive programming modal built in. When the user clicks 'delete', a modal box appears, asking the user to confirm if they do of don't want to delete the catagory. If they say yes, the box closes and the category is deleted. If they say no, the box is closed and the catergory remains untouched. 

##

Credits: Home image - Wasa Crispbread

