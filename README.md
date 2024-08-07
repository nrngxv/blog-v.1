# A simple web application to display blogs
This project was made to advance my understanding of how Django works. This is an application that lets person upload articles as blog post to a webiste.
- The simple frontend is built with [Bootstrap 5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/).
- The theme is from [Bootswatch](https://bootswatch.com/). 
- The Django forms made better using [django crispy forms](https://pypi.org/project/django-crispy-forms/). 
- Text editor for blog posting made using [tinyMCE](https://django-tinymce.readthedocs.io/en/latest/installation.html).

## How this works
-- THE PROGRAM RUNS COMPLETELY LOCALLY --

First check if you are on the latest version of python or not. Run this in your terminal
```
python --version
```
It should say Python 3.11.4

Next, Clone this GitHub respository:
```
git clone https://github.com/nrngxv/blogsite.git
```

Next, cd into the directory where the git is cloned, and run this command
```
python manage.py runserver
```
This will start the server.

Next, go to this web address ```http://127.0.0.1:8000/``` and you will see the home page for the application

## Explanation of the interface
**This is the home page. It displays a list of the already uploaded articles.**
![Screenshot 2024-08-07 151258](https://github.com/user-attachments/assets/3d2450eb-7333-4be2-8a5f-4ff7c8dfd131)

**Click on read more to open a detailed view of the post**
![image](https://github.com/user-attachments/assets/00533118-3096-4134-9a13-5cdf38e39536)

You can scroll to see more posts

**Authentication**
**Navigation bar contains buttons to sign up and sign in.**
![image](https://github.com/user-attachments/assets/ed6f8a49-087b-4d4d-9fe6-ddd8f1abb0d0)

**A user can sign in to post blogs. and the you will be able to Like posts.**
![image](https://github.com/user-attachments/assets/29051ec2-d690-418f-97e0-dff0041f26ff)

**Sign up to make a new admin account locally**
![image](https://github.com/user-attachments/assets/7f24b421-ba41-4f31-ac94-947661bb537f)


**Django admin page**
Navigate to django admin page. Put this in the web address ```http://127.0.0.1:8000/admin``` and this page should appear

To upload another article on the site, click on the article button and an editing interface will appear.
- Ability to put a title to the post
- Full fledged text editor to modify your article content
- Option to make any article a featured article
- assinging author
- See likes from other authors
