## Contents

- [User Story Testing](#user-story-testing)
- [Validator testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)

- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)

- [Manual Testing](#manual-testing)
    - [Landing page](#landing-page)
    - [Navigation](#navigation)
    - [Sign up form](#sign-up-form)
    - [Login form](#login-form)
    - [Create Inventory](#create-inventory)
    - [Add Items to inventory](#add-items-to-inventory)
    - [Dashboard](#dashboard)
    - [Saved inventory list](#saved-inventory-list)
    - [Categories](#categories)
    - [Contact Form](#contact-form)
    - [Logout](#log-out)
    - [Footer](#footer)


- [Automated Testing](#python-automated-testing)
- [Bugs](#bugs)




## User Story Testing

### User Profile

**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site User, I can create an account so that I can start managing my inventories.| Sign up page exists, with a form where the user can fill out the required fields and submit the form.| ✅
|As a Site user, I can verify my account via the verification link sent to my email upon registration.| The user will recieve a verification link to email used when signing up. When clicked on link user can confirm email address and then login.| ✅
|As a Site User, I can login to my account so that I can access my existing inventories.| Login page exists, where user can enter username and password to login and user will login to the dashboard.| ✅
|As a Site User, I can login via Google so that I have several login options.| A google button in the login page exists, which allows the user to login using Google. The user will login to the dashboard.| ✅

### User Navigation

**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site User I can navigate easily through the site due to a responsive navbar so that I understand where to go and it is always visible to me.| The navigation bar is responsive by using Bootstrap and on small screens a hamburger dropdown is displayed. The logo takes user back to landing page/dashboard.| ✅
|As a Site User, I can see my lists in a dropdown list from the navigation bar, so that I can navigate to my lists easily.| When a logged in user creates and saves an inventory list, the list is automatically added to the dropdown menu.| ✅
|As a Site User I can click on the social media links so that I can explore the work of the developer and see the developers profile.| User can click on the the social media icons, LinkedIn and Github that will open in a new tab.| ✅


### User Feedback
**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site User, I can receive feedback whenever I make an action, so that I know if my action was successful or not.| The user will see a success message whenever an action is successful. If not, an error message will display telling the user about the errror. The messages are self-closing.| ✅

### Create Inventories

**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site User, I can create unique inventory lists so that I can't create inventory lists with the same name.| If the user tries to create an inventory list with a name that already exists, the user will get a self-closing error message.|  ✅
|As a Site User, I can create an inventory list and add multiple items at once, so that I can organize my belongings efficiently.| Inventory form where the list name and category exists and when saved, let's user add multiple items at once. User can also edit and delete the items.| ✅

### Manage Inventories

**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site User, I can generate a QR code for my inventory so that I can identify my belongings easily.| The QR-code image associated with the inventory will be generated when the inventory list is saved and displayed on the dashboard.|  ✅
|As a Site User, I can scan the QR code so that I can see my inventory list immediately.| As the list owner I can see the items in the list and edit and/or delete the list when the QR-code is scanned. When shared, the edit and delete buttons will not be visible.| ✅
|As a Site User, I can share my inventory with others using the generated QR code so that I can provide a visual and efficient view of the contents of my Inventory to others.| A "Share" link exists where user can share the QR-code via email with a pre-populated message and the url-link inlcuded| ✅
|As a Site User I can clone my lists so that I can reuse a list and just modify it.| A "Clone list" button exists where user can clone a lists with its items and also add more items, delete or edit.| ✅
|As a Site User, I can see numbers next to the inventory list name so that I can find boxes with an qr code easily if I have many boxes.| When the user creates and saves a list, a number, starting from 1 is automatically added next to the list name| ✅



### Contact Form
**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site User, I can make contact through a contact form, so that I can ask questions, report issues or make suggestions.| A contact form exists, where the user can submit a message. A succes message will display when sent.|✅


### Site Administration

**User Story**|**Test**|**Result**
:------|:------|:----:
|As a Site owner I can log in to the admin dashboard using my username and password so that I can access the functionalities of the superuser.| Created a superuser, using Django AllAuth to acces the admin panel.| ✅
|As a Site owner I can view a list of all inventory items so that I can edit, delete or add items, inventories and categories.| The models are registred in the admin panel which allows admin to add new items and add, edit, delete items/inventories/categories.| ✅
|As a Site Owner I can download the QR codes for each inventory so that I can share the QR codes with team members.| The QR-code URL field is included in the admin panel so admin can access the QR-code url.| ✅
|As a Site owner I can receive messages submitted through the form so that I can respond to the messages.| Functionality in place so the user gets an automated email confirming that the message has been recieved and admin gets the user's submitted message to the email.|✅




## Validator Testing
### HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/) by pasting the source code of each page directly
into the validator. The results are listed in below table.



| Page                  | Result       |
|---------------------- |--------------|
| base.html             | No errors    |
| categories.html       | No errors    |
| contact.html          | No errors    |
| inventory_clone.html  | Errors fixed |
| inventory_detail.html | Errors fixed |
| inventory.html        | Errors fixed |
| landing_page.html     | No errors    |
| login.html  	        | Errors fixed |
| logout.html           | Errors fixed |
| privace_policy.html   | No errors    |
| saved_list.html       | No errors	   |
| signup.html  	        | No errors    |


<br>

**Fixed errors**
<details>
  <summary>Inventory page</summary>

  ![Inventory page](docs/readme_images/inventory_page_errors.png)
  ![Inventory page](docs/readme_images/inventory_page_no_errors.png)
</details>


<details>
  <summary>Inventory detail page</summary>

  ![Inventory detail page](docs/readme_images/inventory_detail_error.png)
  ![Inventory detail page](docs/readme_images/inventory_detail_no_errors.png)
</details>


<details>
  <summary>Inventory clone page</summary>

  ![Inventory clone page](docs/readme_images/inventory_clone_errors.png)
  ![Inventory clone page](docs/readme_images/inventory_clone_no_errors.png)
</details>

<details>
  <summary>Log In page</summary>

  ![Log In page](docs/readme_images/login_page_errors.png)
  ![Log In page](docs/readme_images/login_page_no_errors.png)
</details>

<details>
  <summary>Log out page</summary>

  ![Log out page](docs/readme_images/log_out_page_errors.png)
  ![Log out page](docs/readme_images/logut_page_no_errors.png)
</details>

### CSS
No errors were found when passing my CSS file through
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

<details>
  <summary>CSS</summary>

  ![Jshint](docs/readme_images/css_validation.png)
</details>


### JavaScript
No errors were found when passing the javascript code through
[Jshint](https://jshint.com).

<details>
  <summary>Jshint</summary>

  ![Jshint](docs/readme_images/jshint_validation.png)
</details>

### Python
All Python files were run through Pep8. A lot of errors were
returned. The errors involved too long lines, whitespaces, trailing
whitespaces, blank lines and "continuation line under-indented for visaul
indent. I resolved the trailing whitespace issue by enabling "Trim Trailing
Whitespace" in file -> preferences -> settings, under the section file here
in Gitpod. I also added a ruler in settings (settings.json) set to 78 to make
sure that the lines I needed to correct wouldn't exceed that line. I resolved
all the errors and ran the code for each page through Pep8 again and no errors were returned.


<details>
  <summary>Pep8 errors</summary>

  ![Python Pep8](docs/readme_images/pep8_validation_errors.png)
  ![Python Pep8](docs/readme_images/pep8_validation_errors2.png)
</details>

<details>
  <summary>Pep8 all clear</summary>

   ![Python Pep8](docs/readme_images/pep8_validation_clear.png)
</details>



### Lighthouse
Ligthouse testing was carried out in Incognito mode to achieve best results.
<details>
  <summary>Lighthouse results desktop</summary>

   ![Lighthouse desktop](docs/readme_images/lighthouse_desktop.png)
</details>

<details>
  <summary>Lighthouse results mobile</summary>

   ![Lighthouse mobile](docs/readme_images/lighthouse_mobile.png)
</details>

## Browser Testing

Inventory Manager was tested on Microsoft Edge, Google Chrome, Firefox and Safari browsers and no issues were noted.

| Browser               | Functionality| Layout  |
|---------------------- |------------- |---------|
| Chrome                |       ✔     |     ✔   |
| Edge                  |       ✔     |     ✔   |
| Firefox               |       ✔     |     ✔   |
| Safari                |       ✔     |     ✔   |




## Device Testing
  The website was tested on different devices to ensure responsiveness on various screen sizes. Chrome developer tools was used to test and to check the responsivness on multiple devices. I also used [Am I responsive](https://ui.dev/amiresponsive) to test the responsivness.


| Device                      | Functionality| Layout |
|---------------------------- |--------------|--------|
| Iphone 8                    |       ✔     |     ✔  |
| Ihone mini 12               |       ✔     |     ✔  |
| Iphone 13 Pro               |       ✔     |     ✔  |
| Samsung Galaxy S21          |       ✔     |     ✔  |
| Samsung Galaxy Tab S6 lite  |       ✔     |     ✔  |
| Laptop                      |       ✔     |     ✔  |
| Desktop                     |       ✔     |     ✔  |


  ## Friends and Family
   - Family members and friends were asked to test the website for bugs and overall experience.

## Manual Testing


### Landing Page
| Feature               | Action  | Expected Result                       | Pass/Fail |
|-----------------------|---------|---------------------------------------|-----------|
| **'Sign Up' Button**  | Click   | User is directed to Sign up form      | Pass      |
| **'Sign In' Button**  | Click   | User is directed to the Sign in form  | Pass      |

### Navigation
#### Not signed In

 The navigation links and the icon can be found in the navbar or in the drop-down menu on smaller screens.

| Feature 	           | Action    |  Expected Result                         | Pass/Fail |
|----------------------|-----------|------------------------------------------|-----------|
| **Icon**             | Click     | User is redirected back to landing page. | Pass      |
| **'Sign In' Link**   | Click     | User is directed to Login form.          | Pass      |
| **'Sign Up' Link**   | Click 	   | User is directed to Sign Up form.        | Pass      |


#### Signed In

 The navigation links and the icon can be found in the navbar or in the drop-down menu on smaller screens.

| Feature 	           | Action    |  Expected Result                                                                 | Pass/Fail |
|----------------------|-----------|----------------------------------------------------------------------------------|-----------|
| **Icon**             | Click     | User is redirected back to Inventory page.                                       | Pass      |
| **Dashboard**        | Display   | User is on the dashboard page with dashboard being displayed as the active link. | Pass      |
| **My lists**         | Click     | Once the user creates a list the user can find each list here, in a dropdown menu. When a list is clicked from here, the user is directed to the Saved List view.                                                                | Pass      |
| **Categories**       | Click 	   | User is directed to Categories page.                                             | Pass      |
| **Contact us**       | Click     | User is directed to Contact page.                                                | Pass      |
| **"Log out" Link**   | Click 	   | User is directed to Log out page.                                                   | Pass      |




### Sign up form
Unauthenticated users can create an account.

| Feature            | Action  | Expected Result                                                                                                                                                     | Pass/Fail |
|--------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Sign up form**   | Display | Renders the following input fields: Email, username, password and password confirm.                                                                                 | Pass      |
| **Submit** | Click | User is directed to a page where the user is informed that a verification link has been sent and the user needs to verify by clicking on that link, from their mail. After confirmation, the user will see the sign-in form instead. | Pass      |
|**Form incomplete** | Display | Incorrect or incomplete fields will be displayed with the relevant error and the user will remain on the page. | Pass |
| **'Sign In' Link** | Click | If user aldready has an account, user can click on the link leading to the sign in form instead. | Pass      |


### Login form

Authenticated users can sign in to existing account.

| Feature               | Action  | Expected Result                                             | Pass/Fail |
|-----------------------|---------|-------------------------------------------------------------|-----------|
| **Login form**        | Display | Renders the following input fields: username and password.  | Pass      |
| **Submit** | Click | Upon successful login, user is re-directed to the dashboard, with a self-closing success message with the username.  | Pass
|**Form incomplete** | Display | Incorrect or incomplete fields will be displayed with the relevant error and the user will remain on the page. | Pass |
| **Remember me**       | Check | When the "remember me" checkbox is ticked, the form is pre-populated with username and hidden password when user logs in again after the user have logged out.  | Pass      |
| **Password reset**    | Click | When clicked, the user is directed to the password reset page where the user fills out their email and submits. An email with the reset link is then sent to the user.  | Pass      |
| **''Google' button**  | Click   | User is directed to a separate page where user needs to confirm logging in with a third party. After that, user needs to enter email and password for gmail. Upon successful login, user is re-directed to the dashboard, with a self-closing success message with the username.  | Pass      |
| **"Sign Up" Link** | Click | If user doesn't have an account, user can click on the link leading to the sign up form instead. | Pass      |



### Create Inventory

Authenticated users can create inventory lists.

| Feature              | Action  | Expected Result                                      | Pass/Fail |
|----------------------|---------|------------------------------------------------------|-----------|
| **Plus sign icon**   | Click   | The inventory form is toggled                        | Pass      |
| **Inventory Form**   | Display | The input field and category dropdown are rendered.  | Pass      |
| **Submit**           | Click   | User is redirected to the Itemsform upon successful login, with a self-closing success message  | Pass      |
|**Form incomplete**   | Display | Incorrect or incomplete field will be displayed with the relevant error and the user will remain on the page. | Pass |
| **Unique name**      | Display | The list name needs to be unique. If not, an error message will display and user will remain on the page.  | Pass      |


Authenticated users can add items to their inventory lists as well as edit and delete items.


### Add Items to inventory
| Feature              | Action  | Expected Result                                      | Pass/Fail |
|----------------------|---------|------------------------------------------------------|-----------|
| **'Add item' button**  | Click   | If user clicks without adding an item a self-closing error message will display and user remains on the page. User can add multiple items by clicking on add item.                  | Pass      |
| **Edit and delete icons**   | Display | Once an item is added, an edit and delete icon will be visible on the same row.  | Pass      |
| **Edit icon**   | Click| When clicked, the readonly attribute is removed from the items row and inline editing is enabled.  | Pass
| **Delete icon**   | Click| When clicked, a confirm delete modal will display. If confirmed, a self-closing success message will display and user will stay on the Itemsform.  | Pass
| **Save list without items**   | Display | An error message will display and user remains on the page.  | Pass      |
| **Submit**           | Click| User is redirected to the Dashboard upon successful login, with a self-closing success message.   | Pass      |


### Dashboard
Authenticated users can see their inventory lists on the dashboard along with functionalities such as: scan QR-code, download QR-code, share QR-code, clone list and view list details (where the user can edit and delete a list.).

### Numbered list in alphabetical order
| Feature               | Action  | Expected Result                       | Pass/Fail |
|-----------------------|---------|---------------------------------------|-----------|
| **Number next to list name**    |Display  | When the inventory list is created, a number, starting at 1 will automatically be appended next to the list name.      | Pass      |
| **Sorted in alfabetical order**  |Display  | The list displayed in the dashboard are sorted in alfabetical order to find lists easily. | Pass      |


### QR-code
| Feature               | Action  | Expected Result                       | Pass/Fail |
|-----------------------|---------|---------------------------------------|-----------|
| **QR-code image**    | Display | The QR-code image is associated with the inventory list. When scanned the user will see the Saved list view without the edit/delete functionality since only the owner of the list can edit or delete a list.      | Pass      |


### Download and Share
| Feature               | Action  | Expected Result                              | Pass/Fail |
|-----------------------|---------|----------------------------------------------|-----------|
| **'Download' link**   | Click   | A new tab is opened with the QR-code image    | Pass      |
| **'Share' link**      | Click   | Users email with the QR-code link and a pre-populated message is displayed in a new window.  | Pass     |


### View Details
| Feature               | Action  | Expected Result                       | Pass/Fail |
|-----------------------|---------|---------------------------------------|-----------|
| **'View details' Button**  | Click   | User is directed to the Saved List view where the user can Edit and Delete the inventory list.      | Pass      |



### Clone list

Authenticated users can clone a list, so the user can reuse and/or adapt an existing list.
| Feature               | Action  | Expected Result                       | Pass/Fail |
|-----------------------|---------|---------------------------------------|-----------|
| **'Clone list' Button**  | Click   | User is directed to the Itemsform. | Pass      |
| **'Clone list' Itemsform**  | Display  | User can add more items, edit or delete items before cloning the list. | Pass      |
| **'Submit'**    | Click   | User is redirected to the dashboard with a self-closing success message. | Pass      |
| **The cloned list**  | Display  |"Cloned" is appended to the cloned list to avoid violating the unique name constraint. | Pass
| **Clone same list again**  | Click   |When the "clone list" button is clicked on the original list, an error message about list already being cloned is displayed and user remains on the page (the dashboard). | Pass      |



### Saved inventory list

Authenticated users will see the inventory list and edit and delete list functionality. Only list owner will see the view with the edit and delete option when QR-code is scanned.

| Feature               | Action  | Expected Result                               | Pass/Fail |
|-----------------------|-----------------|---------------------------------------|-----------|
|**Saved inventory list view**  | Click/Scan   | User is directed to the saved inventory list view by clicking on "View details", clicking on "My lists" in the navbar and choosing a list or by scanning the QR-code.                                                             | Pass      |
| **Saved list**  | Display   | User can view the inventory list and its content. | Pass      |
| **'Edit list' button**  | Click  | User can edit the list and upon click, the user will be directed to the Itemsform. There, the user can click on edit, delete or add items.  | Pass      |
| **'Delete list' button'**  | Click   |  When clicked, a confirm delete modal will display. If confirmed, a self-closing success message will display and user will be re-directed to the dashboard. | Pass      |


### Categories

Authenticated users can create unique categories, edit and delete.

| Feature              | Action  | Expected Result                              | Pass/Fail |
|----------------------|---------|----------------------------------------------|-----------|
| **Plus sign icon**   | Click   | The category form is toggled.                | Pass      |
| **Category Form**    | Display | The name input field is rendered.            | Pass      |
| **Submit**           | Click   | A success message with a self-closing success message will display and user stays on category page. | Pass      |
|**Incomplete form**   | Display | Incorrect or incomplete field will be displayed with the relevant error and the user will remain on the page. | Pass |
| **Unique name**      | Display | The category name needs to be unique. If not, an error message will display and user will remain on the page.  | Pass      |
| **Edit icon**   | Click   | When the icon is clicked, the readonly attribute is removed from the category name, and inline editing is enabled. A save button is also visible now. Upon successful submission, a self-closing success message will display and user remains on the page.               | Pass      |
 **Delete icon**   | Click   | When clicked, a confirm delete modal will display. If confirmed, a self-closing success message will display and user will remain on the page.           | Pass      |


### Contact Form
Authenticated users can submit a message using the contact form.

| Feature              | Action  | Expected Result                                            | Pass/Fail |
|----------------------|---------|------------------------------------------------------------|-----------|
| **'Contact us' link**  | Click   | Takes the user to the contact form.                         | Pass      |
| **Contact Form**     | Display | Name, email and message are all required fields.           | Pass      |
| **Submit**           | Click   | A success message with a self-closing success message will display and user stays on the page. | Pass      |
| **Incomplete form**  | Display | Incorrect or incomplete field will be displayed with the relevant error and the user will remain on the page.                         | Pass      |
| **Email confirmation**| Display| User will get an email confirmation of the recieved message.                        | Pass      |


### Log out
Authenticated users can sign out from their account.

| Feature 	           | Action    |  Expected Result                         | Pass/Fail |
|----------------------|-----------|------------------------------------------|-----------|
| **'Logout' link** | Click | User is directed to logout page, asking user to confirm or cancel the logout action. | Pass |
| **Sign out button** | Click | When clicked, a self-closing success message of the logout is displayed to the user. User is re-directed to the landing page with the navbar for unauthenticated users.      | Pass      |
| **Cancel button** | Click | When clicked, user is re-directed to the dashboard. | Pass |



### Footer
The footer remains the same for authenticated and unauthenticated users.

| Feature 	           | Action    |  Expected Result                         | Pass/Fail |
|----------------------|-----------|------------------------------------------|-----------|
| **Social media link icons** | Click | When clicked, a new tab is opened with the relevant social media site. | Pass |
| **Privacy Policy link** | Click | When clicked, a new tab is opened to the privacy policy page. | Pass |




## Bugs
The bugs listed below are bugs that I spent a longer amount of time to resolve or that required assistance from Tutor Support. As this is my first Django project, most of the errors and bugs I encountered were learning curves and initial hurdles.

**Bug** | **Description** | **Actions to Resolve** | **Result** |
|:-----|:------|:------|:-----|
|Items didn't get added in the database.|When setting up the inventory form, addition and deletion of items were also handled there. But the items list was empty, the items didn't get added.|Solution: I changed approach and set up a separate form for addition of items.| Resolved
|Itemsform inputfields not working correctly nor the form errors upon sign-up and sign-in. |When editing and adding items, the form wasn't handling the addition of new items correctly. The form errors wasn't working at all upon sign-up and sign-in. User could just proceed even if the requirements weren't met. |Solution: I exchanged widget tweaks to crispy forms and then got it to work properly.| Resolved
|Items didn't get deleted in the front end nor in the database. |When clicking on the delete icon, the delete modal was displayed correctly. When confirmed, a success message would display even though the item wasn't deleted from the list nor in the backend.|Solution: I reached out to tutor support as I spent some time trying to solve this. Finally, changing the class to delete-link instead of delete-icon in the Javascript code fixed the issue.| Resolved
|Clicking on the "Add item" button would display a success message without an item being added. |When clicking on the add item button without adding an item both in the inventory detail view, and in the clone list view, a success message would display.|Solution: I reached out to tutor support as I spent a lot of time trying to solve this. Using length in the inventory detail view to check if an item was added resolved the issue. A check if an item was added or not in the clone list view resolved the issue.| Resolved
|Add category directly in the inventory form not functioning.|I implemented the functionalty to add a new category at the same time as creating the inventory list. This didn't function properly as the input field kept rendering an error.|Solution: I had to change approach since this seemed to complicated to set up. I created a separate page where categories could be added.| Resolved
|A user could see other users categories|During the test phase I discovered that other users' categories would be visible in my category dropdown menu.|Solution: Since the categories are supposed to be personal, and connected to the user, I had to add a user field in my category model to connect the category to the specific user.| Resolved
|A user can create another "General" category.|A "General" category is provided to the user so that the user can choose that category and create a list instantly. A category is unique, same as the inventory name and duplicates can't be created.|Since a "General" category already is provided, the user doesn't have to create that specific category. But in this specific case, the user can create another General category. Due to time constraints and the fact that is not that likey that the user will create another "General" category if one already exists, I choose to leave this issue unresolved for now.| Unresolved
|Duplicate social login buttons|When I added the social media providers in the admin panel, the social login buttons were suddenly duplicated.|Solution: I looked through the relevant templates, debugged and removed code to try and find the source of the problem. Eventually, when I removed the sites, except for the live site I had added in the admin panel the duplicate buttons disappeared.| Resolved
|Scanned QR-code was leading to a relative path|When the QR code was scanned it would only display this path, not leading anywhere: /inventory/153/saved/. When scanned, the saved list view for that specific inventory was supposed to be displayed.|Solution: I did a lot of research and found that Django's reverse function generated a relative path into the QR code instead of the full absolut URL. I modified the method in my Inventory model to return the full absolute URL.| Resolved
|Migration History Error.| InconsistentMigrationHistory. This error occured when I installed the 'django.contrib.sites' framework to add the social account login.| Debugging and deleting records so the order would be correct since that was the cause of the error.| Resolved
|Unique constraint error| Can't clone the original list again due to the uniqe name constraint. To clone a cloned list is working by appending "cloned" to the list name, but if user tried to clone the original list again, an error would occur.|Solution: I added error handling so an error message renders if user tries to clone the original list again.| Resolved
|Mixed content warning| After deployment, the QR-code image wouldn't display and a mixed content warning would appear in the console.|Solution: After a lot of research it became cleare that the issue was about images loaded over HTTP and not HTTPS so I needed to add secure_url to ensure that the image was delivered over HTTPS and that resolved the mixed content warning.| Resolved




## Python Automated Testing
Automated testing was conducted on specific components of the application, focusing on key features utilizing Django's built-in 'TestCase' class. Although, given more time the intention was to extend the automated tests to include more features and scenarios. A thourough manual testing process was also implemented.

**Test** | **Description** | **Result** |
|:-----|:------|:------|
|test_inventory_form_valid| Verifies that the "InventoryForm" is validated when provided with a valid category and name. This test ensures that the form's validation logic properly accepts correct input.| Passed
|test_inventory_form_invalid| Tests the "InventoryForm" for correct handling of invalid submissions, specifically when mandatory fields are missing. This test is to confirm that the form's logic handles incomple och incorrect submissions correctly.| Passed
|test_items_form_valid| Verifies that the "ItemsForm" validates correctly when provided with valid data. This test ensures that the form properly handles valid user inputs for item creation.| Passed
|test_items_form_invalid| Test the form handling for invalid submissions, such as when item name is missing.  This test is to confirm that the form's logic handles incomplete och incorrect submissions correctly to prevent data integrity errors.| Passed
|test_create_inventory| Tests the functionality of creating a new inventory list through a POST request, verifying that the list is correctly added to the database and that the user is redirected correctly.| Passed
|test_delete_list| Tests the functionality of deleting an inventory list, verifying that after deletion, the list is deleted from the database and the user redirected correctly.| Passed