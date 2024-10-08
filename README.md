# A simple web application to display blogs
This project was made to advance my understanding of how Django works. This is an application that lets person upload articles as blog post to a webiste.
- The simple frontend is built with [Bootstrap 5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/).
- The theme is from [Bootswatch](https://bootswatch.com/). 
- The Django forms made better using [django crispy forms](https://pypi.org/project/django-crispy-forms/). 
- Text editor for blog posting made using [tinyMCE](https://django-tinymce.readthedocs.io/en/latest/installation.html).

## How this works
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
- This is the home page. It displays a list of the already uploaded articles
- Click on read more to open a detailed view of the post
- You can scroll to see more posts

![django gif](https://github.com/user-attachments/assets/b8c7c496-fa97-47b8-b217-5fb4b3541567)


**Authentication**
- Navigation bar contains buttons to sign up and sign in
- A user can sign in to post blogs. and the you will be able to Like posts
- Sign up to make a new admin account locally**

![sign in and out](https://github.com/user-attachments/assets/03bbfef3-343c-4f89-8748-0ba593dea823)


**Django admin page**
Navigate to django admin page. Put this in the web address ```http://127.0.0.1:8000/admin``` and this page should appear

To upload another article on the site, click on the article button and an editing interface will appear.
- Ability to put a title to the post
- Full fledged text editor to modify your article content
- Option to make any article a featured article
- assinging author
- See likes from other authors

![article upload](https://github.com/user-attachments/assets/c119acf9-2086-41de-b366-2595651507a9)
