# Trusty Bank
Do you have what it takes to hack the Trusty Bank?  The answer is almost probably, yes.  But, maybe you want to be sure.  Head on over to [tweddle-acm.herokuapp.com](https://tweddle-acm.herokuapp.com/) and give it a try!


## Goals
Try to accomplish the following:

* Find the user with the highest balance
* Login as any user
* Transfer another user's money to your account


## Run it local
You can run the website locally in a docker container.

1. Clone this repository

	```
	git@github.com:Tweddle-SE-Team/acm.git && cd acm
	```

2. Install [docker](https://docs.docker.com/engine/installation/#desktop) and [docker-compose](https://docs.docker.com/compose/install/)

3. Run the app

    ```
    docker-compose up
    ```

4. Navigate to [127.0.0.1:8000](http://127.0.0.1:8000) in your browser

> Note:  You may need to add `127.0.0.1	db` to your local hosts file.  For Mac the host file is located at `/ect/hosts`


## Deploy it to Heroku

1. Clone this repository

	```
	git@github.com:Tweddle-SE-Team/acm.git && cd acm
	```

2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

3. Create an application in Heroku

    ```
    heroku create my-unique-application-name
    ```

4. Push the code to the Heroku application

    ```
    git push heroku master
    ```

> Note: You can reset the database by running `heroku run './reset.sh' --app tweddle-acm`