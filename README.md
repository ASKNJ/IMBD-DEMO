<div align="center"><h3>IMBD-API</h3></div>
<div align="center">This is an API for getting all IMBD rated movies information. Admin rights available for users.</div>


### Table Of Contents
* [About Api](#about-api)
* [Design Model](#design-model)


### About Api
This Api is designed for the demonstration of Fynd IMDB-Task. It includes all features given which are accesible from UI of Website.
Api design is decided using a monolithic approach which has a dedicated database, a web server and static content in UI which also follows the typical MVC pattern.
This IMBD Api's purpose is to serve users about the information of movies that is stored in IMBD database. Usage is simple and easily integrable.


### Design Model
Whilst designing the model. There are level of access rights are kept in mind.
1. User is anonymous i.e. not authenticated : Authenticated users can only get access to fetch only for top 10 rated movies according to IMBD rating.
2. User is authenticated : Users who are authenticated can have access to get all movies data and even search it. A valid API token is required for both.
3. Admin level: A utility from UI is designed in such a way that user just have to click a button and get admin access. We can commercialise it but just kept it simple as per the demo purpose.
