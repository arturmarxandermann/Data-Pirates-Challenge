# Data Pirates Challenge
## Abstract
In this test we will build a project to obtain information about several cities
from Brazil, including the ZIP code range, name, and UF name.

## Requirements
The entire application is virtualized through docker containers, so 
to run the crawler you just need to install the following softwares:

| Program | Installation |
| --- | --- |
|Docker | https://docs.docker.com/engine/install/  |
|Docker-compose | https://docs.docker.com/compose/install/ |

The crawler uses the Scrapy framework as a search engine, and is written in the Python programming language.
It also uses the standard *os* and *json* libraries.

## Installation 
First of all you need to clone that repository

```git clone https://github.com/arturmarxandermann/Data-Pirates-Challenge```

Access the *test-challenge* folder

```cd test-challenge```

Then build the Docker image

```docker-compose build```

The docker-compose already takes care of linking the folders
of computer and container. Build the container

```docker-compose up -d ```

which must be open, which can be checked with

```docker ps```

![Screenshot from 2022-06-01 18-58-56](https://user-images.githubusercontent.com/71330975/171508951-96e35c02-d1de-47b5-b291-4870718fc9d9.png)

Finnaly,  run the scrapy crawler inside the container

```docker-compose exec scrapy bash -c 'scrapy crawl corrs'```

which can take a few minutes, because the option DOWNLOAD_DELAY = 1 is established in settings.
This can be used to throttle the crawling speed to avoid hitting servers too hard.

The results are in the Data folder, separated by the acronyms of the states, as shown in the following figure
![Screenshot from 2022-04-28 22-20-57](https://user-images.githubusercontent.com/71330975/165871705-3047e940-116c-4de4-8f26-b00a995c8f23.png)




## Tests 
To verify the connection to the website, we use the pytest package.
With the container open, do

```docker-compose exec scrapy bash -c 'pytest test_corrs.py'```

A message like below validates the test

![Screenshot from 2022-06-01 18-12-18](https://user-images.githubusercontent.com/71330975/171502718-5be91b7c-ab11-4ed8-ab3c-f48d6d9ad9a3.png)


## Closing the container

After performing the test,

the docker container can be shut down with the command

```docker kill <container_id>```

where the id can be obtained with docker ps command.









 
