# Diggles Dog Spa

Developer: Chris Diggle

![Mockup image](/static/images/amiresponsive.png)

- [Live Site](https://diggles-dog-spa-4e32378de2f2.herokuapp.com/)
- [GitHub Repo](https://github.com/chrisdiggle1/diggles-dog-spa)

## Table of Content

- [Diggles Dog Spa](#diggles-dog-spa)
  - [Table of Content](#table-of-content)
  - [Introduction](#introduction)
    - [Project Goals](#project-goals)
    - [Data Base Design (ERD)](#data-base-design-(erd))
  - [User Experience - UX](#user-experience-ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [Agile Development](#agile-development)
  - [Current Features](#current-features)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Python Packages](#python-packages)
    - [Frameworks & Tools](#frameworks--tools)
  - [Testing and Validation](#testing-and-validation)
  - [Deployment & Development](#deployment--development)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)

## Introduction

Welcome to Diggles Dog Spa, a fictitious luxury grooming and spa service created for my 4th Code Institute project. Diggles Dog Spa is designed to provide an exceptional pampering experience for dogs of all sizes and breeds. Our website serves as the primary platform for dog owners to explore our wide range of services, book and edit appointments, and stay updated with the latest in canine care and luxury grooming.

The project was designed as the 4th portfolio project of the Code Institutes Full Stack Diploma Program. It was built using Django, Python, JS, CSS, and HTML. The data is stored in a PostgreSQL database created by Code Insitute.

### Project Goals

The goal of the project was to build a webiste for dog owners to effortlessly book, edit and cancel appointments through a user-friendly interface ensuring a seamless experience for dog owners. For an administrator I have built a dashboard for approving or rejecting bookings, as well as adding and removing new services to the site to keep the spa's offerings current and responsive to clients needs. I want the project to provide exceptional service management and a pleasant experience for dog owners and site administrators.

### Data Base Design (ERD)

The The Entity Relationship Diagram (ERD) illustrates the structure of the database which lies at the core of the functionality of the site:

![ERD](/static/documentation/erd.png)

## User Experience - UX

### Strategy

#### Target Audience

The target audience is for dog owners seeking an easy and effeicient way to book there their dog in for grooming appointments. This is for customers looking for a hassle-free online experience to access a variety of grroming treatments, from basic hygiene maintenance to luxurious pampering sessions for their dogs. The customers appreciate the ability to create a persoanl account form managing appointments and tracking their dog's grooming history. Our service is designed for those who see their pets as family members and are committed to their well-being and appearence.

| EPIC                       | ID  | User Story |
| -------------------------- | --- | -----------|
| **CONTENT AND NAVIGATION** |     |            |
|                            | 1A  | As a site visitor I can view the site menu so that easily navigate through the site. |
|                            | 1B  | As a site visitor I can see the relevant information so that I can decide if I want to register for an account and become a customer. |
|                            | 1C  | As a site visitor I can access different pages on the site so that I can smoothly navigate through the functionality of the site. |
|                            | 1D  | As a customer I can view detailed information about each grooming service so that I can make a decision on what service I would like my dog to have. |
|                            | 1E  | As a site visitor I can click and view the sites social media so that I can view more information via social media. |
| **REGISTRATION AND USER ACCOUNTS** |     |            |
|                            | 2A  | As a customer I can create an account so that I can book my dog in for different grooming services. |
|                            | 2B  | As a customer I can use my created account information so that I can log into my account and access my information. |
|                            | 2C  | As a customer I can log out of my account so that my personal information is protected. |
| **MANAGING BOOKINGS**      |     |           |
|                            | 3A  | As an authenticated user I can book a grooming service for my dog so that my dog can receive professional grooming care. |
|                            | 3B  | As an authenticated user I can cancel a booking so that The booking is cancelled if we can no longer make it. |
|                            | 3C  | As an authenticated user I can edit my booking so that I can make amendments if I create a booking with a mistake. |
|                            | 3D  | As a customer I can go straight to the booking page if I see a service I like so that I don't have to close the service card and navigate to another page. |
|                            | 3E  | As a Developer I need to have validation on bookings so that we don't end up with double bookings. |
|                            | 3F  | As a Developer I need to have validation on bookings so that users can't accidentally book appointments on past dates. |
| **ADMIN CAPABILITIES**     |     |           |
|                            | 4A  | As an admin I can view, confirm, and cancel bookings so that I can manage the grooming schedule efficiently. |
|                            | 4B  | As an admin I can add a new grooming service to the website so that customers have a variety of options to choose from. |
|                            | 4C  | As an admin I can remove a grooming service from the website if we decide a service is longer required. |

### Scope

#### Simple and Intuitive User Experience

- Ensure the navigation bar is straightforward, allowing easy access to all services offered, including grooming packages and booking appointments. Ensure it functions correctly on all devices.

- Align page titles with their content, such as "Our Services," "Booking," "About Us," and "Contact."

- Ensure the user gets visual feedback when navigating through the site's functionalities, such as confirmation messages on bookings and successful login and logouts.

- Design the site so it matches the intent of the page. Use a colour scheme and imagery to display a sense of luxury and comfort.

#### Relevant Content

- Display information about the sites purpose to make its intent clear to the user.

#### Core Website Functionality

- Enable users to register an account, log in, and log out to manage their profiles and view booking details.

- Implement an intuitive booking form for grooming appointments, allowing users to choose services, select dates/times, and provide pet details.

- Allow users to view, edit, or cancel their appointments through their user account page.

#### Responsiveness

- Ensure the website is reposonsive across desktops, tablets and mobile devices for greater User Experience.

### Structure

### Skeleton

#### Wireframes

[Balsamiq Wireframes](https://balsamiq.com/) was used to created the below wireframes for mobile and desktop devices.

<details>
<summary>Home Page</summary>
<img src="static/documentation/wireframe-homepage.png">
</details>

<br>

<details>
<summary>Create Account</summary>
<img src="static/documentation/wireframe-create-account.png">
</details>

<br>

<details>
<summary>Sign In</summary>
<img src="static/documentation/wireframe-sign-in.png">
</details>

<br>

<details>
<summary>Book Your Pups Cut</summary>
<img src="static/documentation/wireframe-book-a-cut.png">
</details>

### Surface

#### Color Scheme and Fonts

- Me and my children have chosen the below colours for the website:

  - #F1DAC4 (a creamy beige)
  - #A69CAC (a soft lavender)
  - #474973 (a deep navy)

<summary>Colour Pallette</summary>
<img src="static/documentation/colour-pallette.png">

<br>

The beige makes the site feel warm and inviting, the lavender adds a hint of luxury, and the navy brings a serious, dependable feel. Together, these colors make the site look and feel cozy yet professional, perfect for Diggles dog spa.


### Font
madimi one has been used as the font throughout the website.

<img src="static/documentation/font.png">

## Agile Development

The development of this project was managed through GitHub issues and projects and the work was done in sprints. Story points were used a way to judge how long a user story may take to complete. Story points are recorded using labels attached to the user story.

In order to judge story points the following user story was used as the base guide and given a value of 2 story points as this is a short task and something I am familiar with. I set myself 40 story points for each week:

`USER STORY 1C: Site Pagination` accesing all the different pages the site has to offer and navigate through the functionality of the site.

### Sprints

- Sprint 1

  - Setup CI template
  - Create user story template
  - Install packages
  - Create the project and app
  - setup database
  - Create base.html and navbar
  - Create footer with social media links

- Sprint 2

  - Create booking and services models
  - Create the pages used for the site
  - Install django allauth
  - Register an account
  - View available services
  - Create a booking
  - Cancel a booking
  - Edit a booking

- Sprint 3

  - Prevent Double bookings
  - Prevent bookings on past dates
  - Create custom 403 page
  - Create custom 404 page
  - Create custom 500 page

- Sprint 4

  - Create Admin Dashboard
  - Admin to be able to approve/reject bookings from the dashboard
  - Admin to be able to add/ remove services from the dashboard.
  - Testing
  - Readme
  - Submission

<br>

I created additional labels for my 'project issues' and assigned these to the relevant user stories..

<details>
<summary>GitHub Labels</summary>
<img src="static/documentation/labels.png">
</details>

<br>

<details>
<summary>GitHub Issues</summary>
<img src="static/documentation/GitHub Issues.png">
</details>

<br>

Epics were identified across the various user stories, MoSCoW prioritisation was utilised throughout the project and each issue was assigned both an epic label and MoSCoW label (must have, should have, could have). As issues were completed, each was moved from To Do --> In Progress and finally --> Done on the KanBan board.

<details>
<summary>GitHub Projects</summary>
<img src="static/documentation/GitHub Projects.png">
</details>

## Current Features

### Header and Navigation

Navbar with logo, website name, and links to all pages. On small to medium screens the navigation links are displayed as a burger menu with the links to other pages dropping down.

<details>
<summary>Desktop navbar for unregistered/logged out users</summary>
<img src="static/documentation/features/nav-desktop1.png">
</details>

<br>

<details>
<summary>Desktop navbar for registered/logged in users</summary>
<img src="static/documentation/features/nav-desktop2.png">
</details>

<br>

<details>
<summary>Desktop navbar for site administrators - Have a link to admin dashboard.</summary>
<img src="static/documentation/features/nav-desktop3.png">
</details>

<br>

<details>
<summary>Navbar display on mobile devices</summary>
<img src="static/documentation/features/navbar-mobile.png">
</details>

<br>

<details>
<summary>Navbar expanded on mobile devices</summary>
<img src="static/documentation/features/nav-mobile2.png">
</details>

### Footer

<details>
<summary>Footer displaying social media icons as clickable links and copyright feature.</summary>
<img src="static/documentation/features/footer.png">
</details>

### Site pages

<details>
<summary>Home Page</summary>
<img src="static/documentation/features/home-desktop.png">
</details>

<br>

<details>
<summary>About Page</summary>
<img src="static/documentation/features/about.png">
</details>

<br>

<details>
<summary>Price List Page</summary>
<img src="static/documentation/features/price-list.png">
</details>

<br>

<details>
<summary>Register Page</summary>
<img src="static/documentation/features/reigster.png">
</details>

<br>

<details>
<summary>Login Page</summary>
<img src="static/documentation/features/login.png">
</details>

<br>

<details>
<summary>My Account Page</summary>
<img src="static/documentation/features/myaccount.png">
</details>

<br>

<details>
<summary>Book A Service Page</summary>
<img src="static/documentation/features/book-service.png">
</details>

<br>

<details>
<summary>Admin Dashboard - Bookings and Pending Approvals</summary>
<img src="static/documentation/features/dashboard1.png">
</details>

<br>

<details>
<summary>Admin Dashboard - Services</summary>
<img src="static/documentation/features/dashboard2.png">
</details>

<br>

<details>
<summary>Add New Service Form</summary>
<img src="static/documentation/features/service-form.png">
</details>

<br>

<details>
<summary>Logout</summary>
<img src="static/documentation/features/logout.png">
</details>

<br>

<details>
<summary>Custom 403</summary>
<img src="static/documentation/features/403-error.png">
</details>

<br>

<details>
<summary>Custom 404</summary>
<img src="static/documentation/features/404-error.png">
</details>

<br>

<details>
<summary>Custom 500</summary>
<img src="static/documentation/features/500-error.png">
</details>


### Success Messages

Each time a user out a function on the website, either as part of the account functionality or the CRUD functionality, a success message will be displayed confirming that the function was carried out successfully and also error messages if the user tries to book appointments in the past or double book.

<img src="static/documentation/features/signin-mess.png">

<img src="static/documentation/features/signout-mess.png">

<img src="static/documentation/features/book-success.png">

<img src="static/documentation/features/book-cancel.png">

<img src="static/documentation/features/edit-booking.png">

<img src="static/documentation/features/double-booking.png">

<img src="static/documentation/features/past-dates.png">


## Future Features

- Password reset option to allow the user to retrieve/reset their password if they have lost/forgotten it is also quite important and should be added for a more complete user experience.
- Automated emails for both admin and user when a new booking is requested and the user to be informed if the booking is approved or rejected.
- Capability to login with socal media accounts.
- Message on the booking card stating why the booking is rejected.
- Review features for the website
- The user to have the ability to delete their own account.

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Python Packages

- django - high-level Python web framework used to develop this application/site.
- psycopg2 - PostgreSQL database adapter for the Python programming language.
- dj3-cloudinary-storage - facilitates integration with Cloudinary by implementing Django Storage API.
- django-allauth - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- django-crispy-forms - provides a crispy filter and {% crispy %} tag that allows control of the rendering behavior of Django forms in a very elegant and DRY way.
- crispy-boostrap5 - Bootstrap5 template pack for django-crispy-forms.

### Frameworks & Tools

- Git - used for version control
- GitHub - used to host the source code of the website.
- Django - used to set up the back-logic and both custom models on the website.
- Gitpod -used to write and develop the code for the website, and for committing and pushing code to GitHub.
- Heroku - used to deploy the website
- Cloudinary - used to store the website media
- Bootstrap - used throughout the site for responsiveness, layout, and predefined style elements.
- Balsamiq - used to create the project wireframes.
- Lucid Chart - used for creating the ERD.
- Google Fonts - used to import fonts for the website.


## Testing and Validation

All the testing documentation can be found at [TESTING.md](TESTING.md)

## Deployment & Development

### Deploy on Heroku

**Requirements and Procfile Files**

Before deployment on Heroku, two files need to be created and be up to date, a `requirements.txt` file and a `Procfile`.

- The `requirements.txt` file is created by executing the following command in the terminal window: ` pip3 freeze --local > requirements.txt`. A file with all requirements will be created.
- Then create a file named `Procfile` and insert the following code: `web: gunicorn digglesdogspa.wsgi`, with no empty lines after it.
- Then make sure to push these files to your repository.

**Creating A New Heroku App**

- Log into Heroku your Heroku and go to the Dashboard.
- Click "New" and then select "Create new app".
- Give your app a name and select the region closest to you.
- Click "Create app" to confirm.

**PostgreSQL**

The database for this site was created using [Code Institutes Postgres Database Creator](https://dbs.ci-dbs.net/)

**The env.py file**

- If you do not have a `env.py` file in your workspace create one and make sure it is included in the `.gitignore` file.
- At the top of the `env.py` file add the line: `import os`.
- Below that add the following two lines:

  `os.environ["DATABASE_URL"] = "<copied URL from SQL database>"` 
  `os.environ["SECRET_KEY"] = "<create a secret key of your own>"` 

- If you are using Cloudinary storage also add the following line:

  `os.environ["CLOUDINARY_URL"] = "<copied URL from Cloudinary account>"`

- Make sure the environment variables are imported correctly into the `settings.py` file.
- Run `python manage.py migrate` in the terminal window to migrate the data structure to the database instance.

**Setting Environment Variables**

- On the Heroku Dashboard select the app you just created, select the "Settings" tab.
- Click "Reveal Config Vars"
- Add the following config vars:

  `DATABASE_URL` - copy the database URL emailed from the Code Institute when creating the Postgres database in here, it should also be in the `env.py` file.
  `SECRET_KEY` - copy your secret key in here, should also be in env.py file.

**Connecting to GitHub and Deploy**

- On the Heroku Dashboard select the app you just created and then select the "Deploy" tab.
- Select GitHub for the deployment method.
- Search for the name of your project repository and click "Connect".
- Select "Deploy Branch" and watch the app being built and you can view the build logs.

### Forking the Repository

- Log in to GitHub and locate the GitHub repository you want to fork.
- At the top of the Repository above the "Settings" Tab on the menu, locate the "Fork" Button and click it.
- You will have a copy of the original repository in your GitHub account.
- You will now be able to make changes to the new version and keep the original safe.

### Making a Local Clone

- Log into GitHub and locate the repository you want to clone.
- Click the 'Code' dropdown above the file list.
- Copy the URL for the repository.
- Open Git Bash in your IDE.
- Change the current working directory to the location where you want the cloned directory.
- Type `git clone` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  `$ git clone https://github.com/`
- Press Enter to create your local clone.

## Credits

### Media

- The image for the homepage was purchased from [iStock](https://www.istockphoto.com/sign-in?returnurl=%2Faccount%2Fdownload%2Findividual%2Fcredits) - Credit: Eriklam.

- The 2 images on the about page were taken from [pexels](https://www.pexels.com/search/dog%20groomer/).

- The site logo and favicon was taken from [pngegg](https://www.pngegg.com/).

### Code

- The Code Institutes I Think Therefore I Blog' Django walkthrough project was followed for the initial set up and getting started with the code.

- The following sites were used frequently for guidance and troubleshooting:

  - [Django Documentation](https://docs.djangoproject.com/en/4.2/)
  - [Stack Overflow](https://stackoverflow.com/)
  - [W3 Schools](https://www.w3schools.com/)

- [Bootstrap documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

- [Ultimate Django Course](https://codewithmosh.com/p/the-ultimate-django-part1) - part of my code with mosh subscription.

## Acknowledgements

- First of all, I would like to show my appreciation for my employee for giving me a chance as a junior developer. The last 7 months I have been in the role I have learnt so much and far quicker than I would if I was just studyingg in my own time.

- Which leads me onto my fellow developers who help and answer any questions I have. Having access to other devs all day everyday has been unreal for my learning.

- My wife Kirsty for her support during this and all the other projects, taking the kids out so I can study in peace, bringing regular coffee to keep me going and telling me to take a break when I struggled with an issue.

- My kids for wanting to be part of the project and choosing the colours and picking out the images on the site, also for being good as gold and letting me do my studies without much hassle.

- My Mentor Greame Taylor for his guidance, tips, support and feedback during this project.

- The Slack community for when you need help, a laugh or to help somebody else out.