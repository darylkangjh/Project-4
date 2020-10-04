# KANGA | Digital Marketing 

## Introduction 
KANGA is a digital marketing start-up focused on delivering quality digital marketing consultancy and services. The purpose of this project is to create a platform to showcase KANGA's works as well as allow first-time users to hire our services through a native e-commerce function.

KANGA hopes to use this website to acquire new sales through it's e-commerce platform.

Visit the site [here](https://dk-kanga.herokuapp.com/) 

## How to demo the project 

### To Log in as a regular user: 
| Username | regularuser@mailinator.com |
|----------|----------------------------|
| Password | pass123word                |

### Privileges of a regular user
\* Able to add to cart
\* Able to checkout purchases 

To Log in as a super user: 
| Username | kolipop@mailinator.com |
|----------|------------------------|
| Password | pass123word            |

### Privileges of a super user
<ol>
<li> Able to access navbar admin tab  </li>
\* Able to access django admin panel via the shortcut admin tab 
\* Able to create Services products 
\* Able to creat Assets products 
\* Able to delete all products 
\* Able to edit all products 
</ol>


## Technologies Used 
1. Django-Taggit for tagging module https://django-taggit.readthedocs.io/en/latest/getting_started.html#
2. CrispyForms (Together with Boostrap 4) https://django-crispy-forms.readthedocs.io/en/latest/install.html#

## Credits 
1. GitIgnore template by www.toptal.com/developers/gitignore/api/django.


## Testing 

### Manual Testing 

Manual testing was done to ensure the front-end routes are protected and allowed for 

| Step | Description                                                                                | Expected Outcomes                                                                                                                                                  | Actual Test |
|------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 1    | Load index page                                                                            | Page should load with a "Please login" above the slider or a "Welcome <username>".                                                                                 | As expected |
| 2    | Load Services page                                                                         | Page should load with a banner. Digital Marketing services should appear below the banner together with the search tab                                             | As expected |
| 3    | Add a service                                                                              | Only super user can add a service. Item added via the admin tab on the navbar available only to superuser.                                                         | As expected |
| 4    | Add a service not available to regular user                                                | Regular user will not be able to see the admin panel. Testing done by loggin in as regular user.                                                                   | As expected |
| 5    | Edit a service not available to regular user                                               | Regular user will not be able to edit the individual products. Testing done by logging in as regular user.                                                         | As expected |
| 6    | Edit a service not available to regular user through manual keying of route in the url     | Regular user will not be able to edit the individual products by manually entering a route and id number in the url. Testing done by logging in as regular user.   | As expected |
| 7    | Add a service not available to anonymous user                                              | Anonymous user will not be able to see the admin panel. Testing done by not logging in.                                                                            | As expected |
| 8    | Edit a service not available to anonymous user                                             | Anonymous user will not be able to edit the individual products. Testing done by not logging in.                                                                   | As expected |
| 9    | Edit a service not available to anonymous user through manual keying of route in the url   | Anonymous user will not be able to edit the individual products by manually entering a route and id number in the url. Testing done by not logging in.             | As expected |
| 10   | Delete a service not available to regular user through manual keying of route in the url   | Regular user will not be able to delete the individual products by manually entering a route and id number in the url. Testing done by logging in as regular user. | As expected |
| 11   | Delete a service not available to anonymous user through manual keying of route in the url | Anonymous user will not be able to delete the individual products by manually entering a route and id number in the url. Testing done by not logging in.           | As expected |
| 12   | Delete a service                                                                           | Only super user can delete a service. delete button is only available to superuser on individual product. On delete, item removed.                                 | As expected |
| 13   | Edit a service                                                                             | Only super user can edit a service. edit button is only available to superuser on individual product. On edit, form with populated data shows for editing.         | As expected |
| 14   | Search test for services                                                                   | "Photo" entered into Item Name should only display photography service.                                                                                            | As expected |
| 15   | Add an asset                                                                               | Only super user can add an asset. Item added via the admin tab on the navbar available only to superuser.                                                          | As expected |
| 16   | Add an asset not available to regular user                                                 | Regular user will not be able to see the admin panel. Testing done by loggin in as regular user.                                                                   | As expected |
| 17   | Edit a asset not available to regular user                                                 | Regular user will not be able to edit the individual products by manually entering a route and id number in the url. Testing done by logging in as regular user.   | As expected |
| 18   | Add a asset not available to anonymous user                                                | Anonymous user will not be able to see the admin panel. Testing done by not logging in.                                                                            | As expected |
| 19   | Edit a asset not available to regular user through manual keying of route in the url       | Regular user will not be able to edit the individual products by manually entering a route and id number in the url. Testing done by logging in as regular user.   | As expected |
| 20   | Edit a asset not available to anonymous user                                               | Anonymous user will not be able to see the admin panel. Testing done by not logging in.                                                                            | As expected |
| 21   | Edit a asset not available to anonymous user through manual keying of route in the url     | Anonymous user will not be able to edit the individual products by manually entering a route and id number in the url. Testing done by not logging in.             | As expected |
| 22   | Delete a asset not available to regular user through manual keying of route in the url     | Regular user will not be able to delete the individual products by manually entering a route and id number in the url. Testing done by logging in as regular user. | As expected |
| 23   | Delete a asset not available to anonymous user through manual keying of route in the url   | Anonymous user will not be able to delete the individual products by manually entering a route and id number in the url. Testing done by not logging in.           | As expected |
| 24   | Delete a asset                                                                             | Only super user can delete a asset. delete button is only available to superuser on individual product. On delete, item removed.                                   | As expected |
| 25   | Edit a asset                                                                               | Only super user can edit a asset. edit button is only available to superuser on individual product. On edit, form with populated data shows for editing.           | As expected |
| 26   | Search test for asset                                                                      | "Monkey" entered into Item Name should only display "Space Monkey".                                                                                                | As expected |
| 27   | Add to cart                                                                                | Items added to cart from services and assets will be totalled up as per items                                                                                      | As expected |
| 28   | Checkout                                                                                   | Upon checkout and redirect to stripe, payment made in test mode should reflect a successful webhook on stripe                                                      | As expected |