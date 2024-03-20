# Diggles Dog Spa Testing

[Return to the README](README.md)

- [Performance](#performance)
- [Accessibility](#accessibility)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#python-code-validation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
- [Browser Testing](#browser-testing)
- [Bugs & Fixes](#bugs-and-fixes)

## Performance

[Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance, accessibility, best practices and SEO of the website on mobile and desktop.

### Desktop

<details>
<summary>Home Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-home.png">
</details>

<br>

<details>
<summary>About Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-about.png">
</details>

<br>

<details>
<summary>Price List Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-pricelist.png">
</details>

<br>

<details>
<summary>My Account Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-myaccount.png">
</details>

<br>

<details>
<summary>Book A Service Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-booking.png">
</details>

<br>

<details>
<summary>Dashboard Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-dashboard.png">
</details>

<br>

<details>
<summary>Login Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-login.png">
</details>

<br>

<details>
<summary>Logout Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-logout.png">
</details>

<br>

<details>
<summary>Register Page</summary>
<img src="static/documentation/lighthouse_tests/desktop-register.png">
</details>

<br>

### Mobile

<details>
<summary>Home Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-home.png">
</details>

<br>

<details>
<summary>About Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-about.png">
</details>

<br>

<details>
<summary>Price List Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-pricelist.png">
</details>

<br>

<details>
<summary>My Account Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-myaccount.png">
</details>

<br>

<details>
<summary>Book A Service Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-booking.png">
</details>

<br>

<details>
<summary>Dashboard Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-dashboard.png">
</details>

<br>

<details>
<summary>Login Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-login.png">
</details>

<br>

<details>
<summary>Logout Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-logout.png">
</details>

<br>

<details>
<summary>Register Page</summary>
<img src="static/documentation/lighthouse_tests/mobile-register.png">
</details>

<br>

## Accessibility

The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website meets accessibility standards.

There are no errors on the WAVE tests:

<details>
<summary>Home Page</summary>
<img src="static/documentation/wave_tests/wave-home.png">
</details>

<br>

<details>
<summary>About Page</summary>
<img src="static/documentation/wave_tests/wave-about.png">
</details>

<br>

<details>
<summary>Price List Page</summary>
<img src="static/documentation/wave_tests/wave-pricelist.png">
</details>

<br>

<details>
<summary>Login Page</summary>
<img src="static/documentation/wave_tests/wave-login.png">
</details>

<br>

<details>
<summary>Logout Page</summary>
<img src="static/documentation/wave_tests/wave-logout.png">
</details>

<br>

<details>
<summary>Register Page</summary>
<img src="static/documentation/wave_tests/wave-register.png">
</details>

<br>

## Code Validation

### HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.

All the site pages were tested with no errors or warnings to show:

<details>
<summary>Home Page</summary>
<img src="static/documentation/html_tests/html-home.png">
</details>

<br>

<details>
<summary>About Page</summary>
<img src="static/documentation/html_tests/html-about.png">
</details>

<br>

<details>
<summary>Price List Page</summary>
<img src="static/documentation/html_tests/html-pricelist.png">
</details>

<br>

<details>
<summary>My Account Page</summary>
<img src="static/documentation/html_tests/html-myaccount.png">
</details>

<br>

<details>
<summary>Book A Service Page</summary>
<img src="static/documentation/html_tests/html-booking.png">
</details>

<br>

<details>
<summary>Dashboard Page</summary>
<img src="static/documentation/html_tests/html-dashboard.png">
</details>

<br>

<details>
<summary>Login Page</summary>
<img src="static/documentation/html_tests/html-login.png">
</details>

<br>

<details>
<summary>Logout Page</summary>
<img src="static/documentation/html_tests/html-logout.png">
</details>

<br>

<details>
<summary>Register Page</summary>
<img src="static/documentation/html_tests/html-signup.png">
</details>

<br>

### CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the `style.css` file used in the website.

<summary>CSS Validation</summary>
<img src="static/documentation/css_js_tests/css-validation.png">

<br>

### JS Validation

[JSHint](https://jshint.com/) was used to validate the one JavaScript function used in the website for automatically closing message alerts after 5 seconds. No errors were found in this function.

<summary>JS Validation</summary>
<img src="static/documentation/css_js_tests/js-validation.png">

<br>

### Python Code Validation (PEP8 Compliant)

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code used in this project:

<details>
<summary>admin.py</summary>
<img src="static/documentation/python_tests/admin-pep8.png">
</details>

<br>

<details>
<summary>apps.py</summary>
<img src="static/documentation/python_tests/apps-pep8.png">
</details>

<br>

<details>
<summary>forms.py</summary>
<img src="static/documentation/python_tests/forms-pep8.png">
</details>

<br>

<details>
<summary>models.py</summary>
<img src="static/documentation/python_tests/models-pep8.png">
</details>

<br>

<details>
<summary>urls.py</summary>
<img src="static/documentation/python_tests/urls-pep8.png">
</details>

<br>

<details>
<summary>views.py</summary>
<img src="static/documentation/python_tests/views-pep8.png">
</details>

<br>

## Testing

### Manual Testing

Behavior-driven development (BDD) is an Agile software development methodology in which an application is documented and designed around the behavior a user expects to experience when interacting with it. This process is used to test user stories in a non-technical way, allowing anyone to test the features of an app.

**EPIC: Site navigation and content**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 1A | As a site visitor I can view the site menu so that easily navigate through the site. | A visitor to the site can see a navigation bar in the header. The navbar has links to all the pages of the website. When clicking on the disered link the relevant page opens. Clicking on the title takes the user back to the homepage. When the site is viewed on smaller devices, a navbar toggler (burger menu) is displayed and when clicked, the site links drop down and take you to the desired page when clicked | :white_check_mark: |
| 1B | As a site visitor I can see the relevant information so that I can decide if I want to register for an account and become a customer. | For first time users who aren't registered, the home screen is displayed with a main image and a paragraph to obtain the visiors attention and shows the purpose of the site. The visitor can view the 'about' page with details about the dog spa and a list of sevices provided. There is a price List page which displays each service and a list of dog breeds in the size category. | :white_check_mark: |
| 1C | As a site visitor I can access different pages on the site so that I can smoothly navigate through the functionality of the site. | All the pages on the site can be clicked and taken to the desired page. Registered users have 2 extra links in the navbar whoch when logged in which takes them to their account page or to book a new service. the pages have been designed with good UX in mind. The pages are uncluttered and the content matches the link. | :white_check_mark: |
| 1D | As a customer I can view detailed information about each grooming service so that I can make a decision on what service I would like my dog to have. | The visitor can view the 'price list' page where each service is displayed as a seperate card with a button to click to view more information, when clicking this a modal appears with a description of the service, cost and duration. the user can then click to close the modal or click 'login to book' which will take them to the 'login' page with also a link to sign up if not registered. This page also displays a list of in their size category. | :white_check_mark: |
| 1E | As a site visitor I can click and view the sites social media so that I can view more information via social media. | The site visitor can click on the social media icons in the footer and that will take them to the selected social media website. | :white_check_mark: |

**EPIC: Registration and User Accounts**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 2A | As a customer I can create an account so that I can book my dog in for different grooming services. | Before a user is logged in, the 'register' link is displayed in the navbar. Click this link which takes the user to the sign up form, fill in the required details and click 'sign up' this then creates a new user account. The new customer now sees the 'my account' 'book a service' and 'logout' links in the navbar. | :white_check_mark: |
| 2B | As a customer I can use my created account information so that I can log into my account and access my information. | For a logged out or unregistered user, they will see 'login' link in the navbar, click this link, click 'sign in' fill in the registered details, click 'sign in' again and the user wil be taken straight to there 'my account' page. On the 'sign in' page there is also a link to 'sign up' if the user isnt registered, click this and the user is taken to the sign-up page. | :white_check_mark: |
| 2C | As a customer I can log out of my account so that my personal information is protected. | A logged in user will see the 'Logout' link in the navbar, click this link, a confirmation box appears, click 'sign out' to confirm sign out or click 'cancel' to be taken to the home page but remained logged in. | :white_check_mark: |

**EPIC: Manage Bookings**
| ID | User Story | Action/Expected Results | Pass |
| -- | ---------- | ----------------------- | ---- |
| 3A | As an authenticated user I can book a grooming service for my dog so that my dog can receive professional grooming care. | Click 'Book a Service' as a logged in user, fill in the fields, pick a service from the drop down, pick a date, pick a time from the drop down, 'click submit'.confirmationmessage appears confirming booking success. User is then directed to their account page,new booking is displayed withbooking details with a pending status and edit and cancel booking buttons. | :white_check_mark: |
| 3B | As an authenticated user I can cancel a booking so that The booking is cancelled if we can no longer make it. | On the my account page where the upcoming bookings are displayed, click 'cancel appointment'a model appears to confirm or cancel the cancellation, click 'yes cancel' confirmation message is displayed confirming cancellation and the booking is removed from upcoming bookings section and from the django admin panel. | :white_check_mark: |
| 3C | As an authenticated user I can edit my booking so that I can make amendments if I create a booking with a mistake. | On the my account page where the upcoming bookings are displayed, click 'edit appointment' the edit booking form is displayed, change the required fields, click 'save changes' confirmation message is displayed confirming the changes, booking is pending approval. | :white_check_mark: |
| 3D | As a customer I can go straight to the booking page if I see a service I like so that I don't have to close the service card and navigate to another page. | From the price list page, click 'click here for more info' on a service card, this displays the service description, cost and duration, click the 'book now' button to be taken to the 'book a service' page. | :white_check_mark: |
| 3E | As a Developer I need to have validation on bookings so that we don't end up with double bookings. | Try booking at the same date and time as another booking that has been made as another user, booking form clears and red error message stating 'This appointment slot is already booked. Please choose a different time.' is displayed, check user account and admin panel to ensure booking hasn't been made.| :white_check_mark: |
| 3F | As a Developer I need to have validation on bookings so that users can't accidentally book appointments on past dates. | Try and make a booking with a date in the past, message in red appears stating 'You cannot book appointments for dates that have already passed.' booking form clears, check user account and admin panel to ensure booking hasn't been made. :white_check_mark: |

