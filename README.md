<div align="center"><h3>IMBD-API</h3></div>
<div align="center">This is an API for getting all IMBD rated movies information. Admin rights available for users.</div>


### Table Of Contents
* [About Api](#about-api)
* [Design Model](#design-model)
* [Tech Power](#tech-power)
* [Prerequisites](#prerequisites)
* [Usage Steps](#usage-steps)
* >> [Get data from resource](#get-data-from-resource)
* >> [ADD data to resource](#add-data-to-resource)
* >> [DELETE data to resource](#delete-data-to-resource)

### About Api
This Api is designed for the demonstration of Fynd IMDB-Task. It includes all features given which are accesible from UI of Website.
Api design is decided using a monolithic approach which has a dedicated database, a web server and static content in UI which also follows the typical MVC pattern.
This IMBD Api's purpose is to serve users about the information of movies that is stored in IMBD database. Usage is simple and easily integrable.


### Design Model
Whilst designing the model. There are level of access rights are kept in mind.
1. User is anonymous i.e. not authenticated : Authenticated users can only get access to fetch only for top 10 rated movies according to IMBD rating.
2. User is authenticated : Users who are authenticated can have access to get all movies data and even search it. A valid API token is required for both.
3. Admin level: A utility from UI is designed in such a way that user just have to click a button and get admin access. We can commercialise it but just kept it simple as per the demo purpose.
4. Api is easily accessed and can be hit through Postman / requests(in Python) module etc.

### Tech Power
I have made this basic version which can be wasily commercialised with a lot of effort, tea and have used:
* Django Framework
* Postgresql
* Heroku

### Prerequisites
1. If you are using requests module to hit Api. Install it in Python using:
<pre>pip install requests</pre>

2. If you use postman. Use the following link:
<pre>https://www.postman.com/downloads/</pre>

3. Register on the webiste using google signup:
<pre>https://imbdweb.herokuapp.com/</pre>

### Usage Steps
The usage for accessing information is simple. Follow the below steps:
1. Go to https://imbdweb.herokuapp.com/. Login with google. Or if you decide not to, then we have a button on landing page which can give you an idea about hitting and getting the data. This is very useful when the beginners don't know that how to use the API and how the data looks like.
2. After you login, you are authenticated. You must see the welcome message for your username through which you just logged in.
3. Now you can click on Use API on navbar and generate API token on the left side. Once token is generated, won't change. As for now it does not have the expiration period/ date. You can use that forever.
4. Though this token you are an authenticated user. Congratulations!!
5. Now you can hit the Api by just clicking on button: Get all movies or write the movie name in search box and get the search data then and there.
6. If you want to become an admin. So as to have addition, removal or deletion and even edit or update the data, you can navigate to page set admin.
7. Now if you are on set admin page, you can click **"Set me Admin"** button and can get the admin rights in a go. Remember this is just for demo ease.
8. Now when you are admin, you have the power of add, update, delete on the webapp resource.
9. Test the api using auth token to GET the data, SEARCH for the data, ADD the data to resource, UPDATE the data and DELETE the data.
10. While testing as a authenticated user:


* ### GET data from resource
1. Provide API token to validate in headers. URL: https://imoxie.herokuapp.com/getMovies/.
**Expected is ** - You will get a response with status 200.
>>  Without token: you will only get top 10 rated movies. Remember!

* ### SEARCH the movie data
1. Provide API token to validate in headers. URL: https://imoxie.herokuapp.com/searchMovies/<yourmoviename>/.
  **Expected is ** - You will get a response with status 200.
  >>  Without token: you will only get status OK but error message: You don't have a valid token. You won't be able to see the searched movie.

11. For Admin users:
  
* ### ADD data to resource
  1. We can ingest data in the form of JSON for single or array of JSONs for multiple rows.
  URL: https://imoxie.herokuapp.com/addData/.
  Auth token is reuired and request would be POST.
  **Expected is ** - You will get a response with status 200. And a message that Data is loaded successfully.
  >>  Without token: you don't have admin rights!
  
* ### UPDATE data to resource
  1. We can update data with passing body as JSON. With key value pair. Key--> Column and Value -->updated value that you want to update with.
  movie_id > you can get from response of get that you would want to update.
  URL: https://imoxie.herokuapp.com/updateData/<movie_id>/.
  Auth token is reuired and request would be PATCH.
  **Expected is ** - You will get a response with status 200. And a message that <yourkeycolumn(s)> updated for id:yourid.
  >>  Without token: you don't have admin rights!
  
  * ### DELETE data to resource
  1. We can delete the data with:
  URL: https://imoxie.herokuapp.com/deleteData/<movie_id>/.
  Auth token is reuired and request would be DELETE.
  **Expected is ** - You will get a response with status 200. And a message that row with id :yourid is deleted.
  >>  Without token: you don't have admin rights!
 
 
 ### Enjoy the Api!!!
