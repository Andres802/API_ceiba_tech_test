 CEIBA API

This API allows you to make rent paymenmts. You can create, update, get payments,


## Installation

To start using this API you must install `Python 3.6.13` and `MySQL 5.7.33`. (versions used in develop).

Now, follow this steps:

1. Choose a place in your computer and clone this repository. Type in your terminal:

```
$ git clone PRIVATE REPOSITORY
```

2. Once the repository has been downloaded, enter to it and create a python virtual enviroment. (This step is not required but it is highly recomended).

```
$ cd ceiba_arriendo
$ python3 -m venv env

```

The above command will create a folder called `env`.

> Make suere to use the right Python version at time of creating the virtual enviroment. 

3. Install the requirements needed to run the API in the enviroment.

```
$ ./env/bin/activate
$ pip install -r requirements.txt
```

4. Configure the database.

This API uses a MySQL database, the reason why you must configure one. For this it's included in this repository a file called `sql_setup.sql` which will help you to do it easily. So in your terminal type:

```
$ cat sql_setup.sql | mysql -u root -p
```

Once you run the above command you must enter the passoword and wether all of it was OK the database should be created.

> You can change database name, username and password, to do so, modify the `setup_db.sql` file before runnig the above command.



5. Prepare migrations to the databse 

```
python manage.py makemigrations
```

6. Migrate tables

```
pyhton manage.py migrate

```

## Usage

After setup proccess above the API is ready to be executed. To do it you only to need to execute below command in your terminal:

```
pyhton manage.py runserver
```


Now, the API is running in the 8084 port ready to receive requests. 
For this use a client like `Postman`.

#### List of endpoints:

Pagos:

```
* GET    api/pagos              List Pagos
* POST   api/pagos              Create Pago
* PUT    api/pagos              Update Pago
```



#### Look at this example:

[Youtube Video Example](https://youtu.be/uBloA-6UWIQ)

## Support

If you have any problem executing this AP, please do not hesitate to contact me at [Twitter](https://twitter.com/codesectest)https://github.com/Andres802

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

#### Andres Barrera