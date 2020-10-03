# Django Demo

##### This document is under development

#### Never make a Django Repository public. The secret key will be made public which is serious security risk.

### STEPS:
(In windows powershell is recommended)
1. Create virtual environment and activate it.

2. (Optional)For windows: If the prompt if too long shorten it by writing the function. (This is temporary. If you close and open the powershell the original prompt will be shown):

		Function prompt {"$"} 

    *Add space at the end and hit enter. In place of `$` you can keep anything.

3. Install django

		python -m pip intall django

4. Requirements file

		pip freeze > requirements.txt

5. Start a django project with the following command (Only `_` underscore is allowed in the project name.):

    	Syntax: django-admin startproject <website_name>

			django-admin startproject Demo_Website

6. A directory is created with the name `Demo_Website`. Navigate to that directory. Inside that directory initially we will have a python file named `manage.py` and a directory with the same name.

    6-a. The python file `manage.py` is the main file that is used for running the django applicaton.

    6-b. The directory's primary use is to connect the other applications that you are going to create for the web application. We can develop applications (example a blog, a chatroom) and connect all of them to the main web application by modifying the files and contents here. This is like the main directory that points to all different web applications inside a website. It consists of 5 files:

         __init__.py ==> 

         asgi.py ==> 

         settings.py ==> 

         urls.py ==> contains url patterns to specify what view should be displayed based on the given url.

         wsgi.py ==> 

7. Create an application (like a blog or main page for the website)

    	Syntax: python manage.py startapp <application_name>

			py manage.py startapp home

8. A new directory is created again with the name `home`. It contains one directory and 6 files. These are for configuring the application `home`.

		__init__.py ==> 

		admin.py ==> This file is used to register the models that were created for the application.

		apps.py ==> 

		models.py ==> Every application is based on the models in the Django. It is like creating and mapping to a database table.

		tests.py ==> 

		views.py ==> 

		/migrations ==> All the created models for the application must be migrated and these migrations are stored in this directory

9. Run the server to check if the web application is working fine or not.

		py manage.py runserver

10. If running successfully then continue. Otherwise, start from beginning by deleting everything. Make sure that you have two terminals opened. One for server and other for executing the scripts that are being modified. Keep the server running always.

11. Inside the newly created `home` directory and create a file named `urls.py` (OR) copy and paste that file from the `Demo_Website` directory. 

12. Open the `urls.py` file located in the `Demo_Website` directory and edit like this:

		from django.contrib import admin 
		# importing include
		from django.urls import path, include

		# Adding path to the urls that will be created in the 
		# "urls.py" file located in the "home" directory.
		urlpatterns = [
			path('', include('home.urls')),
			path('admin/', admin.site.urls),
		]
		# when you visit home page the urls written in the 
		# "home" directory file will be executed

13. Open the `urls.py` file located in the `home` directory and edit like this:

		from django.urls import path
		# from current directory importing view
		# Relative import
		from . import views

		# useful when creating custom URLS (in future)
		app_name = "home"

		urlpatterns = [
			path("", views.homepage, name="homepage"),
		]

14. Open `views.py` from `home` directory to create `homepage` function. The file looks like this:

		from django.shortcuts import render
		from django.http import HttpResponse

		# Create your views here.

		# passing a request to the view
		def homepage(request):
			return HttpResponse("Hello World!")

15. Refresh the homepage and check the results. If it is okay continue. Otherwise go to step 11 and do it again.

16. Open `models.py` to create a model. We use a class to create models. It look like this:

		from django.db import models

		# Create your models here.
		# Creating a database table with name "Product" and adding columns

		class Product(models.Model):
			product_title = models.CharField(max_length=200)
			product_content = models.TextField()
			product_added = models.DateTimeField("date added")

		# overriding the __str__ method to return the product title instead of an object
			def __str__(self):
				return self.product_title

17. The changes that are done will not be effected in the applications. Because, when a new application is created we are giving the urls to go to it. But, we did not actually install it. Every time we create a new application we have to add it to the `INSTALLED APPS` list in the `settings.py` in the `Demo_Website` directory. After, adding it to the list the list should like this:

		INSTALLED_APPS = [
			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'home.apps.HomeConfig',
		]

    17-a: The last line that is added will be found when we navigate to the `home` directory and open `apps.py`. We can find the `HomeConfig` function there. It looks like this:

		from django.apps import AppConfig

		class HomeConfig(AppConfig):
			name = 'home'

18. Everytime you modify models file (create a table or modify its columns-add or delete or update columns) you have to migrate them in Django. It is a two step process. Navigate to the `Demo_Website` directory (where `manage.py` file is located) and do run these commands:

    18-a: To see the migrations that are to be done if any. All the boxes should be checked (like ==> [X]). If at least one is without that mark you should do the '18-b' and '18-c' steps.

		python manage.py showmigrations

	18-b: You have to make the migrations.

		python manage.py makemigrations

	*When you navigate to the `migratios` directory you can see the generated migrations and their configurations with a number for each generation. To see what and how the table is created in the database (to see the SQL query) you can see it like this:

		python manage.py sqlmigrate home 0001

	*Since, it is out first generation we get only one generation and it will have '0001'.

    18-c: You have to migrate the migrations.

		python manage.py migrate

19. This step is optional. Instead of using a template to add the data into the database we can use the django's interactive shell. It is easy and fast. To open the shell run command 

		python manage.py shell

	19-a. To add data into the table:

	    # import the Model
	    from home.models import Product
	    # Retrieve all the data from the table
	    Product.objects.all()
	    # importing timezone to add date time
	    from django.utils import timezone
	    # the parameters names must be same as in the product model
	    new_product = Product(product_title='Product 1', product_content='Product 1 Content', product_added=timezone.now())
	    # now we need to save the insertion in the database
	    new_product.save()
	    # Retrieve all the data from the table
	    Product.objects.all()
	    # exit the shell
	    exit()

20. Now we have to create a super user to use the django's admin page. The steps are as follows:

		python manage.py createsuperuser

    *Username and email address can be edited later on. For practice use simple passwords. But, for production use a strong password since it is a password for the ADMIN page where you can edit the whole database.

21. Now go to `localhost:8000/admin` (OR) `127.0.0.1:8000/admin` in the web browser to open the Admin page and login with the super user credentials.

22. You can find your credentials under the `Users` section. You can see your details there (except for password-it will be hashed). You can edit details in that page.

23. But the models or the database is not shown there because we haven't registered it. So to register the models open the `admin.py` file located inside the `home` directory. Register the newly created model. It should look like this:

		from django.contrib import admin
		# Relative import the model here
		from .models import Product

		# Register your models here.
		admin.site.register(Product)

    *Refresh the admin page now. You should see the model.

24. Do not mind the name in the webpage which is plural (Products) but you have registed singular (Product). There is an in-built function that does this. We can override it if we want later.

25. We can add or update or delete the products in the database using this in-built template. We can modify this template by adding a custom class during the registration of the models. We can also change the order of displaying the database items. After modifying the "admin.py" it looks like this:

		from django.contrib import admin
		from .models import Product

		# Register your models here.

		class ProductDisplay(admin.ModelAdmin):
		# the order of displaying the items can be changed here
		# can also change what items to show and not to show
			fields = [
				"product_title",
				"product_content",
				"product_added"
			]

		admin.site.register(Product, ProductDisplay)

26. We can also set fieldsets (like showing items in sections - title and data one set, content another set) by using fieldsets variable instead of fields variable. Replace fields variable with following variable:

		fieldsets = [
			("Title/Date", {"fields": ["product_title", "product_added"]}),
			("Content", {"fields": ["product_content"]})
			]

27. We can have default values for the fields like getting the current time for adding a product by default instead of giving it manually in the template. This can be done by adding a paramenter called `default` to the `DateTimeField` in the `product_added` in the models of the home page. Remember step-18. On modifying the model we have to start the migration again. Sometimes it might not be necessary. But doing migrations is always a good practice to avoid unapplied migrations erros. The table will be altered only on migrating. On modifying the model it looks like this:

		from django.db import models
		from datetime import datetime

		# Create your models here.

		class Product(models.Model):
			product_title = models.CharField(max_length=200)
			product_content = models.TextField()
			product_added = models.DateTimeField("date added", default=datetime.now())

			def __str__(self):
				return self.product_title

    *Now, do the migration process.

28. In the `home` directory create a directory named `templates` to store the html templates. Inside that directory create another directory called `home` to store the html pages that are to be rendered for the home page. Navigate to the directory and create a html page named "home.html" and add the following line.

		<h2>Hello! This is Home Page</h2>

    *The creation of extra directories inside the `templates` is recommended because Django looks in all of the templates directories available in the `Demo_Website`. It means when we call a template for rendering the Django looks for that template in all the created `applications`. We may have few files with same names but in different applications. To avoid such complexity (for Django) in choosing the template it is highly recommended to create extra directories inside templated for each application.

    *The same principle applies to the files css and javascript files.

29. Now we to update the `views.py` inside `home` `application directory` to display the created html page. It looks like this:

		from django.shortcuts import render
		from django.http import HttpResponse
		from .models import Product

		# Create your views here.

		# passing a request to the view
		def homepage(request):
			return render(
				request=request,
				template_name="home/home.html",
				context={"products": Product.objects.all}
			)

		'''
		   1. The "request" parameter is necessary to catch the request objects that are passed to the html page. This will be used later. But, keep it for now.

		   2. The "template_name" parameter gets the template name that has to be rendered. It searches for the template inside the "templates" directory of the current application.

		   3. The "context" parameter is used to pass data to the rendered template. Here we are passing all the items in the products table.
		'''

30. Now for editing the `home.html` template to display the products on the home page we use Django Template Language (DTL) which is alternative to the Jinja2 Template which is used in Flask. It looks like this:

		{% for pd in products %}
			<p>{{ pd.product_title }}</p>
			<p>{{ pd.product_added }}</p>
			<p>{{ pd.product_content }}</p>
			<br/>
		{% endfor %}

31. Alongside `templates` directory create a directory named `static` and then create `home` directory inside it and then create `css` directory inside it and create the file `styles.css`

32. Before importing css in the template add the following lines in the created css file:
	
		*{
		  margin: 0;
		  padding: 0;
		}

		p{
		 color: blue;
		}

33. Modify the `home.html` like this:

		<head>
			{% load static %}
			<link rel="stylesheet" href="{% static 'home/css/styles.css' %}"/>
		</head>

		<body>
			{% for pd in products %}
				<p>{{ pd.product_title }}</p>
				<p>{{ pd.product_added }}</p>
				<p>{{ pd.product_content }}</p>
				<br/>
			{% endfor %}
		</body>
	
    *The static folder must be loaded before using it. After modifying the html file restart the server (stop and start).

34. The css or javascript files and some headings (like title) or navigation bar are common for most of the html pages in an application. So rather than copy and pasting the `importing` lines for every html file we can write those lines in a separate html file and import that one file in every html file in that application with one or few lines of code.

35. Alongside `home.html` create a directory named `bases` and create a html file named `header.html` and add the lines:

		<head>
			{% load static %}
			<link rel="stylesheet" href="{% static 'home/css/styles.css' %}"/>
		</head>
		<body>
			{% block content %}

			{% endblock %}
		</body>

    *The `block content` is the block where the code is dynamically added and executed from the file in which the `header.html` is imported.

36. Modify the `home.html` like this:

		{% extends 'home/bases/header.html' %}

		{% block content %}
			{% for pd in products %}
				<p>{{ pd.product_title }}</p>
				<p>{{ pd.product_added }}</p>
				<p>{{ pd.product_content }}</p>
				<br/>
			{% endfor %}
		{% endblock %}

    *The `block content` in the `header.html` file is replaced by the body tag and it's content in the `home.html` file. Refresh the home page. It should work fine. If not restart the server (OR) do the steps again carefully.

37. We use bootstrap to give styling for the pages. Now the `header.html` looks like this.

		<head>
			{% load static %}
			<link rel="stylesheet" href="{% static 'home/css/styles.css' %}"/>

			<!-- Bootstrap CDN -->
			<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

		</head>

		<body>
			<nav class="navbar navbar-expand-lg navbar-light bg-light">
				<div class="collapse navbar-collapse" id="navbarSupportedContent">
						<ul class="navbar-nav mr-auto">
							<li class="nav-item active">
								<a class="nav-link" href="/">Home</a>
							</li>
							<li class="nav-item">
								<a class="nav-link" href="/register">Register</a>
						</li>
							<li class="nav-item">
								<a class="nav-link" href="/login">Login</a>
						</li>
						</ul>
				</div>
			</nav>
			<br/>
			{% block content %}

			{% endblock %}
		</body>

    *Refresh the page.

38. Now we need to add the views for registering the users, login and others. Create `register.html` alongside `home.html` and add the lines here:

		{% extends 'home/bases/header.html' %}

		{% block content %}
			<form method='POST'>
				{% csrf_token %}
				{{ form.as_p }}
			</form>
		{% endblock %}

    *The `csrf_token` is essential for providing security. Do google to know more about it. Django provides a in-built or pre-created user registration form. We will use it in the views.
    *The `form.ap_p` shows every element with a paragraph tag.

39. Now add a function named register in the "views.py" in the "home" directory and also import the "UserCreationForm" from "django.contrib.auth.forms". Add the following lines at appropriate places:

		# importing
		from django.contrib.auth.forms import UserCreationForm

		# register function
		def register(request):
			form = UserCreationForm
			return render(request,
							template_name="home/register.html",
							context={"form": form}
				   )

40. Now add the following list item in `urlpatterns` in the `urls.py` inside `home` directory.

		path("register/", views.register, name="register"),

    *Always keep forward slash '/' at the end of the name in the url 

41. Refresh and go to register. The form doesn't look nice because we have used Bootstrap and it rewrites all the css. If you want to modify you can. We still need to add button and the register behaviour.

42. Add a button after the `{{ form }}` in `register.html` like this:

		<button class="btn btn-primary" values="submit">Regsiter</button>

    *The styling of the button is done by bootstrap

43. Now modifying the view to get the data by clicking the register button. It looks like this:
	
		# imported redirect along with render
		from django.shortcuts import render, redirect
		# new import
		from django.contrib.auth import login, logout, authenticate

		# modified register
		def register(request):
			if request.method == 'POST':
				form = UserCreationForm(request.POST)
				if form.is_valid():
					user = form.save()
					login(request, user)
					return redirect("home:homepage")
				else:
					for msg in form.error_messages:
						print(form.error_messages[msg])

			form = UserCreationForm
			return render(request,
							  template_name="home/register.html",
							  context={"form": form}
						 )

    *Same usernames must not be given. Passwords can be duplicated. To check your entered passwords if you are stuck:
	
		print(request.POST['password1'])
        print(request.POST['password2'])

    *Passwords can be printed to the server console and also username. Also check users in admin page so that you find a way to register.

44. Adding messages to show the register to the user. We use bootstrap template. Before the block content and after the navigation bar paste the following code:

		{% if messages %}
			{% for msg in messages %}
				<div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-delay=4000>
					<div class="toast-header">
							<strong class="mr-auto">{{ msg.tags|upper }}</strong>
					</div>
					<div class="toast-body">
							{{ msg }}
					</div>
				</div>
				<script>
					$('.toast').toast('show');
				</script>
			{% endfor %}
		{% endif %}

    *jhgkjdj

45. Update the `views.py` as follows:
	
		# Add the import statement
		from django.contrib import messages

		# Update the request function
		def register(request):
			if request.method == 'POST':
				form = UserCreationForm(request.POST)
				if form.is_valid():
					user = form.save()
					username = form.cleaned_data.get('username')
					messages.success(request, f"New account created {username}")
					login(request, user)
					return redirect("home:homepage")
				else:
					for msg in form.error_messages:
						messages.error(request, f"{msg}: {form.error_messages[msg]")

			form = UserCreationForm
			return render(request,
							template_name="home/register.html",
							context={"form": form}
					 )

    *dlg dfh hfgh

46. Add user authentication logic in the navigation bar. Update the navigation bar as below:

		<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav mr-auto">
				{% if user.is_authenticated %}
						<li class="nav-item">
							<a class="nav-link" href="#">{{ user.username }}</a>
					</li>
					<li class="nav-item">
							<a class="nav-link" href="/logout">Logout</a>
					</li>
				{% else %}
					<li class="nav-item">
							<a class="nav-link" href="/register">Register</a>
					</li>
						<li class="nav-item">
							<a class="nav-link" href="/login">Login</a>
					</li>
				{% endif %}
				</ul>
		</div>

    *No need to update the `views.py`. It is already modified previously. 

47. Since header file became large lets split that. Making `navbar.html` and `message.html` for navigation bar and messages respectively. Cut and paste from `<nav>` tag to `</nav>` tag from `header.html` into `navbar.html`. In the `header.html` in place of the removed code write the following line:

		{% include "home/bases/navbar.html" %}

    *Likewise, cut and paste the toast code from the header file into the message file.

48. Now adding the logout. Open `urls.py` in the `home` directory and add the url pattern as below:

		path("logout/", views.logout_the_user, name="logout"),

    *Add the logout function in the `views.py` in the same directory as below:

		def logout_the_user(request):
			logout(request)
			messages.info(request, "You logged out!!!")
			return redirect("home:homepage")

49. Now adding the login functionality.	Add the url pattern in `urls.py` file.

		# new url pattern
		path("login/", views.login_the_user, name="login"),

		# Modified import. Import the Django user Login template
		from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

		# login view
		def login_the_user(request):
			if request.method == 'POST':
				form = AuthenticationForm(request, data=request.POST)
				if form.is_valid():
					username = form.cleaned_data('username')
					password = form.cleaned_data('password')
					user = authenticate(request, username=username, password=password)
					if user is not None:
						login(request, user)
						messages.success(request, f"You are logged in as {username}")
						return redirect("home:homepage")
					else:
						for msg in form.error_messages:
							messages.error(request, f"{msg}: {form.error_messages[msg]}")
				else:
					for msg in form.error_messages:
						messages.error(request, f"{msg}: {form.error_messages[msg]}")

			form = AuthenticationForm()
			return render(request,
							"home/login.html",
							{"form": form}
						   )

    *Now the `login.html`:

		{% extends 'home/bases/header.html' %}

		{% block content %}
			<form method='POST'>
				{% csrf_token %}
				{{ form.as_p }}
				<button class="btn btn-primary" values="submit">Login</button>
			</form>
		{% endblock %}

50. Let's start building some real stuff. Using the bootstrap to get the pre-built templates to change the home page. Modifying css to this:

		*{
		 margin: 0;
		 padding: 0;
		}

		.bd-placeholder-img {
				font-size: 1.125rem;
				text-anchor: middle;
				-webkit-user-select: none;
				-moz-user-select: none;
				-ms-user-select: none;
				user-select: none;
		}

		@media (min-width: 768px) {
				.bd-placeholder-img-lg {
				  font-size: 3.5rem;
			}
		}

    *Modifying the homepage to this:

		{% extends 'home/bases/header.html' %}

		{% block content %}
			<div class="album py-5 bg-light">
				<div class="container">
				<div class="row">
			  {% if products|length > 0 %}
					{% for pd in products %}
					  <div class="col-md-4">
						  <div class="card mb-4 shadow-sm">

							  <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
					  <title>{{ pd.product_title }}</title>
					  <rect width="100%" height="100%" fill="#55595c"/>
					  <text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text>
					  </svg>

						  <div class="card-body">
					  <p class="card-text">
						<strong>{{ pd.product_title }}</strong>
					  </p>
								  <p class="card-text">{{ pd.product_content }}</p>
								  <p class="card-text">(INR) <strong>Rs. Price</strong></p>
						  <div class="d-flex justify-content-between align-items-center">
						  <div class="btn-group">
							  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
						  </div>
						  <small class="text-muted">{{ pd.product_added }}</small>
						  </div>
					  </div>
				  </div>
				  </div>
						{% endfor %}
			  {% else %}
				<h2>Sorry! No products to show</h2>
			  {% endif %}
			</div>
			</div>
		</div>
		{% endblock %}

    *The kjhjs hdug	

51. The products can only be added by the admin. Now, let's update the product model (table) so that the admin can have add thumbnail, title, content, price and a link. Before updating, delete the products and refresh the homepage. Also, install `Pillow` module to work with Images (Required). The updated `models.py` in the home directory looks like this:

		# updated product view
		class Product(models.Model):
			product_thumbnail = models.ImageField(blank=True, upload_to='products_images/', max_length=500)
			product_title = models.CharField(max_length=200)
			product_content = models.TextField()
			product_price = models.IntegerField(default=0)
			product_url = models.URLField(blank=True, max_length=250)
			product_added = models.DateTimeField("date added", default=datetime.now())

		# updated fieldsets variable in admin view
		fieldsets = [
			("Title/Date", {"fields": ["product_title", "product_added"]}),
			("Content", {"fields": ["product_content", "product_thumbnail",
									"product_url",
									"product_price"]
						 })
			]
	
    *Repeat step-18. Go to admin page and add the products. THejfl dgjbsdgj

52. Update the `settings.py` to work with images like this:

		# new import statement
		import os

		# new lines
		MEDIA_URL = '/media/'
		MEDIA_ROOT = os.path.join(BASE_DIR, 'home/media')

		*Update the "urls.py" from the "home" directory as below:

		#new import statements
		from django.conf import settings
		from django.conf.urls.static import static

		# Add this to the urlpatterns
		+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

		*Replace the homepage <svg> tag with the following tags:

		{% if not pd.product_thumbnail %}
			<svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
				<title>{{ pd.product_title }}</title>
				<rect width="100%" height="100%" fill="#55595c"/>
				<text x="50%" y="50%" fill="#eceeef" dy=".3em">Picture not available!</text>
			</svg>
		{% else %}
			<center>
				<img src="{{ pd.product_thumbnail.url }}" alt="{{ pd.product_title }} Picture" width="50%"/>
			</center>
		{% endif %}

    *Thelr ;lkjjg jdg

53. Update the `home.html` to work with the urls as below:

	*Replace the view button with this code:

		{% if pd.product_url %}
			<button type="button" class="btn btn-sm btn-outline-secondary" onclick="urlFun('{{ pd.product_url }}')">View</button>
		{% else %}
			<button type="button" class="btn btn-sm btn-outline-secondary" onclick="urlFun('empty')">View</button>
		{% endif %}

	*Add the following script in the bottom after the last div tag and before "{% endblock %}":
	
		<script>
			function urlFun(url) {
				if (!("empty".localeCompare(url))) {
					alert("Sorry! no URL is found!");
				}
				else {
					var element = document.createElement('a');
						element.style.display = 'none';
						element.setAttribute('href', url);
						element.setAttribute('target', '_blank');
						document.body.appendChild(element);
					element.click();
				}
			}
		</script>

    *Tel ksheg khjddf db d df 
