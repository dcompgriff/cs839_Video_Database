# 839 Project Stage 2: IMDB and Movie Numbers Web Page Movie Extraction

## Introduction

This project follows the guidelines for AnHai's CS 839 Data Analysis course for project stage 2, and contains scripts and data for two movie lists from IMDB.com and the-numbers.com. We have the scripts arranged in a code folder and the json and csv formatted data in the data folder. 

## Links

* [IMDB Website](http://www.imdb.com/list/ls032600534)
* [Movie Numbers Website](https://www.the-numbers.com/movies/\#tab=letter)
* [Data Folder](DATA/)- Generated .json and .csv data sets.
* [Code folder](CODE/) - Scripts for performing the parsing and generating the data sets.
* [Pdf Detailing The Project](839_Project_Stage_2.pdf) - Pdf describing the process of movie extraction in detail

## Running the Extractors

### Scraping the IMDB Website

Running the scraper to scrape the IMDB website is shown below. If you are running the scraper for the first time, then make sure to use the "--generate" optional argument. This optional argument tells the scraper to actually go to the web url to pull information for creating the .csv file, and generates a corresponding intermediate json file. If the json file has already been generated, then the optional --generate option can be dropped. However, this script assumes that the "imdb_movies.json" file has already been generated in that case, and that the file is in the same folder as the scraper script. Also note that if you already have a generated "imdb_movies.json" file generated and want to generate another file, you need to remove the original file first before generating a new file. If you don't, the parser will throw json parse errors.

```
cd CODE/
python scrapeIMDB.py --generate
```
### Scraping the Movie Numbers Website

Running this scraper is the same as running the previous scraper.

```
cd CODE/
python scrapeMovieNumbers.py --generate
```


## Built With

* [Python 3.4.3](https://www.python.org/)
* [Numpy 1.13.1](http://www.numpy.org/) - Numerical matrix lib
* [Pandas 0.21.0](https://pandas.pydata.org/) - Data manipulation lib
* [Scrapy 1.5.0](https://scrapy.org/) - Web scraping framework

## Authors

* **Daniel Griffin** - [dcompgriff](https://github.com/dcompgriff)
* **Yudhister Satija**
* **Mitali Rawat**




