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

```git clone https://github.com/arturmarxandermann/test-challenge```

Access the *test-challenge* folder

```cd test-challenge```

Then build the Docker image

```docker-compose build```

The docker-compose already takes care of linking the folders
of computer and container. Build the container

```docker-compose up -d ```

which must be open, which can be checked with

```docker ps```

![Screenshot from 2022-04-28 22-21-42](https://user-images.githubusercontent.com/71330975/165871812-341d3f97-03ab-4beb-8739-de95df2fc17f.png)

Finnaly,  run the scrapy crawler inside the container

```docker-compose exec scrapy bash -c 'scrapy crawl corrs'```

which can take a few minutes, because the option DOWNLOAD_DELAY = 3 is established in settings.
This can be used to throttle the crawling speed to avoid hitting servers too hard.

The results are in the Data folder, separated by the acronyms of the states, as shown in the following figure
![Screenshot from 2022-04-28 22-20-57](https://user-images.githubusercontent.com/71330975/165871705-3047e940-116c-4de4-8f26-b00a995c8f23.png)


## Tests 
To verify the connection to the website, we use the pytest package.
In the test-challenge folder, do

```python3 -m pytest test_corrs.py```

A message like below validates the test

![Screenshot from 2022-06-01 18-12-18](https://user-images.githubusercontent.com/71330975/171502718-5be91b7c-ab11-4ed8-ab3c-f48d6d9ad9a3.png)










 
