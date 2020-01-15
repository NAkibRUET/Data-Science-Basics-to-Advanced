# Data-Science-Basics-to-Advanced

## Scrapping with Scrapy
### To create scrapy class run command 
```
scrapy genspider <file_name> <domain_name>
```
### To run scrapy class run command 
```
scrapy runspider <file_name>
scrapy runspider <file_name> -o <file_where_to_WRITE_scrapped_data>
```

### Scrapping in CMD. 
#### It will give a response if it's successfully scraped
```
scrapy shell <web_url>
```
#### Furthermore (working with JSON format data)
```
import json
data = json.loads(response.text)
data
data.keys()
```
etc.
