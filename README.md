# TO-DO LIST
#### Demo: [Demo](https://todo-app-theta-green-74.vercel.app/)
#### Description:
This project allows the user to add, view, edit tasks they have to complete or delete tasks they have completed in a list.

The project was created using the following technologies:

- **[HTML](#templates)**
- **[CSS](#css)**
- **[BOOTSTRAP](#bootstrap)**
- **[JAVASCRIPT](#js)**
- **[PYTHON](#apppy)**
- **[FLASK](#apppy)**
- **[SQLITE](https://sqlitecloud.io/)**

Let's take a look at each folders and files included in the project.

## STATIC
There are **3** folders in the **static** folder. **CSS**, **IMAGES**, and **JS**.

### CSS
The **css** folder contains a file called styles.css.
This file styles all parts of the project. For example, the navigation bar, titles, navigation links, text fields, buttons, dropdown menus, divs, image, and select options on the pages.

It also contains styles that makes the app responsive across devices like mobiles, tablets, and desktops.

#### BOOTSTRAP

Below is a list of elements I've styled using bootstrap:

- **Navigation Bar**
- **Text Fields**
- **Buttons**
- **Multiple Select**
- **Dropdown menu**
- **Labels**
- **Unordered Lists**
- **Divs**
- **Links**
- **Main**

### IMAGES
This folder contains only **1** image. The image is used on the [error](#errorhtml) page.

### JS
The last folder in the **static** folder is the **js** folder. This folder contains 1 file called **script.js**. Let's take a closer look at this file.

Inside this file, the first line of code waits for the page to load and then executes all the codes inside the block of the event listener.

There's a lot of stuff happening inside this block, so let's see what's going on in detail.

The first part in this file check which page the user is currently visiting, and set an active style on the navlink to indicate the page the user is currently on.

For example, if the user is on the home page, then set an active style on the navlink called "Home".

The active style changes the color of the navlink.

The second part prevent the user from exceeding the maximum number of characters which is 50.

This will apply for all text fields that are present in the project.

If the user exceeding that number, this will display a message inside a div telling the user that the maximum number of characters has been reached and prevent the user from typing more characters.

Else, if the number of characters is less than 50, then the div containing the message will disappear.

The next part is for the edit page. There is a dropdown menu on the edit page that allows the user to select an item from the list and then edit that item.

So, when the user click on an item in the dropdown menu, we take the id of the item that has been clicked, and pass it to a hidden input which will be submitted with the form so that on the backend side, the server knows which item to edit.

> **In order to get the id of the item, an id attribute has been added on each item and the value of the attribute is equal to the id of the item in the database.**

That's what this line of code is doing.

The final part displays a message in a div everytime the user add, delete, or edit an item and then disappear after 3 seconds.

## TEMPLATES
The templates folder contains **5** html files. **[layout.html](#layouthtml)**, **[index.html](#indexhtml)**, **[delete.html](#deletehtml)**, **[edit.html](#edithtml)**, and **[error.html](#errorhtml)**. Those are the files that are rendered when the user request to see the "Home", "Delete" or "Edit" page. The "error.html" page is rendered only if an error occured. Refer to the **[ERROR.HTML](#errorhtml)** section for more information about the error page.

### LAYOUT.HTML
Take a look at the html boilerplate below:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title></title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="" />
</head>
<body>
</body>
</html>
```
Let's say for example we want to create 4 html pages.
We will have to include this boilerplate everytime we create an html page.

Using **Jinja**, an extensible templating engine, we create an html file called **layout.html** and put this boilerplate inside.

Then, if we want to create another html page, for example, called **index.html**, all we have to do is put this inside our **layout.html**:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{% block title %} {% endblock %}</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="" />
</head>
<body>
  {% block body %}

  {endblock}
</body>
</html>

```

and this inside the **index.html**:

```
{% extends "layout.html" %}

{% block title %}
  YOUR TITLE HERE
{% endblock %}

{% block body %}
  YOUR CONTENT HERE
{% endblock %}

```

That's how the **layout.html** is being used.

But, it also contains the navigation bar, project title, and navigation links too.

### INDEX.HTML
This is where the user can add things they have to do in the list. The first div in this file contains a message that will appear everytime the user add, delete, or edit an item.

Inside the second div, there's a form with a text field and submit button allowing the user to add an item to the list.

There's also another div inside that div containing a message that will pop up if the maximum number of characters has been reached.

The final div holds a title that says "Items" and the list itself.

### DELETE.HTML
On this page, the user can delete one or more items. There's a multiple select tag that allows the user to select one or more items they want to delete.

There's also a div containing texts that tells the user they can select one or more items to delete.

### EDIT.HTML
This one holds a dropdown menu as well as a text field. From the dropdown menu, the user can select an item they want to edit.

After selecting an item, the user must type something in the text field to edit the selected item.

It also have a div that contains a message alerting the user if the maximum number of characters has been reached.

### ERROR.HTML
This one is rather short because it only displays this error page if:

- **On the Home page and the user leaves the text field empty and click on the ADD button**

- **On the Delete page and does'n select any item and click on the DELETE button**

- **On Edit page and user doesn't select an item from the dropdown menu or user leaves the text field empty and click on the EDIT button**

The page contains an image and a text telling the user that they must provide an item and an another text that says "Error".

## APP.PY
The **app.py** file contains **python** codes. I have imported some libraries. The libraries used are:

- **flask**
- **secrets**
- **pathlib**
- **cs50**

Let's see how they are used.

First, in order to make the **TO-DO** app a flask application, I used a function that comes from the **flask** library called **`FLASK`** and passed in the name of the file (**app.py**). Here's an example: **`FLASK(__name__)`**.

Then a connection to the todo_lists database was made by using another function from the **cs50** library called **`SQL`** and here's how to connect to the database: **`SQL("sqlite:///todo_lists.db")`**.

Next, I used the **`PATH`** function from the **pathlib** library to locate a file called **secret_key**. This file stores a secret key that allows the app to run correctly.

Then, try to read the **secret_key** file and set the **secret key** of the project equals to the secret key found in the **secret_key** file.

If the **secret_key** is not found, then, create a **secret_key** file and generate a **secret_key** using the **secrets** library and set the **secret_key** of the project equals to the newly generated **secret_key**.

After that, put the newly generated **secret_key** in the newly created **secret_key** file.

Next, we have **3** routes that handles what should happen when the user lands on the **Home**, **Delete**, **Edit**, or the **Error** page.

Let's start with the "**/**" route. First, I created a variable to store the maximum number of characters allowed.

### / Route
The next line of code checks if it's a **POST** request meaning if the user submitted a form on the Home page, if it's the case, then check if the user provided something in the text field.

If the user didn't, then,  I used the **`render_template`** function from the **flask** library to render the **error.html** page.

But if they provided something in the text field, then, add the item the user provided to the todo_lists **sqlite** database.

And then, call a functiion called **`flash`** from the **flask** library to display a message to the user letting them know that the item has been added to the list.

The user will then be redirected to the **"Home"** page using the **`redirect`** function from the **flask** library. This is where the user will be able to see the message mentioned above and the list containing all the items.

Now if it's a **GET** request, there will be only **2** lines of code that will simply fetch all the items from the database and the **maximum number of characters**' value mentioned above and pass it to the **`render_template`** and render the index.html page to the user.

### /delete Route
Next is the **/delete** route. In this route, it's kind of similar to the **/** route except that there's no **maximum number of characters** variable created here and instead of inserting into the database, we will simply remove from it.

Also instead of having a text field to type something,on the delete page, the user will have to select one or more item from a multiple select option to delete.

So instead of checking if the text field is empty and then render the **error.html** page, here it's going to check if the user selected something. If not, then display the **error.html** page.

Then, take what the user selected and then delete it from the database.

After the item or items has been deleted from the database, there's also a little conditional check to see if the number of items the user selected is equal to 1 or greater than 1.

This is just to display the word **"Item"** in either singular or plural. For example if the user selected only 1 item, then the message they will see is going to be: **"Item Deleted!"**. But if they selected for example 2 items, then it's going to be: **"Items Deleted!"**.

Then redirect the user to the **Home** page where they will see the message mentioned above and a list without the item or items they selected.

Now, if it's a **GET** request, same as **"/"** route, fetch all the items from the database and pass it to the **`render_template`**. Except this time, there's no need to pass the **maximum number of characters**' value to the **`render_template`** function. Then, redirect the user to the **"Home"** page.

### /edit Route
This one is similar to the **"/"** route. Except that the **"/edit"** route has **2** input.

One is a dropdown menu (Not really an input element) but it allows the user to select an item they want to edit and the second one is a text field in which the user has to type the text they want to replace the old one with.

These **2** inputs will also have a check to see if they are empty or not. And if one or the other or both are empty, render the **error.html** page.

But if the user provided something for both inputs, then the next line of code will simply **update the the value of the selected item** and set it equals to the **value provided in the text field**.

After that, redirect the user to the **"Home"** page where they will see a message saying that the item they selected has been edited.

Finally, if it is a **GET** request, then fetch all the items from the database and pass both the items and the **maximum number of characters**' value to the **`render_template`** so that when the user open the dropdown menu, they will be able to see all the items present in the list. As for the **maximum number of characters**' value, when the user exceed the maximum number of characters allowed (which is 50), the following message will appear: "Maximum number of characters reached (1 - 50 characters allowed)". The value of the **maximum number of characters** variable is going to be passed in the message.

## REQUIREMENTS.TXT
This file only contains libraries installed in this project. It included libraries I installed as well as libraries that comes with other libraries too.
